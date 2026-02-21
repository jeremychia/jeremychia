"""GitHub PR scraper using Playwright for comprehensive data extraction."""

import asyncio
import logging
import re
from datetime import datetime, timedelta
from typing import List, Optional, Dict, Any
from urllib.parse import urljoin, urlparse

from playwright.async_api import async_playwright, Browser, BrowserContext, Page
from bs4 import BeautifulSoup

from .models import (
    GitHubPRData, ReviewMetrics, TimeMetrics, FileAnalysis, 
    EngagementMetrics, AnalysisConfig, ScrapingResult
)

logger = logging.getLogger(__name__)


class GitHubPRScraper:
    """Playwright-based GitHub PR scraper for comprehensive data extraction."""
    
    def __init__(
        self,
        headless: bool = True,
        slow_mo: int = 1000,
        timeout: int = 30000,
        concurrent_pages: int = 3,
        user_data_dir: Optional[str] = None
    ):
        """Initialize the scraper with configuration."""
        self.headless = headless
        self.slow_mo = slow_mo
        self.timeout = timeout
        self.concurrent_pages = concurrent_pages
        self.user_data_dir = user_data_dir
        self.browser: Optional[Browser] = None
        self.context: Optional[BrowserContext] = None
        
    async def __aenter__(self):
        """Async context manager entry."""
        self.playwright = await async_playwright().start()
        
        # Launch browser with persistent context if user_data_dir is provided
        if self.user_data_dir:
            self.context = await self.playwright.chromium.launch_persistent_context(
                user_data_dir=self.user_data_dir,
                headless=self.headless,
                slow_mo=self.slow_mo
            )
            self.browser = None  # Not needed for persistent context
        else:
            self.browser = await self.playwright.chromium.launch(
                headless=self.headless,
                slow_mo=self.slow_mo
            )
            self.context = await self.browser.new_context()
        
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        if self.context:
            await self.context.close()
        if self.browser:
            await self.browser.close()
        if hasattr(self, 'playwright'):
            await self.playwright.stop()
    
    async def check_github_session(self) -> bool:
        """Check if user is logged into GitHub in current browser session."""
        try:
            page = await self.context.new_page()
            await page.goto("https://github.com/settings/profile")
            
            # Wait a moment for redirect or login page
            await page.wait_for_timeout(2000)
            
            # Check if we're on a settings page (logged in) or login page
            current_url = page.url
            
            if "/login" in current_url:
                logger.warning("Not logged into GitHub. Please login to GitHub in your browser first.")
                await page.close()
                return False
            elif "/settings" in current_url:
                logger.info("GitHub session detected and valid")
                
                # Try to get username from the page
                try:
                    username_elem = await page.query_selector('input[name="user[login]"]')
                    if username_elem:
                        username = await username_elem.get_attribute('value')
                        logger.info(f"Logged in as: {username}")
                except:
                    pass
                    
                await page.close()
                return True
            else:
                logger.warning("Unable to determine GitHub login status")
                await page.close()
                return False
                
        except Exception as e:
            logger.error(f"Session check failed: {e}")
            if 'page' in locals():
                await page.close()
            return False
    
    async def get_user_prs(self, config: AnalysisConfig) -> ScrapingResult:
        """Get all PRs for a user based on configuration."""
        start_time = datetime.now()
        all_prs = []
        errors = []
        
        # Build search URL
        search_query = self._build_search_query(config)
        search_url = f"https://github.com/search?q={search_query}&type=pullrequests&s=created&o=desc"
        
        logger.info(f"Starting PR search with query: {search_query}")
        
        try:
            # Get list of PR URLs from search results
            pr_urls = await self._get_pr_urls_from_search(search_url, config.max_prs)
            
            logger.info(f"Found {len(pr_urls)} PRs to scrape")
            
            # Process PRs in batches with concurrency control
            semaphore = asyncio.Semaphore(self.concurrent_pages)
            
            async def process_pr(url: str) -> Optional[GitHubPRData]:
                async with semaphore:
                    try:
                        return await self._scrape_single_pr(url)
                    except Exception as e:
                        error_msg = f"Failed to scrape PR {url}: {e}"
                        logger.error(error_msg)
                        errors.append(error_msg)
                        return None
            
            # Run scraping tasks
            tasks = [process_pr(url) for url in pr_urls]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # Filter successful results
            for result in results:
                if isinstance(result, GitHubPRData):
                    all_prs.append(result)
                elif isinstance(result, Exception):
                    errors.append(str(result))
            
        except Exception as e:
            logger.error(f"Error in get_user_prs: {e}")
            errors.append(str(e))
        
        end_time = datetime.now()
        processing_time = (end_time - start_time).total_seconds()
        
        return ScrapingResult(
            prs=all_prs,
            total_processed=len(pr_urls) if 'pr_urls' in locals() else 0,
            successful_scrapes=len(all_prs),
            failed_scrapes=len(errors),
            errors=errors,
            processing_time_seconds=processing_time
        )
    
    def _build_search_query(self, config: AnalysisConfig) -> str:
        """Build GitHub search query from config."""
        query_parts = [f"author:{config.username}"]
        
        if config.organization:
            query_parts.append(f"org:{config.organization}")
        
        if config.repositories:
            repo_queries = [f"repo:{repo}" for repo in config.repositories]
            query_parts.append(f"({' OR '.join(repo_queries)})")
        
        if config.date_from:
            query_parts.append(f"created:>={config.date_from.strftime('%Y-%m-%d')}")
        
        if config.date_to:
            query_parts.append(f"created:<={config.date_to.strftime('%Y-%m-%d')}")
        
        if not config.include_drafts:
            query_parts.append("-is:draft")
        
        query_parts.append("is:pr")
        
        return " ".join(query_parts)
    
    async def _get_pr_urls_from_search(self, search_url: str, max_prs: Optional[int] = None) -> List[str]:
        """Extract PR URLs from GitHub search results."""
        page = await self.context.new_page()
        pr_urls = []
        
        try:
            page_num = 1
            while True:
                current_url = f"{search_url}&p={page_num}" if page_num > 1 else search_url
                await page.goto(current_url)
                
                # Wait for search results to load
                await page.wait_for_selector(".search-results", timeout=self.timeout)
                
                # Extract PR links from current page
                pr_links = await page.query_selector_all('a[data-testid="results-list"] .search-title a')
                
                if not pr_links:
                    break
                
                for link in pr_links:
                    href = await link.get_attribute("href")
                    if href and "/pull/" in href:
                        full_url = urljoin("https://github.com", href)
                        pr_urls.append(full_url)
                        
                        if max_prs and len(pr_urls) >= max_prs:
                            return pr_urls[:max_prs]
                
                # Check if there's a next page
                next_button = await page.query_selector('a[rel="next"]')
                if not next_button:
                    break
                    
                page_num += 1
                
        finally:
            await page.close()
        
        return pr_urls
    
    async def _scrape_single_pr(self, pr_url: str) -> GitHubPRData:
        """Scrape comprehensive data from a single PR page."""
        page = await self.context.new_page()
        
        try:
            await page.goto(pr_url)
            await page.wait_for_selector('.gh-header-title', timeout=self.timeout)
            
            # Extract basic PR information
            pr_data = await self._extract_basic_info(page, pr_url)
            
            # Extract advanced metrics
            pr_data.review_metrics = await self._extract_review_metrics(page)
            pr_data.time_metrics = await self._extract_time_metrics(page, pr_data)
            pr_data.file_analysis = await self._extract_file_analysis(page)
            pr_data.engagement_metrics = await self._extract_engagement_metrics(page)
            
            return pr_data
            
        finally:
            await page.close()
    
    async def _extract_basic_info(self, page: Page, pr_url: str) -> GitHubPRData:
        """Extract basic PR information from the page."""
        # Parse URL for repo and PR number
        parsed_url = urlparse(pr_url)
        path_parts = parsed_url.path.strip('/').split('/')
        repository = f"{path_parts[0]}/{path_parts[1]}"
        pr_number = int(path_parts[3])
        
        # Extract title and description
        title = await page.inner_text('.gh-header-title .js-issue-title')
        
        # Try to get description
        description = ""
        try:
            desc_element = await page.query_selector('.comment-body p')
            if desc_element:
                description = await desc_element.inner_text()
        except:
            pass
        
        # Extract author
        author_link = await page.query_selector('.timeline-comment-header .author')
        author = await author_link.inner_text() if author_link else "Unknown"
        
        # Extract state and timestamps
        state_element = await page.query_selector('.State--merged, .State--closed, .State--open')
        state = "open"  # default
        if state_element:
            state_text = await state_element.get_attribute('title')
            if "merged" in state_text.lower():
                state = "merged"
            elif "closed" in state_text.lower():
                state = "closed"
        
        # Extract branch information
        source_branch = ""
        target_branch = ""
        try:
            branch_elements = await page.query_selector_all('.commit-ref')
            if len(branch_elements) >= 2:
                source_branch = await branch_elements[0].inner_text()
                target_branch = await branch_elements[1].inner_text()
        except:
            pass
        
        # Extract code changes (additions/deletions)
        additions = 0
        deletions = 0
        try:
            diff_stats = await page.query_selector('.diffstat')
            if diff_stats:
                stats_text = await diff_stats.inner_text()
                # Parse "+X −Y" format
                matches = re.findall(r'([+−])(\d+)', stats_text)
                for sign, num in matches:
                    if sign == '+':
                        additions = int(num)
                    elif sign == '−':
                        deletions = int(num)
        except:
            pass
        
        # Extract labels
        labels = []
        try:
            label_elements = await page.query_selector_all('.labels .IssueLabel')
            for label_elem in label_elements:
                label_text = await label_elem.inner_text()
                labels.append(label_text)
        except:
            pass
        
        return GitHubPRData(
            repository=repository,
            pr_number=pr_number,
            title=title.strip(),
            description=description.strip(),
            url=pr_url,
            author=author,
            state=state,
            created_at=datetime.now(),  # TODO: Parse actual dates
            source_branch=source_branch,
            target_branch=target_branch,
            additions=additions,
            deletions=deletions,
            labels=labels
        )
    
    async def _extract_review_metrics(self, page: Page) -> ReviewMetrics:
        """Extract review-related metrics."""
        metrics = ReviewMetrics()
        
        try:
            # Count review comments
            review_comments = await page.query_selector_all('.review-comment')
            metrics.review_comments_count = len(review_comments)
            
            # Count approvals and change requests
            review_states = await page.query_selector_all('.review-status')
            for state_elem in review_states:
                state_text = await state_elem.inner_text()
                if "approved" in state_text.lower():
                    metrics.approvals_count += 1
                elif "changes requested" in state_text.lower():
                    metrics.changes_requested_count += 1
            
            # Extract unique reviewers
            reviewer_elements = await page.query_selector_all('.timeline-comment .author')
            reviewers = set()
            for reviewer_elem in reviewer_elements:
                reviewer = await reviewer_elem.inner_text()
                reviewers.add(reviewer)
            
            metrics.unique_reviewers = list(reviewers)
            metrics.total_reviewers = len(reviewers)
            
        except Exception as e:
            logger.debug(f"Error extracting review metrics: {e}")
        
        return metrics
    
    async def _extract_time_metrics(self, page: Page, pr_data: GitHubPRData) -> TimeMetrics:
        """Extract time-based metrics."""
        metrics = TimeMetrics()
        
        # TODO: Implement time parsing from timeline
        # This would involve parsing the timeline for creation, first review, merge times
        
        return metrics
    
    async def _extract_file_analysis(self, page: Page) -> FileAnalysis:
        """Extract file change analysis."""
        analysis = FileAnalysis()
        
        try:
            # Navigate to files changed tab
            files_tab = await page.query_selector('a[data-tab-item="pr-files"]')
            if files_tab:
                await files_tab.click()
                await page.wait_for_selector('.file-info', timeout=5000)
                
                # Count files and analyze types
                file_elements = await page.query_selector_all('.file-info')
                analysis.total_files_changed = len(file_elements)
                
                file_types = {}
                for file_elem in file_elements:
                    file_name = await file_elem.inner_text()
                    if '.' in file_name:
                        ext = file_name.split('.')[-1].lower()
                        file_types[ext] = file_types.get(ext, 0) + 1
                
                analysis.file_types = file_types
                
        except Exception as e:
            logger.debug(f"Error extracting file analysis: {e}")
        
        return analysis
    
    async def _extract_engagement_metrics(self, page: Page) -> EngagementMetrics:
        """Extract engagement and collaboration metrics."""
        metrics = EngagementMetrics()
        
        try:
            # Extract reactions
            reaction_elements = await page.query_selector_all('.reaction-summary-item')
            reactions = {}
            for reaction_elem in reaction_elements:
                reaction_text = await reaction_elem.inner_text()
                # Parse reaction emoji and count
                # This would need more sophisticated parsing
                pass
            
            metrics.reactions = reactions
            
            # Count discussion participants
            comment_authors = await page.query_selector_all('.timeline-comment .author')
            participants = set()
            for author_elem in comment_authors:
                author = await author_elem.inner_text()
                participants.add(author)
            
            metrics.discussion_participants = list(participants)
            
        except Exception as e:
            logger.debug(f"Error extracting engagement metrics: {e}")
        
        return metrics
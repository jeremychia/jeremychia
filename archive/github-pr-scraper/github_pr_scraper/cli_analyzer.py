"""GitHub CLI-based PR analyzer - simpler and more reliable than web scraping."""

import json
import subprocess
from datetime import datetime
from typing import List, Dict, Any, Optional
import logging

from .models import GitHubPRData, ReviewMetrics, TimeMetrics, FileAnalysis, EngagementMetrics

logger = logging.getLogger(__name__)


class GitHubCLIAnalyzer:
    """GitHub CLI-based PR analyzer."""
    
    def __init__(self):
        """Initialize the analyzer."""
        self.check_gh_cli()
    
    def check_gh_cli(self) -> bool:
        """Check if GitHub CLI is installed and authenticated."""
        try:
            # Check if gh CLI is installed
            result = subprocess.run(['gh', '--version'], capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                raise Exception("GitHub CLI not found")
            
            # Check if authenticated
            result = subprocess.run(['gh', 'auth', 'status'], capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                raise Exception("Not authenticated with GitHub CLI")
            
            logger.info("GitHub CLI is installed and authenticated")
            return True
            
        except Exception as e:
            logger.error(f"GitHub CLI check failed: {e}")
            raise Exception(f"GitHub CLI setup issue: {e}")
    
    def get_user_prs(
        self,
        username: str,
        organization: Optional[str] = None,
        repositories: List[str] = None,
        date_from: Optional[datetime] = None,
        date_to: Optional[datetime] = None,
        max_prs: Optional[int] = None,
        include_closed: bool = True,
        include_merged: bool = True
    ) -> List[GitHubPRData]:
        """Get PRs for a user using GitHub CLI."""
        
        all_prs = []
        
        if repositories:
            # Search specific repositories
            repo_list = repositories
        elif organization:
            # Get all repos for organization first
            repo_list = self._get_organization_repos(organization)
        else:
            # Use search across all accessible repos
            return self._search_prs_globally(username, date_from, date_to, max_prs)
        
        # Process repositories in batches
        for repo in repo_list:
            try:
                repo_prs = self._get_prs_for_repo(
                    repo, username, date_from, date_to, 
                    include_closed, include_merged
                )
                all_prs.extend(repo_prs)
                
                if max_prs and len(all_prs) >= max_prs:
                    break
                    
            except Exception as e:
                logger.warning(f"Failed to get PRs for repo {repo}: {e}")
                continue
        
        # Sort by creation date and limit
        all_prs.sort(key=lambda pr: pr.created_at, reverse=True)
        
        if max_prs:
            all_prs = all_prs[:max_prs]
        
        return all_prs
    
    def _get_organization_repos(self, organization: str) -> List[str]:
        """Get list of repositories for an organization."""
        try:
            cmd = [
                'gh', 'repo', 'list', organization,
                '--json', 'name',
                '--limit', '1000'  # GitHub CLI default limit
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            if result.returncode != 0:
                logger.error(f"Failed to get repos for org {organization}: {result.stderr}")
                return []
            
            repos_data = json.loads(result.stdout)
            return [f"{organization}/{repo['name']}" for repo in repos_data]
            
        except Exception as e:
            logger.error(f"Error getting organization repos: {e}")
            return []
    
    def _search_prs_globally(
        self,
        username: str,
        date_from: Optional[datetime] = None,
        date_to: Optional[datetime] = None,
        max_prs: Optional[int] = None
    ) -> List[GitHubPRData]:
        """Search for PRs globally using GitHub search."""
        try:
            # Build search query
            query_parts = [f"author:{username}", "is:pr"]
            
            if date_from:
                query_parts.append(f"created:>={date_from.strftime('%Y-%m-%d')}")
            if date_to:
                query_parts.append(f"created:<={date_to.strftime('%Y-%m-%d')}")
            
            search_query = " ".join(query_parts)
            
            cmd = [
                'gh', 'search', 'prs',
                '--query', search_query,
                '--json', 'number,title,body,createdAt,mergedAt,closedAt,additions,deletions,url,repository',
                '--limit', str(max_prs or 100)
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            if result.returncode != 0:
                logger.error(f"PR search failed: {result.stderr}")
                return []
            
            prs_data = json.loads(result.stdout)
            return self._convert_to_pr_data(prs_data, username)
            
        except Exception as e:
            logger.error(f"Global PR search failed: {e}")
            return []
    
    def _get_prs_for_repo(
        self,
        repo: str,
        username: str,
        date_from: Optional[datetime] = None,
        date_to: Optional[datetime] = None,
        include_closed: bool = True,
        include_merged: bool = True
    ) -> List[GitHubPRData]:
        """Get PRs for a specific repository."""
        try:
            cmd = [
                'gh', 'pr', 'list',
                '--repo', repo,
                '--author', username,
                '--json', 'number,title,body,createdAt,updatedAt,mergedAt,closedAt,additions,deletions,url,headRefName,baseRefName,labels,state',
                '--limit', '1000'
            ]
            
            # Add state filters
            states = []
            if include_closed:
                states.append('closed')
            if include_merged:
                states.append('merged')
            states.append('open')
            
            for state in states:
                state_cmd = cmd + ['--state', state]
                result = subprocess.run(state_cmd, capture_output=True, text=True, timeout=30)
                
                if result.returncode != 0:
                    logger.warning(f"Failed to get {state} PRs for {repo}: {result.stderr}")
                    continue
                
                prs_data = json.loads(result.stdout)
                repo_prs = self._convert_to_pr_data(prs_data, username, repo)
                
                # Filter by date if specified
                if date_from or date_to:
                    repo_prs = self._filter_prs_by_date(repo_prs, date_from, date_to)
                
                return repo_prs
            
            return []
            
        except Exception as e:
            logger.error(f"Error getting PRs for repo {repo}: {e}")
            return []
    
    def _convert_to_pr_data(self, prs_data: List[Dict], username: str, repo: str = None) -> List[GitHubPRData]:
        """Convert GitHub CLI JSON data to our PR data model."""
        pr_list = []
        
        for pr_json in prs_data:
            try:
                # Handle repository field
                repository = repo or pr_json.get('repository', {}).get('nameWithOwner', 'unknown/unknown')
                
                # Parse timestamps
                created_at = datetime.fromisoformat(pr_json['createdAt'].replace('Z', '+00:00'))
                merged_at = None
                closed_at = None
                updated_at = None
                
                if pr_json.get('mergedAt'):
                    merged_at = datetime.fromisoformat(pr_json['mergedAt'].replace('Z', '+00:00'))
                if pr_json.get('closedAt'):
                    closed_at = datetime.fromisoformat(pr_json['closedAt'].replace('Z', '+00:00'))
                if pr_json.get('updatedAt'):
                    updated_at = datetime.fromisoformat(pr_json['updatedAt'].replace('Z', '+00:00'))
                
                # Extract labels
                labels = []
                if pr_json.get('labels'):
                    labels = [label.get('name', '') for label in pr_json['labels']]
                
                # Determine state
                state = pr_json.get('state', 'open').lower()
                
                # Create PR data object
                pr_data = GitHubPRData(
                    repository=repository,
                    pr_number=pr_json['number'],
                    title=pr_json.get('title', ''),
                    description=pr_json.get('body', ''),
                    url=pr_json.get('url', ''),
                    author=username,
                    state=state,
                    created_at=created_at,
                    updated_at=updated_at,
                    merged_at=merged_at,
                    closed_at=closed_at,
                    source_branch=pr_json.get('headRefName', ''),
                    target_branch=pr_json.get('baseRefName', ''),
                    additions=pr_json.get('additions', 0),
                    deletions=pr_json.get('deletions', 0),
                    labels=labels,
                    
                    # Initialize with basic metrics (could be enhanced later)
                    review_metrics=ReviewMetrics(),
                    time_metrics=self._calculate_time_metrics(created_at, merged_at, closed_at),
                    file_analysis=FileAnalysis(),
                    engagement_metrics=EngagementMetrics()
                )
                
                pr_list.append(pr_data)
                
            except Exception as e:
                logger.warning(f"Failed to parse PR data: {e}")
                continue
        
        return pr_list
    
    def _calculate_time_metrics(
        self, 
        created_at: datetime, 
        merged_at: Optional[datetime], 
        closed_at: Optional[datetime]
    ) -> TimeMetrics:
        """Calculate basic time metrics."""
        metrics = TimeMetrics()
        
        end_time = merged_at or closed_at
        if end_time:
            time_diff = end_time - created_at
            metrics.time_open_hours = time_diff.total_seconds() / 3600
            
            if merged_at:
                metrics.time_to_merge_hours = (merged_at - created_at).total_seconds() / 3600
        
        return metrics
    
    def _filter_prs_by_date(
        self, 
        prs: List[GitHubPRData], 
        date_from: Optional[datetime], 
        date_to: Optional[datetime]
    ) -> List[GitHubPRData]:
        """Filter PRs by date range."""
        filtered_prs = []
        
        for pr in prs:
            if date_from and pr.created_at < date_from:
                continue
            if date_to and pr.created_at > date_to:
                continue
            filtered_prs.append(pr)
        
        return filtered_prs
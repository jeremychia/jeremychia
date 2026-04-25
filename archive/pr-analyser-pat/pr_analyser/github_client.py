"""GitHub API client for fetching PR and commit data."""

import logging
import time
from datetime import datetime
from typing import List, Dict, Any, Optional
from github import Github, GithubException
from github.Repository import Repository
from github.PullRequest import PullRequest
from github.Commit import Commit

from .models import PRData, CommitData

logger = logging.getLogger(__name__)


class GitHubClient:
    """GitHub API client for fetching user data."""

    def __init__(self, token: str, requests_per_hour: int = 4000):
        """Initialize GitHub client."""
        self.github = Github(token, per_page=100)
        self.requests_per_hour = requests_per_hour
        self.requests_made = 0
        self.last_reset = time.time()

    def _handle_rate_limit(self):
        """Handle GitHub API rate limiting."""
        current_time = time.time()
        
        # Reset counter every hour
        if current_time - self.last_reset >= 3600:
            self.requests_made = 0
            self.last_reset = current_time
        
        # Check if we're approaching the limit
        if self.requests_made >= self.requests_per_hour:
            sleep_time = 3600 - (current_time - self.last_reset)
            if sleep_time > 0:
                logger.warning(f"Rate limit approaching, sleeping for {sleep_time:.1f} seconds")
                time.sleep(sleep_time)
                self.requests_made = 0
                self.last_reset = time.time()
        
        self.requests_made += 1

    def get_organization_repositories(self, org_name: str, filters: Optional[Dict[str, List[str]]] = None) -> List[Repository]:
        """Get all repositories in an organization."""
        self._handle_rate_limit()
        
        try:
            org = self.github.get_organization(org_name)
            repositories = list(org.get_repos())
            
            if filters:
                # Apply repository filters
                if filters.get("repositories"):
                    repositories = [repo for repo in repositories if repo.name in filters["repositories"]]
                
                if filters.get("exclude_repositories"):
                    repositories = [repo for repo in repositories if repo.name not in filters["exclude_repositories"]]
            
            logger.info(f"Found {len(repositories)} repositories in organization {org_name}")
            return repositories
        
        except GithubException as e:
            logger.error(f"Error fetching repositories for organization {org_name}: {e}")
            return []

    def get_user_pull_requests(
        self, 
        repositories: List[Repository], 
        username: str, 
        date_from: Optional[datetime] = None,
        date_to: Optional[datetime] = None,
        filters: Optional[Dict[str, List[str]]] = None
    ) -> List[PRData]:
        """Get all pull requests authored by a user across repositories."""
        all_prs = []
        
        for repo in repositories:
            logger.info(f"Fetching PRs from repository: {repo.name}")
            self._handle_rate_limit()
            
            try:
                # Get all PRs for the repository
                prs = repo.get_pulls(state='all', sort='created', direction='desc')
                
                for pr in prs:
                    self._handle_rate_limit()
                    
                    # Filter by author
                    if pr.user.login != username:
                        continue
                    
                    # Filter by date range
                    if date_from and pr.created_at < date_from:
                        continue
                    if date_to and pr.created_at > date_to:
                        continue
                    
                    # Apply PR status filters
                    if filters and filters.get("pr_status"):
                        pr_status = "merged" if pr.merged else pr.state
                        if pr_status not in filters["pr_status"]:
                            continue
                    
                    # Apply branch filters
                    if filters and filters.get("branches"):
                        if pr.head.ref not in filters["branches"]:
                            continue
                    
                    # Get review information
                    reviews = list(pr.get_reviews())
                    reviewers = list(set([review.user.login for review in reviews if review.user]))
                    
                    # Get comments count
                    comments_count = pr.comments + pr.review_comments
                    
                    pr_data = PRData(
                        id=pr.id,
                        number=pr.number,
                        title=pr.title,
                        description=pr.body or "",
                        repository=repo.name,
                        author=pr.user.login,
                        state=pr.state,
                        merged=pr.merged,
                        created_at=pr.created_at,
                        updated_at=pr.updated_at,
                        merged_at=pr.merged_at,
                        closed_at=pr.closed_at,
                        source_branch=pr.head.ref,
                        target_branch=pr.base.ref,
                        additions=pr.additions,
                        deletions=pr.deletions,
                        changed_files=pr.changed_files,
                        comments_count=comments_count,
                        reviewers=reviewers,
                        labels=[label.name for label in pr.labels]
                    )
                    
                    all_prs.append(pr_data)
                    
            except GithubException as e:
                logger.error(f"Error fetching PRs from repository {repo.name}: {e}")
                continue
        
        logger.info(f"Found {len(all_prs)} pull requests for user {username}")
        return all_prs

    def get_user_commits(
        self, 
        repositories: List[Repository], 
        username: str,
        date_from: Optional[datetime] = None,
        date_to: Optional[datetime] = None,
        filters: Optional[Dict[str, List[str]]] = None
    ) -> List[CommitData]:
        """Get all commits authored by a user across repositories."""
        all_commits = []
        
        for repo in repositories:
            logger.info(f"Fetching commits from repository: {repo.name}")
            self._handle_rate_limit()
            
            try:
                # Get commits with author filter
                commits = repo.get_commits(author=username, since=date_from, until=date_to)
                
                for commit in commits:
                    self._handle_rate_limit()
                    
                    # Apply branch filters if specified
                    if filters and filters.get("branches"):
                        # This is a simplified approach - in practice, determining which branches
                        # a commit belongs to requires additional API calls
                        pass
                    
                    # Get commit statistics
                    commit_details = repo.get_commit(commit.sha)
                    
                    commit_data = CommitData(
                        sha=commit.sha,
                        message=commit.commit.message,
                        repository=repo.name,
                        author=commit.commit.author.name,
                        author_email=commit.commit.author.email,
                        authored_date=commit.commit.author.date,
                        committed_date=commit.commit.committer.date,
                        additions=commit_details.stats.additions,
                        deletions=commit_details.stats.deletions,
                        total_changes=commit_details.stats.total,
                        files_changed=[file.filename for file in commit_details.files]
                    )
                    
                    all_commits.append(commit_data)
                    
            except GithubException as e:
                logger.error(f"Error fetching commits from repository {repo.name}: {e}")
                continue
        
        logger.info(f"Found {len(all_commits)} commits for user {username}")
        return all_commits
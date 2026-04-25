"""Data models for comprehensive GitHub PR analysis."""

from datetime import datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class ReviewMetrics(BaseModel):
    """Review-related metrics for a PR."""
    total_reviewers: int = 0
    unique_reviewers: List[str] = []
    review_comments_count: int = 0
    approvals_count: int = 0
    changes_requested_count: int = 0
    review_cycles: int = 0
    time_to_first_review_hours: Optional[float] = None
    average_review_response_time_hours: Optional[float] = None


class TimeMetrics(BaseModel):
    """Time-based metrics for PR lifecycle."""
    time_open_hours: Optional[float] = None
    time_to_merge_hours: Optional[float] = None
    time_in_draft_hours: Optional[float] = None
    time_from_last_commit_to_merge_hours: Optional[float] = None
    business_days_open: Optional[int] = None


class FileAnalysis(BaseModel):
    """Analysis of changed files and code."""
    total_files_changed: int = 0
    file_types: Dict[str, int] = {}  # Extension -> count
    programming_languages: Dict[str, int] = {}  # Language -> line count  
    largest_file_changes: List[Dict[str, Any]] = []  # Top files by changes
    binary_files_count: int = 0
    test_files_count: int = 0
    documentation_files_count: int = 0


class EngagementMetrics(BaseModel):
    """Engagement and collaboration metrics."""
    reactions: Dict[str, int] = {}  # Reaction type -> count
    discussion_participants: List[str] = []
    total_discussion_comments: int = 0
    mentioned_users: List[str] = []
    cross_references: List[str] = []  # Other PRs/issues referenced


class GitHubPRData(BaseModel):
    """Comprehensive GitHub Pull Request data model."""
    
    # Basic PR Information
    repository: str
    pr_number: int
    title: str
    description: str = ""
    url: str
    
    # Author & State
    author: str
    author_avatar_url: str = ""
    state: str  # open, closed, merged
    is_draft: bool = False
    
    # Timestamps
    created_at: datetime
    updated_at: Optional[datetime] = None
    merged_at: Optional[datetime] = None
    closed_at: Optional[datetime] = None
    
    # Branch Information
    source_branch: str
    target_branch: str
    source_repository: str = ""  # For forks
    
    # Code Changes
    additions: int = 0
    deletions: int = 0
    commits_count: int = 0
    
    # Labels & Classification
    labels: List[str] = []
    milestone: Optional[str] = None
    linked_issues: List[str] = []
    
    # Advanced Metrics
    review_metrics: ReviewMetrics = ReviewMetrics()
    time_metrics: TimeMetrics = TimeMetrics()
    file_analysis: FileAnalysis = FileAnalysis()
    engagement_metrics: EngagementMetrics = EngagementMetrics()
    
    # Additional Context
    is_security_fix: bool = False
    is_breaking_change: bool = False
    deployment_info: Dict[str, Any] = {}
    ci_status: Dict[str, str] = {}  # CI check -> status
    
    @property
    def net_lines_changed(self) -> int:
        """Net lines changed (additions - deletions)."""
        return self.additions - self.deletions
    
    @property
    def total_lines_changed(self) -> int:
        """Total lines changed (additions + deletions)."""
        return self.additions + self.deletions
    
    @property
    def status(self) -> str:
        """Normalized status."""
        if self.state == "closed" and self.merged_at:
            return "merged"
        elif self.state == "closed":
            return "closed"
        return "open"
    
    @property
    def complexity_score(self) -> float:
        """Simple complexity score based on various factors."""
        score = 0.0
        
        # File changes impact
        score += min(self.file_analysis.total_files_changed * 0.5, 10)
        
        # Line changes impact  
        score += min(self.total_lines_changed * 0.01, 20)
        
        # Review complexity
        score += min(self.review_metrics.review_cycles * 2, 10)
        
        # Time complexity
        if self.time_metrics.time_open_hours:
            score += min(self.time_metrics.time_open_hours * 0.1, 15)
        
        return round(score, 2)


class AnalysisConfig(BaseModel):
    """Configuration for PR analysis."""
    username: str
    organization: Optional[str] = None
    repositories: List[str] = []
    exclude_repositories: List[str] = []
    date_from: Optional[datetime] = None
    date_to: Optional[datetime] = None
    include_drafts: bool = True
    include_closed: bool = True
    max_prs: Optional[int] = None


class ScrapingResult(BaseModel):
    """Result of PR scraping operation."""
    prs: List[GitHubPRData]
    total_processed: int
    successful_scrapes: int
    failed_scrapes: int
    errors: List[str] = []
    processing_time_seconds: float
    
    @property
    def success_rate(self) -> float:
        """Success rate of scraping operation."""
        if self.total_processed == 0:
            return 0.0
        return (self.successful_scrapes / self.total_processed) * 100
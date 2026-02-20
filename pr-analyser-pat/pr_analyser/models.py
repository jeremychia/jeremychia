"""Data models for PR and commit analysis."""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class PRData(BaseModel):
    """Pull Request data model."""
    id: int
    number: int
    title: str
    description: str
    repository: str
    author: str
    state: str  # open, closed
    merged: bool
    created_at: datetime
    updated_at: datetime
    merged_at: Optional[datetime] = None
    closed_at: Optional[datetime] = None
    source_branch: str
    target_branch: str
    additions: int
    deletions: int
    changed_files: int
    comments_count: int
    reviewers: List[str]
    labels: List[str]

    @property
    def total_changes(self) -> int:
        """Total lines changed (additions + deletions)."""
        return self.additions + self.deletions

    @property
    def status(self) -> str:
        """Normalized status (open, merged, closed)."""
        if self.merged:
            return "merged"
        return self.state


class CommitData(BaseModel):
    """Commit data model."""
    sha: str
    message: str
    repository: str
    author: str
    author_email: str
    authored_date: datetime
    committed_date: datetime
    additions: int
    deletions: int
    total_changes: int
    files_changed: List[str]

    @property
    def short_sha(self) -> str:
        """Short SHA (first 7 characters)."""
        return self.sha[:7]

    @property
    def short_message(self) -> str:
        """First line of commit message."""
        return self.message.split('\n')[0]


class AnalysisResult(BaseModel):
    """Analysis result model."""
    user: str
    organization: str
    analysis_date: datetime
    date_range: dict
    total_prs: int
    total_commits: int
    repositories_contributed: int
    pull_requests: List[PRData]
    commits: List[CommitData]

    @property
    def merged_prs(self) -> int:
        """Number of merged PRs."""
        return sum(1 for pr in self.pull_requests if pr.merged)

    @property
    def open_prs(self) -> int:
        """Number of open PRs."""
        return sum(1 for pr in self.pull_requests if pr.state == "open")

    @property
    def closed_prs(self) -> int:
        """Number of closed (but not merged) PRs."""
        return sum(1 for pr in self.pull_requests if pr.state == "closed" and not pr.merged)

    @property
    def total_lines_added(self) -> int:
        """Total lines added across all PRs."""
        return sum(pr.additions for pr in self.pull_requests)

    @property
    def total_lines_deleted(self) -> int:
        """Total lines deleted across all PRs."""
        return sum(pr.deletions for pr in self.pull_requests)

    @property
    def total_files_changed(self) -> int:
        """Total files changed across all PRs."""
        return sum(pr.changed_files for pr in self.pull_requests)

    @property
    def average_pr_size(self) -> float:
        """Average PR size in lines changed."""
        if not self.pull_requests:
            return 0.0
        return sum(pr.total_changes for pr in self.pull_requests) / len(self.pull_requests)


class ContributionMetrics(BaseModel):
    """Contribution metrics model."""
    total_contributions: int
    prs_created: int
    prs_merged: int
    prs_closed: int
    commits_made: int
    lines_added: int
    lines_deleted: int
    files_modified: int
    repositories_touched: int
    average_pr_size: float
    merge_rate: float
    most_active_repository: str
    contribution_streak: int
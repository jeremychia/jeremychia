"""Data analysis and metrics calculation."""

import logging
from collections import defaultdict, Counter
from datetime import datetime, timedelta
from typing import Dict, List, Any, Tuple
import pandas as pd

from .models import AnalysisResult, PRData, CommitData, ContributionMetrics

logger = logging.getLogger(__name__)


class DataAnalyzer:
    """Analyze PR and commit data to generate insights."""

    def __init__(self, result: AnalysisResult):
        """Initialize analyzer with analysis result."""
        self.result = result
        self.pr_df = self._create_pr_dataframe()
        self.commit_df = self._create_commit_dataframe()

    def _create_pr_dataframe(self) -> pd.DataFrame:
        """Create pandas DataFrame from PR data."""
        if not self.result.pull_requests:
            return pd.DataFrame()
        
        data = []
        for pr in self.result.pull_requests:
            data.append({
                'id': pr.id,
                'number': pr.number,
                'title': pr.title,
                'repository': pr.repository,
                'status': pr.status,
                'created_at': pr.created_at,
                'merged_at': pr.merged_at,
                'closed_at': pr.closed_at,
                'additions': pr.additions,
                'deletions': pr.deletions,
                'total_changes': pr.total_changes,
                'changed_files': pr.changed_files,
                'comments_count': pr.comments_count,
                'reviewers_count': len(pr.reviewers),
                'labels_count': len(pr.labels)
            })
        
        df = pd.DataFrame(data)
        df['created_at'] = pd.to_datetime(df['created_at'])
        df['merged_at'] = pd.to_datetime(df['merged_at'])
        df['closed_at'] = pd.to_datetime(df['closed_at'])
        
        return df

    def _create_commit_dataframe(self) -> pd.DataFrame:
        """Create pandas DataFrame from commit data."""
        if not self.result.commits:
            return pd.DataFrame()
        
        data = []
        for commit in self.result.commits:
            data.append({
                'sha': commit.sha,
                'short_sha': commit.short_sha,
                'message': commit.short_message,
                'repository': commit.repository,
                'authored_date': commit.authored_date,
                'committed_date': commit.committed_date,
                'additions': commit.additions,
                'deletions': commit.deletions,
                'total_changes': commit.total_changes,
                'files_changed_count': len(commit.files_changed)
            })
        
        df = pd.DataFrame(data)
        df['authored_date'] = pd.to_datetime(df['authored_date'])
        df['committed_date'] = pd.to_datetime(df['committed_date'])
        
        return df

    def calculate_contribution_metrics(self) -> ContributionMetrics:
        """Calculate comprehensive contribution metrics."""
        if self.pr_df.empty and self.commit_df.empty:
            return ContributionMetrics(
                total_contributions=0,
                prs_created=0,
                prs_merged=0,
                prs_closed=0,
                commits_made=0,
                lines_added=0,
                lines_deleted=0,
                files_modified=0,
                repositories_touched=0,
                average_pr_size=0.0,
                merge_rate=0.0,
                most_active_repository="",
                contribution_streak=0
            )

        # PR metrics
        prs_created = len(self.pr_df) if not self.pr_df.empty else 0
        prs_merged = len(self.pr_df[self.pr_df['status'] == 'merged']) if not self.pr_df.empty else 0
        prs_closed = len(self.pr_df[self.pr_df['status'] == 'closed']) if not self.pr_df.empty else 0
        
        # Commit metrics
        commits_made = len(self.commit_df) if not self.commit_df.empty else 0
        
        # Lines and files metrics
        pr_lines_added = self.pr_df['additions'].sum() if not self.pr_df.empty else 0
        pr_lines_deleted = self.pr_df['deletions'].sum() if not self.pr_df.empty else 0
        pr_files_modified = self.pr_df['changed_files'].sum() if not self.pr_df.empty else 0
        
        commit_lines_added = self.commit_df['additions'].sum() if not self.commit_df.empty else 0
        commit_lines_deleted = self.commit_df['deletions'].sum() if not self.commit_df.empty else 0
        commit_files_modified = self.commit_df['files_changed_count'].sum() if not self.commit_df.empty else 0
        
        lines_added = max(pr_lines_added, commit_lines_added)  # Use the higher value
        lines_deleted = max(pr_lines_deleted, commit_lines_deleted)
        files_modified = max(pr_files_modified, commit_files_modified)
        
        # Repository metrics
        pr_repos = set(self.pr_df['repository']) if not self.pr_df.empty else set()
        commit_repos = set(self.commit_df['repository']) if not self.commit_df.empty else set()
        repositories_touched = len(pr_repos.union(commit_repos))
        
        # Calculate averages and rates
        average_pr_size = self.pr_df['total_changes'].mean() if not self.pr_df.empty else 0.0
        merge_rate = (prs_merged / prs_created * 100) if prs_created > 0 else 0.0
        
        # Most active repository
        all_repos = list(pr_repos) + list(commit_repos)
        repo_counter = Counter(all_repos)
        most_active_repository = repo_counter.most_common(1)[0][0] if repo_counter else ""
        
        # Contribution streak (simplified - consecutive days with commits)
        contribution_streak = self._calculate_contribution_streak()
        
        return ContributionMetrics(
            total_contributions=prs_created + commits_made,
            prs_created=prs_created,
            prs_merged=prs_merged,
            prs_closed=prs_closed,
            commits_made=commits_made,
            lines_added=int(lines_added),
            lines_deleted=int(lines_deleted),
            files_modified=int(files_modified),
            repositories_touched=repositories_touched,
            average_pr_size=round(average_pr_size, 2),
            merge_rate=round(merge_rate, 2),
            most_active_repository=most_active_repository,
            contribution_streak=contribution_streak
        )

    def _calculate_contribution_streak(self) -> int:
        """Calculate consecutive days with contributions."""
        if self.commit_df.empty:
            return 0
        
        # Get unique dates of commits
        commit_dates = self.commit_df['authored_date'].dt.date.unique()
        commit_dates = sorted(commit_dates, reverse=True)
        
        if not commit_dates:
            return 0
        
        streak = 0
        current_date = datetime.now().date()
        
        for commit_date in commit_dates:
            if current_date - commit_date == timedelta(days=streak):
                streak += 1
                current_date = commit_date
            else:
                break
        
        return streak

    def get_time_series_data(self, period: str = 'D') -> Dict[str, Any]:
        """Get time series data for contributions."""
        if self.pr_df.empty and self.commit_df.empty:
            return {}
        
        # Combine PR and commit dates
        pr_dates = self.pr_df['created_at'] if not self.pr_df.empty else pd.Series([], dtype='datetime64[ns]')
        commit_dates = self.commit_df['authored_date'] if not self.commit_df.empty else pd.Series([], dtype='datetime64[ns]')
        
        # Group by specified period (use pandas frequency strings)
        pr_by_period = pr_dates.dt.to_period(period).value_counts().sort_index()
        commit_by_period = commit_dates.dt.to_period(period).value_counts().sort_index()
        
        # Create combined timeline
        all_periods = pd.period_range(
            start=min(pr_by_period.index[0] if len(pr_by_period) > 0 else commit_by_period.index[0],
                     commit_by_period.index[0] if len(commit_by_period) > 0 else pr_by_period.index[0]),
            end=max(pr_by_period.index[-1] if len(pr_by_period) > 0 else commit_by_period.index[-1],
                   commit_by_period.index[-1] if len(commit_by_period) > 0 else pr_by_period.index[-1]),
            freq=period
        )
        
        timeline_data = []
        for period_val in all_periods:
            timeline_data.append({
                'period': str(period_val),
                'prs': pr_by_period.get(period_val, 0),
                'commits': commit_by_period.get(period_val, 0),
                'total': pr_by_period.get(period_val, 0) + commit_by_period.get(period_val, 0)
            })
        
        return {
            'timeline': timeline_data,
            'total_periods': len(all_periods),
            'avg_prs_per_period': pr_by_period.mean() if len(pr_by_period) > 0 else 0,
            'avg_commits_per_period': commit_by_period.mean() if len(commit_by_period) > 0 else 0
        }

    def get_repository_breakdown(self) -> Dict[str, Any]:
        """Get contribution breakdown by repository."""
        if self.pr_df.empty and self.commit_df.empty:
            return {}
        
        repo_stats = defaultdict(lambda: {
            'prs': 0, 'commits': 0, 'lines_added': 0, 'lines_deleted': 0, 'files_changed': 0
        })
        
        # PR stats by repository
        if not self.pr_df.empty:
            pr_by_repo = self.pr_df.groupby('repository').agg({
                'id': 'count',
                'additions': 'sum',
                'deletions': 'sum',
                'changed_files': 'sum'
            }).to_dict('index')
            
            for repo, stats in pr_by_repo.items():
                repo_stats[repo]['prs'] = stats['id']
                repo_stats[repo]['lines_added'] = stats['additions']
                repo_stats[repo]['lines_deleted'] = stats['deletions']
                repo_stats[repo]['files_changed'] = stats['changed_files']
        
        # Commit stats by repository
        if not self.commit_df.empty:
            commit_by_repo = self.commit_df.groupby('repository').agg({
                'sha': 'count',
                'additions': 'sum',
                'deletions': 'sum',
                'files_changed_count': 'sum'
            }).to_dict('index')
            
            for repo, stats in commit_by_repo.items():
                repo_stats[repo]['commits'] = stats['sha']
                # Use the higher value between PR and commit stats
                repo_stats[repo]['lines_added'] = max(repo_stats[repo]['lines_added'], stats['additions'])
                repo_stats[repo]['lines_deleted'] = max(repo_stats[repo]['lines_deleted'], stats['deletions'])
                repo_stats[repo]['files_changed'] = max(repo_stats[repo]['files_changed'], stats['files_changed_count'])
        
        # Sort by total contributions
        sorted_repos = sorted(
            repo_stats.items(),
            key=lambda x: x[1]['prs'] + x[1]['commits'],
            reverse=True
        )
        
        return {
            'repositories': dict(sorted_repos),
            'total_repositories': len(repo_stats),
            'most_active': sorted_repos[0][0] if sorted_repos else None
        }

    def get_collaboration_insights(self) -> Dict[str, Any]:
        """Get insights about collaboration patterns."""
        if self.pr_df.empty:
            return {}
        
        # Most frequent reviewers
        all_reviewers = []
        for pr in self.result.pull_requests:
            all_reviewers.extend(pr.reviewers)
        
        reviewer_counts = Counter(all_reviewers)
        
        # PR review statistics
        prs_with_reviews = len([pr for pr in self.result.pull_requests if pr.reviewers])
        avg_reviewers_per_pr = sum(len(pr.reviewers) for pr in self.result.pull_requests) / len(self.result.pull_requests)
        avg_comments_per_pr = self.pr_df['comments_count'].mean()
        
        return {
            'top_reviewers': dict(reviewer_counts.most_common(10)),
            'prs_with_reviews': prs_with_reviews,
            'review_rate': (prs_with_reviews / len(self.result.pull_requests) * 100),
            'avg_reviewers_per_pr': round(avg_reviewers_per_pr, 2),
            'avg_comments_per_pr': round(avg_comments_per_pr, 2),
            'total_unique_reviewers': len(reviewer_counts)
        }
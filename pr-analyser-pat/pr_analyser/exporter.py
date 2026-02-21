"""Export functionality for analysis results."""

import csv
import json
import os
import logging
from datetime import datetime
from typing import Dict, Any, List

from .models import AnalysisResult
from .analyzer import DataAnalyzer

logger = logging.getLogger(__name__)


class Exporter:
    """Export analysis results to various formats."""

    def __init__(self, result: AnalysisResult, output_dir: str = "./reports"):
        """Initialize exporter."""
        self.result = result
        self.analyzer = DataAnalyzer(result)
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def export_to_csv(self) -> Dict[str, str]:
        """Export data to CSV files."""
        created_files = {}
        
        # Export PRs to CSV
        if self.result.pull_requests:
            pr_filename = os.path.join(self.output_dir, f"pull_requests_{self.result.user}.csv")
            
            with open(pr_filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = [
                    'id', 'number', 'title', 'repository', 'status', 'created_at',
                    'merged_at', 'closed_at', 'source_branch', 'target_branch',
                    'additions', 'deletions', 'total_changes', 'changed_files',
                    'comments_count', 'reviewers', 'labels'
                ]
                
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for pr in self.result.pull_requests:
                    writer.writerow({
                        'id': pr.id,
                        'number': pr.number,
                        'title': pr.title,
                        'repository': pr.repository,
                        'status': pr.status,
                        'created_at': pr.created_at.isoformat(),
                        'merged_at': pr.merged_at.isoformat() if pr.merged_at else '',
                        'closed_at': pr.closed_at.isoformat() if pr.closed_at else '',
                        'source_branch': pr.source_branch,
                        'target_branch': pr.target_branch,
                        'additions': pr.additions,
                        'deletions': pr.deletions,
                        'total_changes': pr.total_changes,
                        'changed_files': pr.changed_files,
                        'comments_count': pr.comments_count,
                        'reviewers': '; '.join(pr.reviewers),
                        'labels': '; '.join(pr.labels)
                    })
            
            created_files['pull_requests'] = pr_filename
            logger.info(f"PRs exported to {pr_filename}")
        
        # Export commits to CSV
        if self.result.commits:
            commit_filename = os.path.join(self.output_dir, f"commits_{self.result.user}.csv")
            
            with open(commit_filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = [
                    'sha', 'short_sha', 'message', 'repository', 'author',
                    'authored_date', 'committed_date', 'additions', 'deletions',
                    'total_changes', 'files_changed'
                ]
                
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for commit in self.result.commits:
                    writer.writerow({
                        'sha': commit.sha,
                        'short_sha': commit.short_sha,
                        'message': commit.short_message,
                        'repository': commit.repository,
                        'author': commit.author,
                        'authored_date': commit.authored_date.isoformat(),
                        'committed_date': commit.committed_date.isoformat(),
                        'additions': commit.additions,
                        'deletions': commit.deletions,
                        'total_changes': commit.total_changes,
                        'files_changed': '; '.join(commit.files_changed)
                    })
            
            created_files['commits'] = commit_filename
            logger.info(f"Commits exported to {commit_filename}")
        
        return created_files

    def export_to_json(self) -> str:
        """Export complete analysis result to JSON."""
        filename = os.path.join(self.output_dir, f"analysis_{self.result.user}.json")
        
        # Convert to JSON-serializable format
        data = {
            'metadata': {
                'user': self.result.user,
                'organization': self.result.organization,
                'analysis_date': self.result.analysis_date.isoformat(),
                'date_range': self.result.date_range,
                'summary': {
                    'total_prs': self.result.total_prs,
                    'total_commits': self.result.total_commits,
                    'repositories_contributed': self.result.repositories_contributed,
                    'merged_prs': self.result.merged_prs,
                    'open_prs': self.result.open_prs,
                    'closed_prs': self.result.closed_prs,
                    'total_lines_added': self.result.total_lines_added,
                    'total_lines_deleted': self.result.total_lines_deleted,
                    'average_pr_size': self.result.average_pr_size
                }
            },
            'pull_requests': [
                {
                    'id': pr.id,
                    'number': pr.number,
                    'title': pr.title,
                    'repository': pr.repository,
                    'status': pr.status,
                    'created_at': pr.created_at.isoformat(),
                    'merged_at': pr.merged_at.isoformat() if pr.merged_at else None,
                    'closed_at': pr.closed_at.isoformat() if pr.closed_at else None,
                    'source_branch': pr.source_branch,
                    'target_branch': pr.target_branch,
                    'additions': pr.additions,
                    'deletions': pr.deletions,
                    'changed_files': pr.changed_files,
                    'reviewers': pr.reviewers,
                    'labels': pr.labels
                }
                for pr in self.result.pull_requests
            ],
            'commits': [
                {
                    'sha': commit.sha,
                    'message': commit.short_message,
                    'repository': commit.repository,
                    'authored_date': commit.authored_date.isoformat(),
                    'additions': commit.additions,
                    'deletions': commit.deletions,
                    'files_changed': commit.files_changed
                }
                for commit in self.result.commits
            ]
        }
        
        with open(filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=2, ensure_ascii=False)
        
        logger.info(f"Analysis exported to JSON: {filename}")
        return filename

    def export_to_markdown(self) -> str:
        """Export analysis summary to Markdown report."""
        filename = os.path.join(self.output_dir, f"report_{self.result.user}.md")
        
        # Get analysis data
        metrics = self.analyzer.calculate_contribution_metrics()
        time_series = self.analyzer.get_time_series_data('M')  # Monthly data
        repo_breakdown = self.analyzer.get_repository_breakdown()
        collaboration = self.analyzer.get_collaboration_insights()
        
        # Generate markdown content
        content = f"""# GitHub Contribution Report

**User:** {self.result.user}  
**Organization:** {self.result.organization}  
**Analysis Date:** {self.result.analysis_date.strftime('%Y-%m-%d %H:%M:%S')}  
**Date Range:** {self.result.date_range.get('from', 'All time')} to {self.result.date_range.get('to', 'All time')}

## Summary

| Metric | Value |
|--------|-------|
| Total Contributions | {metrics.total_contributions} |
| Pull Requests Created | {metrics.prs_created} |
| Pull Requests Merged | {metrics.prs_merged} |
| Pull Requests Closed | {metrics.prs_closed} |
| Commits Made | {metrics.commits_made} |
| Lines Added | {metrics.lines_added:,} |
| Lines Deleted | {metrics.lines_deleted:,} |
| Files Modified | {metrics.files_modified:,} |
| Repositories Touched | {metrics.repositories_touched} |
| Average PR Size | {metrics.average_pr_size:.1f} lines |
| Merge Rate | {metrics.merge_rate:.1f}% |
| Most Active Repository | {metrics.most_active_repository} |

## Repository Breakdown

"""
        
        if repo_breakdown and repo_breakdown['repositories']:
            content += "| Repository | PRs | Commits | Lines Added | Lines Deleted |\n"
            content += "|------------|-----|---------|-------------|---------------|\n"
            
            for repo, stats in list(repo_breakdown['repositories'].items())[:10]:
                content += f"| {repo} | {stats['prs']} | {stats['commits']} | {stats['lines_added']:,} | {stats['lines_deleted']:,} |\n"
        
        content += "\n## Collaboration Insights\n\n"
        
        if collaboration:
            content += f"- **PRs with Reviews:** {collaboration.get('prs_with_reviews', 0)}\n"
            content += f"- **Review Rate:** {collaboration.get('review_rate', 0):.1f}%\n"
            content += f"- **Average Reviewers per PR:** {collaboration.get('avg_reviewers_per_pr', 0):.1f}\n"
            content += f"- **Average Comments per PR:** {collaboration.get('avg_comments_per_pr', 0):.1f}\n"
            content += f"- **Total Unique Reviewers:** {collaboration.get('total_unique_reviewers', 0)}\n"
            
            top_reviewers = collaboration.get('top_reviewers', {})
            if top_reviewers:
                content += "\n### Top Reviewers\n\n"
                for reviewer, count in list(top_reviewers.items())[:5]:
                    content += f"- **{reviewer}:** {count} reviews\n"
        
        # Recent activity
        content += "\n## Recent Pull Requests\n\n"
        recent_prs = sorted(self.result.pull_requests, key=lambda x: x.created_at, reverse=True)[:10]
        
        for pr in recent_prs:
            content += f"- **#{pr.number}** [{pr.title}] - {pr.repository} ({pr.status})\n"
            content += f"  - Created: {pr.created_at.strftime('%Y-%m-%d')}\n"
            content += f"  - Changes: +{pr.additions} -{pr.deletions} lines\n\n"
        
        content += f"\n---\n*Report generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*"
        
        with open(filename, 'w', encoding='utf-8') as mdfile:
            mdfile.write(content)
        
        logger.info(f"Markdown report exported to {filename}")
        return filename
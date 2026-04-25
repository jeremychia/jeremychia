"""Data processing and export utilities for GitHub PR analysis."""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional
import pandas as pd

from .models import GitHubPRData, ScrapingResult

logger = logging.getLogger(__name__)


class DataProcessor:
    """Process and analyze scraped PR data."""
    
    def __init__(self):
        """Initialize data processor."""
        pass
    
    def calculate_summary_stats(self, prs: List[GitHubPRData]) -> Dict[str, Any]:
        """Calculate summary statistics from PR data."""
        if not prs:
            return {}
        
        total_prs = len(prs)
        merged_prs = len([pr for pr in prs if pr.status == "merged"])
        closed_prs = len([pr for pr in prs if pr.status == "closed"])
        open_prs = len([pr for pr in prs if pr.status == "open"])
        
        # Code metrics
        total_additions = sum(pr.additions for pr in prs)
        total_deletions = sum(pr.deletions for pr in prs)
        total_files_changed = sum(pr.file_analysis.total_files_changed for pr in prs)
        
        # Review metrics
        avg_reviewers = sum(pr.review_metrics.total_reviewers for pr in prs) / total_prs if total_prs > 0 else 0
        avg_review_comments = sum(pr.review_metrics.review_comments_count for pr in prs) / total_prs if total_prs > 0 else 0
        
        # Repository distribution
        repo_counts = {}
        for pr in prs:
            repo_counts[pr.repository] = repo_counts.get(pr.repository, 0) + 1
        
        # Language distribution
        language_counts = {}
        for pr in prs:
            for lang, count in pr.file_analysis.programming_languages.items():
                language_counts[lang] = language_counts.get(lang, 0) + count
        
        # File type distribution
        file_type_counts = {}
        for pr in prs:
            for ext, count in pr.file_analysis.file_types.items():
                file_type_counts[ext] = file_type_counts.get(ext, 0) + count
        
        # Time metrics (if available)
        time_stats = {}
        time_to_merge_values = [pr.time_metrics.time_to_merge_hours for pr in prs 
                              if pr.time_metrics.time_to_merge_hours is not None]
        if time_to_merge_values:
            time_stats['avg_time_to_merge_hours'] = sum(time_to_merge_values) / len(time_to_merge_values)
            time_stats['min_time_to_merge_hours'] = min(time_to_merge_values)
            time_stats['max_time_to_merge_hours'] = max(time_to_merge_values)
        
        return {
            'summary': {
                'total_prs': total_prs,
                'merged_prs': merged_prs,
                'closed_prs': closed_prs,
                'open_prs': open_prs,
                'merge_rate': (merged_prs / total_prs * 100) if total_prs > 0 else 0
            },
            'code_metrics': {
                'total_additions': total_additions,
                'total_deletions': total_deletions,
                'net_changes': total_additions - total_deletions,
                'total_files_changed': total_files_changed,
                'avg_additions_per_pr': total_additions / total_prs if total_prs > 0 else 0,
                'avg_deletions_per_pr': total_deletions / total_prs if total_prs > 0 else 0
            },
            'review_metrics': {
                'avg_reviewers_per_pr': round(avg_reviewers, 2),
                'avg_review_comments_per_pr': round(avg_review_comments, 2)
            },
            'distributions': {
                'repositories': dict(sorted(repo_counts.items(), key=lambda x: x[1], reverse=True)),
                'programming_languages': dict(sorted(language_counts.items(), key=lambda x: x[1], reverse=True)),
                'file_types': dict(sorted(file_type_counts.items(), key=lambda x: x[1], reverse=True))
            },
            'time_metrics': time_stats
        }
    
    def create_pr_dataframe(self, prs: List[GitHubPRData]) -> pd.DataFrame:
        """Convert PR data to pandas DataFrame for analysis."""
        data = []
        
        for pr in prs:
            row = {
                # Basic info
                'repository': pr.repository,
                'pr_number': pr.pr_number,
                'title': pr.title,
                'author': pr.author,
                'state': pr.state,
                'status': pr.status,
                'url': pr.url,
                'is_draft': pr.is_draft,
                
                # Timestamps
                'created_at': pr.created_at,
                'merged_at': pr.merged_at,
                'closed_at': pr.closed_at,
                'updated_at': pr.updated_at,
                
                # Branches
                'source_branch': pr.source_branch,
                'target_branch': pr.target_branch,
                
                # Code changes
                'additions': pr.additions,
                'deletions': pr.deletions,
                'net_lines_changed': pr.net_lines_changed,
                'total_lines_changed': pr.total_lines_changed,
                'commits_count': pr.commits_count,
                'complexity_score': pr.complexity_score,
                
                # Labels and context
                'labels': ','.join(pr.labels),
                'milestone': pr.milestone,
                'linked_issues': ','.join(pr.linked_issues),
                
                # Review metrics
                'total_reviewers': pr.review_metrics.total_reviewers,
                'unique_reviewers': ','.join(pr.review_metrics.unique_reviewers),
                'review_comments_count': pr.review_metrics.review_comments_count,
                'approvals_count': pr.review_metrics.approvals_count,
                'changes_requested_count': pr.review_metrics.changes_requested_count,
                'review_cycles': pr.review_metrics.review_cycles,
                'time_to_first_review_hours': pr.review_metrics.time_to_first_review_hours,
                
                # Time metrics
                'time_open_hours': pr.time_metrics.time_open_hours,
                'time_to_merge_hours': pr.time_metrics.time_to_merge_hours,
                'time_in_draft_hours': pr.time_metrics.time_in_draft_hours,
                'business_days_open': pr.time_metrics.business_days_open,
                
                # File analysis
                'total_files_changed': pr.file_analysis.total_files_changed,
                'file_types_json': json.dumps(pr.file_analysis.file_types),
                'programming_languages_json': json.dumps(pr.file_analysis.programming_languages),
                'binary_files_count': pr.file_analysis.binary_files_count,
                'test_files_count': pr.file_analysis.test_files_count,
                'documentation_files_count': pr.file_analysis.documentation_files_count,
                
                # Engagement metrics
                'reactions_json': json.dumps(pr.engagement_metrics.reactions),
                'discussion_participants': ','.join(pr.engagement_metrics.discussion_participants),
                'total_discussion_comments': pr.engagement_metrics.total_discussion_comments,
                'mentioned_users': ','.join(pr.engagement_metrics.mentioned_users),
                
                # Additional flags
                'is_security_fix': pr.is_security_fix,
                'is_breaking_change': pr.is_breaking_change
            }
            
            data.append(row)
        
        return pd.DataFrame(data)


class DataExporter:
    """Export processed data to various formats."""
    
    def __init__(self, output_dir: str = "./outputs"):
        """Initialize exporter with output directory."""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def export_csv(
        self, 
        prs: List[GitHubPRData], 
        filename: Optional[str] = None,
        include_summary: bool = True
    ) -> Path:
        """Export PR data to CSV format."""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"github_pr_analysis_{timestamp}.csv"
        
        filepath = self.output_dir / filename
        
        processor = DataProcessor()
        df = processor.create_pr_dataframe(prs)
        
        # Export main data
        df.to_csv(filepath, index=False)
        logger.info(f"Exported {len(prs)} PRs to {filepath}")
        
        # Export summary if requested
        if include_summary:
            summary_stats = processor.calculate_summary_stats(prs)
            summary_filepath = filepath.with_name(f"summary_{filepath.name}")
            
            # Convert summary to DataFrame for CSV export
            summary_rows = []
            
            def flatten_dict(d, prefix=""):
                for key, value in d.items():
                    full_key = f"{prefix}_{key}" if prefix else key
                    if isinstance(value, dict):
                        summary_rows.extend(flatten_dict(value, full_key))
                    else:
                        summary_rows.append({
                            'metric': full_key,
                            'value': str(value)
                        })
                return summary_rows
            
            summary_df = pd.DataFrame(flatten_dict(summary_stats))
            summary_df.to_csv(summary_filepath, index=False)
            logger.info(f"Exported summary statistics to {summary_filepath}")
        
        return filepath
    
    def export_json(
        self, 
        result: ScrapingResult, 
        filename: Optional[str] = None,
        pretty_print: bool = True
    ) -> Path:
        """Export complete scraping result to JSON format."""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"github_pr_scraping_result_{timestamp}.json"
        
        filepath = self.output_dir / filename
        
        # Convert to JSON-serializable format
        json_data = {
            'metadata': {
                'total_processed': result.total_processed,
                'successful_scrapes': result.successful_scrapes,
                'failed_scrapes': result.failed_scrapes,
                'success_rate': result.success_rate,
                'processing_time_seconds': result.processing_time_seconds,
                'export_timestamp': datetime.now().isoformat(),
                'errors': result.errors
            },
            'prs': [pr.model_dump() for pr in result.prs]
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(
                json_data, 
                f, 
                indent=2 if pretty_print else None,
                default=str,  # Handle datetime serialization
                ensure_ascii=False
            )
        
        logger.info(f"Exported scraping result to {filepath}")
        return filepath
    
    def export_analysis_report(
        self, 
        prs: List[GitHubPRData], 
        filename: Optional[str] = None
    ) -> Path:
        """Export a comprehensive analysis report."""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"github_pr_analysis_report_{timestamp}.md"
        
        filepath = self.output_dir / filename
        
        processor = DataProcessor()
        stats = processor.calculate_summary_stats(prs)
        
        report_content = self._generate_markdown_report(stats, prs)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        logger.info(f"Generated analysis report: {filepath}")
        return filepath
    
    def _generate_markdown_report(self, stats: Dict[str, Any], prs: List[GitHubPRData]) -> str:
        """Generate a markdown analysis report."""
        report_lines = [
            "# GitHub PR Analysis Report",
            "",
            f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"**Total PRs Analyzed:** {len(prs)}",
            "",
            "## Summary Statistics",
            "",
        ]
        
        # Add summary section
        if 'summary' in stats:
            summary = stats['summary']
            report_lines.extend([
                f"- **Total PRs:** {summary.get('total_prs', 0)}",
                f"- **Merged PRs:** {summary.get('merged_prs', 0)}",
                f"- **Closed PRs:** {summary.get('closed_prs', 0)}",
                f"- **Open PRs:** {summary.get('open_prs', 0)}",
                f"- **Merge Rate:** {summary.get('merge_rate', 0):.1f}%",
                "",
            ])
        
        # Add code metrics
        if 'code_metrics' in stats:
            code = stats['code_metrics']
            report_lines.extend([
                "## Code Contribution Metrics",
                "",
                f"- **Total Lines Added:** {code.get('total_additions', 0):,}",
                f"- **Total Lines Deleted:** {code.get('total_deletions', 0):,}",
                f"- **Net Lines Changed:** {code.get('net_changes', 0):,}",
                f"- **Total Files Changed:** {code.get('total_files_changed', 0):,}",
                f"- **Average Additions per PR:** {code.get('avg_additions_per_pr', 0):.1f}",
                f"- **Average Deletions per PR:** {code.get('avg_deletions_per_pr', 0):.1f}",
                "",
            ])
        
        # Add repository distribution
        if 'distributions' in stats and 'repositories' in stats['distributions']:
            repos = stats['distributions']['repositories']
            report_lines.extend([
                "## Repository Distribution",
                "",
            ])
            for repo, count in list(repos.items())[:10]:  # Top 10
                report_lines.append(f"- **{repo}:** {count} PRs")
            report_lines.append("")
        
        # Add programming languages
        if 'distributions' in stats and 'programming_languages' in stats['distributions']:
            langs = stats['distributions']['programming_languages']
            if langs:
                report_lines.extend([
                    "## Programming Languages",
                    "",
                ])
                for lang, count in list(langs.items())[:10]:  # Top 10
                    report_lines.append(f"- **{lang}:** {count} lines")
                report_lines.append("")
        
        # Add recent PR highlights
        recent_prs = sorted(prs, key=lambda x: x.created_at, reverse=True)[:5]
        if recent_prs:
            report_lines.extend([
                "## Recent PR Highlights",
                "",
            ])
            for pr in recent_prs:
                report_lines.extend([
                    f"### [{pr.repository}#{pr.pr_number}]({pr.url})",
                    f"**{pr.title}**",
                    f"- Status: {pr.status.title()}",
                    f"- Lines: +{pr.additions} -{pr.deletions}",
                    f"- Files: {pr.file_analysis.total_files_changed}",
                    f"- Reviewers: {pr.review_metrics.total_reviewers}",
                    "",
                ])
        
        return "\n".join(report_lines)
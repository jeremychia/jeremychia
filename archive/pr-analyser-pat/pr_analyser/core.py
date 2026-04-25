"""Core analysis engine for PR and commit data."""

import logging
from datetime import datetime, timedelta
from typing import Optional, Dict, List, Any

from .config import Config
from .github_client import GitHubClient
from .models import AnalysisResult
from .analyzer import DataAnalyzer
from .exporter import Exporter
from .visualizer import Visualizer

logger = logging.getLogger(__name__)


class PRAnalyser:
    """Main PR and commit analysis engine."""

    def __init__(self, config: Config):
        """Initialize the analyser with configuration."""
        self.config = config
        self.github_client = GitHubClient(
            token=config.github.token,
            requests_per_hour=config.rate_limiting.requests_per_hour
        )

    def analyze(
        self,
        organization: Optional[str] = None,
        user: Optional[str] = None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        repositories: Optional[List[str]] = None,
        exclude_repositories: Optional[List[str]] = None
    ) -> AnalysisResult:
        """Perform complete analysis of user's PRs and commits."""
        
        # Use provided parameters or fall back to config
        org_name = organization or self.config.organization
        username = user or self.config.user
        
        if not org_name or not username:
            raise ValueError("Organization and user must be specified in config or as parameters")
        
        logger.info(f"Starting analysis for user {username} in organization {org_name}")
        
        # Parse date range
        date_from_parsed = None
        date_to_parsed = None
        
        if date_from:
            try:
                date_from_parsed = datetime.strptime(date_from, '%Y-%m-%d')
            except ValueError:
                logger.warning(f"Invalid date format for date_from: {date_from}, ignoring")
        
        if date_to:
            try:
                date_to_parsed = datetime.strptime(date_to, '%Y-%m-%d')
            except ValueError:
                logger.warning(f"Invalid date format for date_to: {date_to}, ignoring")
        
        # Build filters
        filters = {
            "repositories": repositories or self.config.analysis.filters["repositories"],
            "exclude_repositories": exclude_repositories or self.config.analysis.filters["exclude_repositories"],
            "branches": self.config.analysis.filters["branches"],
            "pr_status": self.config.analysis.filters["pr_status"]
        }
        
        # Fetch repositories
        logger.info("Fetching organization repositories...")
        repositories = self.github_client.get_organization_repositories(org_name, filters)
        
        if not repositories:
            logger.warning(f"No repositories found for organization {org_name}")
            return self._create_empty_result(username, org_name, date_from, date_to)
        
        # Fetch PRs and commits
        logger.info("Fetching pull requests...")
        pull_requests = self.github_client.get_user_pull_requests(
            repositories=repositories,
            username=username,
            date_from=date_from_parsed,
            date_to=date_to_parsed,
            filters=filters
        )
        
        logger.info("Fetching commits...")
        commits = self.github_client.get_user_commits(
            repositories=repositories,
            username=username,
            date_from=date_from_parsed,
            date_to=date_to_parsed,
            filters=filters
        )
        
        # Create analysis result
        result = AnalysisResult(
            user=username,
            organization=org_name,
            analysis_date=datetime.now(),
            date_range={
                "from": date_from,
                "to": date_to
            },
            total_prs=len(pull_requests),
            total_commits=len(commits),
            repositories_contributed=len(set(
                [pr.repository for pr in pull_requests] + 
                [commit.repository for commit in commits]
            )),
            pull_requests=pull_requests,
            commits=commits
        )
        
        logger.info(f"Analysis complete: {result.total_prs} PRs, {result.total_commits} commits")
        return result

    def _create_empty_result(self, username: str, org_name: str, date_from: Optional[str], date_to: Optional[str]) -> AnalysisResult:
        """Create an empty analysis result."""
        return AnalysisResult(
            user=username,
            organization=org_name,
            analysis_date=datetime.now(),
            date_range={
                "from": date_from,
                "to": date_to
            },
            total_prs=0,
            total_commits=0,
            repositories_contributed=0,
            pull_requests=[],
            commits=[]
        )

    def export_results(self, result: AnalysisResult, formats: Optional[List[str]] = None) -> Dict[str, Any]:
        """Export analysis results in specified formats."""
        if not formats:
            formats = [self.config.output.format]
        
        exporter = Exporter(result, self.config.output.directory)
        exported_files = {}
        
        for format_type in formats:
            try:
                if format_type.lower() == 'csv':
                    files = exporter.export_to_csv()
                    exported_files['csv'] = files
                elif format_type.lower() == 'json':
                    file = exporter.export_to_json()
                    exported_files['json'] = file
                elif format_type.lower() == 'markdown':
                    file = exporter.export_to_markdown()
                    exported_files['markdown'] = file
                else:
                    logger.warning(f"Unsupported export format: {format_type}")
            except Exception as e:
                logger.error(f"Error exporting to {format_type}: {e}")
        
        return exported_files

    def create_visualizations(self, result: AnalysisResult) -> List[str]:
        """Create visualizations for the analysis results."""
        if not self.config.output.visualizations:
            return []
        
        visualizer = Visualizer(result, self.config.output.directory)
        
        try:
            return visualizer.create_all_visualizations()
        except Exception as e:
            logger.error(f"Error creating visualizations: {e}")
            return []

    def get_summary_metrics(self, result: AnalysisResult) -> Dict[str, Any]:
        """Get summary metrics from analysis result."""
        analyzer = DataAnalyzer(result)
        
        metrics = analyzer.calculate_contribution_metrics()
        time_series = analyzer.get_time_series_data('M')  # Monthly data
        repo_breakdown = analyzer.get_repository_breakdown()
        collaboration = analyzer.get_collaboration_insights()
        
        return {
            'metrics': metrics.dict(),
            'time_series': time_series,
            'repository_breakdown': repo_breakdown,
            'collaboration_insights': collaboration
        }
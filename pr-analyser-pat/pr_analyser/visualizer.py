"""Data visualization and reporting."""

import logging
import os
from datetime import datetime
from typing import Dict, Any, List
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd

from .models import AnalysisResult
from .analyzer import DataAnalyzer

logger = logging.getLogger(__name__)


class Visualizer:
    """Create visualizations for PR and commit analysis."""

    def __init__(self, result: AnalysisResult, output_dir: str = "./reports"):
        """Initialize visualizer."""
        self.result = result
        self.analyzer = DataAnalyzer(result)
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def create_timeline_chart(self, period: str = 'W') -> str:
        """Create timeline chart of contributions."""
        time_series = self.analyzer.get_time_series_data(period)
        
        if not time_series or not time_series['timeline']:
            logger.warning("No data available for timeline chart")
            return ""
        
        df = pd.DataFrame(time_series['timeline'])
        
        fig = make_subplots(
            rows=2, cols=1,
            subplot_titles=('Pull Requests Over Time', 'Commits Over Time'),
            vertical_spacing=0.1
        )
        
        # PRs timeline
        fig.add_trace(
            go.Scatter(
                x=df['period'],
                y=df['prs'],
                mode='lines+markers',
                name='Pull Requests',
                line=dict(color='#2E86AB'),
                marker=dict(size=6)
            ),
            row=1, col=1
        )
        
        # Commits timeline
        fig.add_trace(
            go.Scatter(
                x=df['period'],
                y=df['commits'],
                mode='lines+markers',
                name='Commits',
                line=dict(color='#A23B72'),
                marker=dict(size=6)
            ),
            row=2, col=1
        )
        
        fig.update_layout(
            title=f"Contribution Timeline - {self.result.user}",
            height=600,
            showlegend=True
        )
        
        filename = os.path.join(self.output_dir, f"timeline_{period}.html")
        fig.write_html(filename)
        logger.info(f"Timeline chart saved to {filename}")
        return filename

    def create_repository_breakdown_chart(self) -> str:
        """Create repository contribution breakdown chart."""
        repo_data = self.analyzer.get_repository_breakdown()
        
        if not repo_data or not repo_data['repositories']:
            logger.warning("No repository data available for chart")
            return ""
        
        repos = list(repo_data['repositories'].keys())[:10]  # Top 10 repositories
        pr_counts = [repo_data['repositories'][repo]['prs'] for repo in repos]
        commit_counts = [repo_data['repositories'][repo]['commits'] for repo in repos]
        
        fig = go.Figure(data=[
            go.Bar(name='Pull Requests', x=repos, y=pr_counts, marker_color='#2E86AB'),
            go.Bar(name='Commits', x=repos, y=commit_counts, marker_color='#A23B72')
        ])
        
        fig.update_layout(
            title=f"Top Repositories by Contributions - {self.result.user}",
            xaxis_title="Repository",
            yaxis_title="Number of Contributions",
            barmode='group',
            height=500
        )
        
        filename = os.path.join(self.output_dir, "repository_breakdown.html")
        fig.write_html(filename)
        logger.info(f"Repository breakdown chart saved to {filename}")
        return filename

    def create_pr_status_pie_chart(self) -> str:
        """Create PR status distribution pie chart."""
        if not self.result.pull_requests:
            logger.warning("No PR data available for pie chart")
            return ""
        
        status_counts = {
            'Merged': self.result.merged_prs,
            'Open': self.result.open_prs,
            'Closed': self.result.closed_prs
        }
        
        # Filter out zero counts
        status_counts = {k: v for k, v in status_counts.items() if v > 0}
        
        fig = go.Figure(data=[go.Pie(
            labels=list(status_counts.keys()),
            values=list(status_counts.values()),
            hole=0.3,
            marker_colors=['#28A745', '#FFC107', '#DC3545']
        )])
        
        fig.update_layout(
            title=f"Pull Request Status Distribution - {self.result.user}",
            height=400
        )
        
        filename = os.path.join(self.output_dir, "pr_status_distribution.html")
        fig.write_html(filename)
        logger.info(f"PR status pie chart saved to {filename}")
        return filename

    def create_contribution_heatmap(self) -> str:
        """Create contribution heatmap."""
        if not self.result.commits:
            logger.warning("No commit data available for heatmap")
            return ""
        
        # Create DataFrame with commit dates
        dates = [commit.authored_date.date() for commit in self.result.commits]
        df = pd.DataFrame({'date': dates})
        df['count'] = 1
        
        # Group by date and count commits
        daily_commits = df.groupby('date')['count'].sum().reset_index()
        daily_commits['date'] = pd.to_datetime(daily_commits['date'])
        daily_commits['weekday'] = daily_commits['date'].dt.day_name()
        daily_commits['week'] = daily_commits['date'].dt.isocalendar().week
        
        # Create pivot table for heatmap
        heatmap_data = daily_commits.pivot_table(
            index='weekday',
            columns='week',
            values='count',
            fill_value=0
        )
        
        # Reorder weekdays
        weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        heatmap_data = heatmap_data.reindex(weekday_order)
        
        fig = go.Figure(data=go.Heatmap(
            z=heatmap_data.values,
            x=heatmap_data.columns,
            y=heatmap_data.index,
            colorscale='YlOrRd',
            showscale=True
        ))
        
        fig.update_layout(
            title=f"Contribution Heatmap - {self.result.user}",
            xaxis_title="Week of Year",
            yaxis_title="Day of Week",
            height=400
        )
        
        filename = os.path.join(self.output_dir, "contribution_heatmap.html")
        fig.write_html(filename)
        logger.info(f"Contribution heatmap saved to {filename}")
        return filename

    def create_pr_size_distribution(self) -> str:
        """Create PR size distribution chart."""
        if not self.result.pull_requests:
            logger.warning("No PR data available for size distribution")
            return ""
        
        sizes = [pr.total_changes for pr in self.result.pull_requests]
        
        fig = go.Figure(data=[go.Histogram(
            x=sizes,
            nbinsx=20,
            marker_color='#2E86AB',
            opacity=0.7
        )])
        
        fig.update_layout(
            title=f"Pull Request Size Distribution - {self.result.user}",
            xaxis_title="Lines Changed",
            yaxis_title="Number of PRs",
            height=400
        )
        
        filename = os.path.join(self.output_dir, "pr_size_distribution.html")
        fig.write_html(filename)
        logger.info(f"PR size distribution chart saved to {filename}")
        return filename

    def create_all_visualizations(self) -> List[str]:
        """Create all visualizations and return list of filenames."""
        created_files = []
        
        try:
            file = self.create_timeline_chart('W')
            if file:
                created_files.append(file)
        except Exception as e:
            logger.error(f"Error creating timeline chart: {e}")
        
        try:
            file = self.create_repository_breakdown_chart()
            if file:
                created_files.append(file)
        except Exception as e:
            logger.error(f"Error creating repository breakdown chart: {e}")
        
        try:
            file = self.create_pr_status_pie_chart()
            if file:
                created_files.append(file)
        except Exception as e:
            logger.error(f"Error creating PR status pie chart: {e}")
        
        try:
            file = self.create_contribution_heatmap()
            if file:
                created_files.append(file)
        except Exception as e:
            logger.error(f"Error creating contribution heatmap: {e}")
        
        try:
            file = self.create_pr_size_distribution()
            if file:
                created_files.append(file)
        except Exception as e:
            logger.error(f"Error creating PR size distribution: {e}")
        
        return created_files
"""Tests for data analyzer."""

import pytest
from pr_analyser.analyzer import DataAnalyzer


def test_data_analyzer_initialization(sample_analysis_result):
    """Test DataAnalyzer initialization."""
    analyzer = DataAnalyzer(sample_analysis_result)
    
    assert analyzer.result == sample_analysis_result
    assert not analyzer.pr_df.empty
    assert not analyzer.commit_df.empty


def test_contribution_metrics_calculation(sample_analysis_result):
    """Test contribution metrics calculation."""
    analyzer = DataAnalyzer(sample_analysis_result)
    metrics = analyzer.calculate_contribution_metrics()
    
    assert metrics.total_contributions == 2  # 1 PR + 1 commit
    assert metrics.prs_created == 1
    assert metrics.prs_merged == 1
    assert metrics.prs_closed == 0
    assert metrics.commits_made == 1
    assert metrics.lines_added == 150  # From PR
    assert metrics.lines_deleted == 25  # From PR
    assert metrics.repositories_touched == 1
    assert metrics.average_pr_size == 175.0
    assert metrics.merge_rate == 100.0


def test_time_series_data(sample_analysis_result):
    """Test time series data generation."""
    analyzer = DataAnalyzer(sample_analysis_result)
    time_series = analyzer.get_time_series_data('D')  # Use pandas frequency string
    
    assert 'timeline' in time_series
    assert 'total_periods' in time_series
    assert len(time_series['timeline']) > 0


def test_repository_breakdown(sample_analysis_result):
    """Test repository breakdown analysis."""
    analyzer = DataAnalyzer(sample_analysis_result)
    breakdown = analyzer.get_repository_breakdown()
    
    assert 'repositories' in breakdown
    assert 'total_repositories' in breakdown
    assert breakdown['total_repositories'] == 1
    assert 'test-repo' in breakdown['repositories']


def test_collaboration_insights(sample_analysis_result):
    """Test collaboration insights analysis."""
    analyzer = DataAnalyzer(sample_analysis_result)
    insights = analyzer.get_collaboration_insights()
    
    assert 'top_reviewers' in insights
    assert 'prs_with_reviews' in insights
    assert 'review_rate' in insights
    assert insights['prs_with_reviews'] == 1
    assert insights['total_unique_reviewers'] == 2
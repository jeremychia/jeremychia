"""Tests for data models."""

import pytest
from datetime import datetime
from pr_analyser.models import PRData, CommitData, AnalysisResult


def test_pr_data_total_changes(sample_pr_data):
    """Test PR data total changes calculation."""
    assert sample_pr_data.total_changes == 175  # 150 + 25


def test_pr_data_status_merged(sample_pr_data):
    """Test PR status for merged PR."""
    assert sample_pr_data.status == "merged"


def test_pr_data_status_open():
    """Test PR status for open PR."""
    pr = PRData(
        id=1, number=1, title="Test", description="", repository="test",
        author="user", state="open", merged=False, created_at=datetime.now(),
        updated_at=datetime.now(), source_branch="feature", target_branch="main",
        additions=10, deletions=5, changed_files=2, comments_count=0,
        reviewers=[], labels=[]
    )
    assert pr.status == "open"


def test_commit_data_short_sha(sample_commit_data):
    """Test commit short SHA generation."""
    assert sample_commit_data.short_sha == "abc123d"


def test_commit_data_short_message(sample_commit_data):
    """Test commit short message extraction."""
    assert sample_commit_data.short_message == "Add new feature implementation"


def test_analysis_result_properties(sample_analysis_result):
    """Test analysis result computed properties."""
    assert sample_analysis_result.merged_prs == 1
    assert sample_analysis_result.open_prs == 0
    assert sample_analysis_result.closed_prs == 0
    assert sample_analysis_result.total_lines_added == 150
    assert sample_analysis_result.total_lines_deleted == 25
    assert sample_analysis_result.total_files_changed == 5
    assert sample_analysis_result.average_pr_size == 175.0
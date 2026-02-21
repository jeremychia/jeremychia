"""Test configuration and fixtures."""

import pytest
from datetime import datetime
from pr_analyser.models import PRData, CommitData, AnalysisResult


@pytest.fixture
def sample_pr_data():
    """Sample PR data for testing."""
    return PRData(
        id=123456,
        number=42,
        title="Add new feature",
        description="This PR adds a new feature to the application",
        repository="test-repo",
        author="testuser",
        state="closed",
        merged=True,
        created_at=datetime(2024, 1, 15, 10, 30),
        updated_at=datetime(2024, 1, 16, 14, 20),
        merged_at=datetime(2024, 1, 16, 14, 20),
        closed_at=datetime(2024, 1, 16, 14, 20),
        source_branch="feature/new-feature",
        target_branch="main",
        additions=150,
        deletions=25,
        changed_files=5,
        comments_count=3,
        reviewers=["reviewer1", "reviewer2"],
        labels=["enhancement", "feature"]
    )


@pytest.fixture
def sample_commit_data():
    """Sample commit data for testing."""
    return CommitData(
        sha="abc123def456",
        message="Add new feature implementation\n\nThis commit implements the core functionality",
        repository="test-repo",
        author="testuser",
        author_email="testuser@example.com",
        authored_date=datetime(2024, 1, 15, 9, 15),
        committed_date=datetime(2024, 1, 15, 9, 15),
        additions=120,
        deletions=15,
        total_changes=135,
        files_changed=["src/main.py", "src/utils.py", "tests/test_main.py"]
    )


@pytest.fixture
def sample_analysis_result(sample_pr_data, sample_commit_data):
    """Sample analysis result for testing."""
    return AnalysisResult(
        user="testuser",
        organization="testorg",
        analysis_date=datetime(2024, 1, 20, 12, 0),
        date_range={"from": "2024-01-01", "to": "2024-01-31"},
        total_prs=1,
        total_commits=1,
        repositories_contributed=1,
        pull_requests=[sample_pr_data],
        commits=[sample_commit_data]
    )
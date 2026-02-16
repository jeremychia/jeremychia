"""Display and formatting utilities for the PR Analyser CLI."""

from rich.table import Table
from rich.console import Console


def display_summary(result, console: Console):
    """Display analysis summary in a formatted table."""
    
    # Create summary table
    table = Table(title=f"Analysis Summary - {result.user}")
    table.add_column("Metric", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")
    
    table.add_row("Total Pull Requests", str(result.total_prs))
    table.add_row("Merged PRs", str(result.merged_prs))
    table.add_row("Open PRs", str(result.open_prs))
    table.add_row("Closed PRs", str(result.closed_prs))
    table.add_row("Total Commits", str(result.total_commits))
    table.add_row("Repositories Contributed", str(result.repositories_contributed))
    table.add_row("Lines Added", f"{result.total_lines_added:,}")
    table.add_row("Lines Deleted", f"{result.total_lines_deleted:,}")
    table.add_row("Files Changed", f"{result.total_files_changed:,}")
    table.add_row("Average PR Size", f"{result.average_pr_size:.1f} lines")
    
    console.print()
    console.print(table)


def format_file_size(size_bytes: int) -> str:
    """Format file size in human readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"


def format_duration(seconds: int) -> str:
    """Format duration in human readable format."""
    if seconds < 60:
        return f"{seconds}s"
    elif seconds < 3600:
        minutes = seconds // 60
        return f"{minutes}m {seconds % 60}s"
    else:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return f"{hours}h {minutes}m"
"""Command-line interface for GitHub PR scraper."""

import asyncio
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, List

import click
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel

from .config import ConfigManager
from .cli_analyzer import GitHubCLIAnalyzer
from .models import AnalysisConfig, ScrapingResult
from .exporter import DataExporter, DataProcessor

console = Console()
logger = logging.getLogger(__name__)


@click.group()
@click.option('--config', '-c', type=click.Path(exists=True), help='Configuration file path')
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose logging')
@click.pass_context
def main(ctx, config: Optional[str], verbose: bool):
    """GitHub PR Scraper - Advanced PR analysis using web scraping."""
    
    ctx.ensure_object(dict)
    ctx.obj['config_file'] = config
    ctx.obj['verbose'] = verbose
    
    # Skip config loading for init-config command
    if ctx.invoked_subcommand in ['init_config', 'init-config']:
        return
    
    # Initialize config manager for other commands
    config_manager = ConfigManager(config)
    
    try:
        app_config = config_manager.load_config()
        config_manager.setup_logging()
        
        if verbose:
            logging.getLogger().setLevel(logging.DEBUG)
        
        # Store config in context for subcommands
        ctx.obj['config'] = app_config
        ctx.obj['config_manager'] = config_manager
        
    except Exception as e:
        console.print(f"[red]Configuration error: {e}[/red]")
        console.print("[yellow]Use 'github-pr-scraper init-config' to create a sample configuration[/yellow]")
        ctx.exit(1)


@main.command('init-config')
@click.option('--output', '-o', default='config.yaml', help='Output configuration file')
@click.pass_context
def init_config(ctx, output: str):
    """Create a sample configuration file."""
    config_manager = ConfigManager()
    
    try:
        config_manager.create_sample_config(output)
        console.print(f"[green]✓[/green] Created sample configuration: {output}")
        console.print("[yellow]Please edit the configuration file with your GitHub credentials[/yellow]")
    except Exception as e:
        console.print(f"[red]Failed to create config file: {e}[/red]")


@main.command()
@click.option('--user', '-u', required=True, help='GitHub username to analyze')
@click.option('--org', '--organization', help='GitHub organization to focus on')
@click.option('--repos', help='Comma-separated list of repositories to include')
@click.option('--exclude-repos', help='Comma-separated list of repositories to exclude')
@click.option('--from', 'date_from', help='Start date (YYYY-MM-DD)')
@click.option('--to', 'date_to', help='End date (YYYY-MM-DD)')
@click.option('--max-prs', type=int, help='Maximum number of PRs to analyze')
@click.option('--include-drafts/--no-drafts', default=True, help='Include draft PRs')
@click.option('--include-closed/--no-closed', default=True, help='Include closed PRs')
@click.option('--output-dir', '-d', help='Output directory for results')
@click.option('--format', 'output_format', type=click.Choice(['csv', 'json', 'both']), help='Output format')
@click.pass_context
def analyze(
    ctx, user: str, org: Optional[str], repos: Optional[str], exclude_repos: Optional[str],
    date_from: Optional[str], date_to: Optional[str], max_prs: Optional[int],
    include_drafts: bool, include_closed: bool, output_dir: Optional[str],
    output_format: Optional[str]
):
    """Analyze GitHub PRs for a user."""
    
    app_config = ctx.obj['config']
    
    # Parse date strings
    parsed_date_from = None
    parsed_date_to = None
    
    if date_from:
        try:
            parsed_date_from = datetime.strptime(date_from, '%Y-%m-%d')
        except ValueError:
            console.print(f"[red]Invalid date format: {date_from}. Use YYYY-MM-DD[/red]")
            ctx.exit(1)
    
    if date_to:
        try:
            parsed_date_to = datetime.strptime(date_to, '%Y-%m-%d')
        except ValueError:
            console.print(f"[red]Invalid date format: {date_to}. Use YYYY-MM-DD[/red]")
            ctx.exit(1)
    
    # Parse repository lists
    repositories = repos.split(',') if repos else []
    exclude_repositories = exclude_repos.split(',') if exclude_repos else []
    
    # Create analysis config
    analysis_config = AnalysisConfig(
        username=user,
        organization=org,
        repositories=repositories,
        exclude_repositories=exclude_repositories,
        date_from=parsed_date_from,
        date_to=parsed_date_to,
        include_drafts=include_drafts,
        include_closed=include_closed,
        max_prs=max_prs
    )
    
    # Override output settings if provided
    if output_dir:
        app_config.output.output_dir = output_dir
    if output_format:
        app_config.output.default_format = output_format
    
    # Display analysis info
    _display_analysis_info(analysis_config, app_config)
    
    # Run the analysis
    _run_analysis(analysis_config, app_config)


def _run_analysis(analysis_config: AnalysisConfig, app_config):
    """Run the PR analysis using GitHub CLI."""
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:
        
        # Initialize CLI analyzer
        task = progress.add_task("Initializing GitHub CLI analyzer...", total=None)
        
        try:
            analyzer = GitHubCLIAnalyzer()
            console.print("[green]✓[/green] GitHub CLI is ready")
            
            # Start analysis
            progress.update(task, description="Fetching PR data...")
            
            start_time = datetime.now()
            
            prs = analyzer.get_user_prs(
                username=analysis_config.username,
                organization=analysis_config.organization,
                repositories=analysis_config.repositories,
                date_from=analysis_config.date_from,
                date_to=analysis_config.date_to,
                max_prs=analysis_config.max_prs,
                include_closed=analysis_config.include_closed,
                include_merged=True  # Always include merged
            )
            
            end_time = datetime.now()
            processing_time = (end_time - start_time).total_seconds()
            
            # Create result object
            result = ScrapingResult(
                prs=prs,
                total_processed=len(prs),
                successful_scrapes=len(prs),
                failed_scrapes=0,
                errors=[],
                processing_time_seconds=processing_time
            )
            
            progress.update(task, description="Processing results...")
            
            # Display results summary
            _display_results_summary(result)
            
            # Export data
            exporter = DataExporter(app_config.output.output_dir)
            
            if app_config.output.default_format in ['csv', 'both']:
                csv_file = exporter.export_csv(
                    result.prs, 
                    include_summary=app_config.output.include_summary
                )
                console.print(f"[green]✓[/green] Exported CSV: {csv_file}")
            
            if app_config.output.default_format in ['json', 'both']:
                json_file = exporter.export_json(
                    result, 
                    pretty_print=app_config.output.pretty_json
                )
                console.print(f"[green]✓[/green] Exported JSON: {json_file}")
            
            if app_config.output.generate_report:
                report_file = exporter.export_analysis_report(result.prs)
                console.print(f"[green]✓[/green] Generated report: {report_file}")
            
            # Display top insights
            _display_insights(result.prs)
            
        except Exception as e:
            console.print(f"[red]✗[/red] Analysis failed: {e}")
            logger.exception("Analysis failed")


def _display_analysis_info(analysis_config: AnalysisConfig, app_config):
    """Display analysis configuration info."""
    
    info_lines = [
        f"User: {analysis_config.username}",
        f"Organization: {analysis_config.organization or 'All'}",
        f"Repositories: {', '.join(analysis_config.repositories) or 'All'}",
    ]
    
    if analysis_config.date_from:
        info_lines.append(f"From: {analysis_config.date_from.strftime('%Y-%m-%d')}")
    if analysis_config.date_to:
        info_lines.append(f"To: {analysis_config.date_to.strftime('%Y-%m-%d')}")
    if analysis_config.max_prs:
        info_lines.append(f"Max PRs: {analysis_config.max_prs}")
    
    info_lines.extend([
        f"Include drafts: {analysis_config.include_drafts}",
        f"Include closed: {analysis_config.include_closed}",
        f"Output format: {app_config.output.default_format}",
        f"Output directory: {app_config.output.output_dir}"
    ])
    
    panel = Panel(
        "\\n".join(info_lines),
        title="Analysis Configuration",
        border_style="blue"
    )
    console.print(panel)


def _display_results_summary(result):
    """Display scraping results summary."""
    
    table = Table(title="Scraping Results")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")
    
    table.add_row("Total Processed", str(result.total_processed))
    table.add_row("Successful Scrapes", str(result.successful_scrapes))
    table.add_row("Failed Scrapes", str(result.failed_scrapes))
    table.add_row("Success Rate", f"{result.success_rate:.1f}%")
    table.add_row("Processing Time", f"{result.processing_time_seconds:.1f}s")
    
    console.print(table)
    
    if result.errors:
        console.print(f"\\n[yellow]Errors encountered ({len(result.errors)}):[/yellow]")
        for error in result.errors[:5]:  # Show first 5 errors
            console.print(f"  • {error}")
        if len(result.errors) > 5:
            console.print(f"  ... and {len(result.errors) - 5} more")


def _display_insights(prs: List):
    """Display key insights from analyzed PRs."""
    
    if not prs:
        return
    
    processor = DataProcessor()
    stats = processor.calculate_summary_stats(prs)
    
    # Top repositories
    if stats.get('distributions', {}).get('repositories'):
        table = Table(title="Top Repositories")
        table.add_column("Repository", style="cyan")
        table.add_column("PRs", style="green")
        
        top_repos = list(stats['distributions']['repositories'].items())[:5]
        for repo, count in top_repos:
            table.add_row(repo, str(count))
        
        console.print(table)
    
    # Code metrics summary
    if 'code_metrics' in stats:
        code = stats['code_metrics']
        
        metrics_table = Table(title="Code Contribution Summary")
        metrics_table.add_column("Metric", style="cyan")
        metrics_table.add_column("Value", style="green")
        
        metrics_table.add_row("Total Lines Added", f"{code.get('total_additions', 0):,}")
        metrics_table.add_row("Total Lines Deleted", f"{code.get('total_deletions', 0):,}")
        metrics_table.add_row("Net Lines Changed", f"{code.get('net_changes', 0):,}")
        metrics_table.add_row("Files Changed", f"{code.get('total_files_changed', 0):,}")
        metrics_table.add_row("Avg. Additions/PR", f"{code.get('avg_additions_per_pr', 0):.1f}")
        
        console.print(metrics_table)


@main.command()
@click.option('--user', '-u', required=True, help='GitHub username')
@click.option('--days', '-d', default=30, type=int, help='Number of days to look back')
@click.pass_context
def quick_analysis(ctx, user: str, days: int):
    """Quick analysis of recent PRs."""
    
    date_from = datetime.now() - timedelta(days=days)
    
    analysis_config = AnalysisConfig(
        username=user,
        date_from=date_from,
        max_prs=50,
        include_drafts=True,
        include_closed=True
    )
    
    app_config = ctx.obj['config']
    
    console.print(f"[blue]Running quick analysis for {user} (last {days} days)[/blue]")
    
    _run_analysis(analysis_config, app_config)


if __name__ == '__main__':
    main()
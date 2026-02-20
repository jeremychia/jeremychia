"""Analysis command for the PR Analyser CLI."""

import sys
import logging
from typing import Optional, List

import click
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel

from ..config import load_config
from ..core import PRAnalyser
from ..auth import AuthManager
from ..display import display_summary

logger = logging.getLogger(__name__)
console = Console()


@click.command()
@click.option('--config', '-c', type=click.Path(exists=True), help='Configuration file path')
@click.option('--org', '-o', help='GitHub organization name')
@click.option('--user', '-u', help='GitHub username to analyze')
@click.option('--from', 'date_from', help='Start date (YYYY-MM-DD)')
@click.option('--to', 'date_to', help='End date (YYYY-MM-DD)')
@click.option('--repository', 'repositories', multiple=True, help='Specific repositories to include')
@click.option('--exclude-repository', 'exclude_repositories', multiple=True, help='Repositories to exclude')
@click.option('--export', 'export_formats', multiple=True, 
              type=click.Choice(['csv', 'json', 'markdown'], case_sensitive=False),
              help='Export formats (can be used multiple times)')
@click.option('--visualize/--no-visualize', default=None, help='Create visualizations')
@click.option('--output-dir', '-d', help='Output directory for reports')
@click.option('--reauth', is_flag=True, help='Force re-authentication')
@click.pass_context
def analyze(ctx, config, org, user, date_from, date_to, repositories, exclude_repositories, 
           export_formats, visualize, output_dir, reauth):
    """Analyze GitHub PRs and commits for a user."""
    
    try:
        # Load configuration
        with console.status("Loading configuration..."):
            app_config = load_config(config)
        
        # Override config with command line parameters
        if org:
            app_config.organization = org
        if user:
            app_config.user = user
        if output_dir:
            app_config.output.directory = output_dir
        if visualize is not None:
            app_config.output.visualizations = visualize
        
        # Determine target user for authentication
        target_user = app_config.user
        if not target_user:
            console.print("[red]Error: User not specified. Use --user parameter or set in config file.[/red]")
            sys.exit(1)
        
        # Handle authentication
        auth_manager = AuthManager()
        token = auth_manager.get_auth_token(target_user, force_reauth=reauth)
        
        if not token:
            console.print("[red]Error: Authentication failed. Cannot proceed without valid GitHub token.[/red]")
            sys.exit(1)
        
        # Update config with authenticated token
        app_config.github.token = token
        
        # Validate required parameters
        if not app_config.organization:
            console.print("[red]Error: Organization not specified. Use --org parameter or set in config file.[/red]")
            sys.exit(1)
        
        # Create analyser
        analyser = PRAnalyser(app_config)
        
        # Display analysis info
        _display_analysis_config(app_config, date_from, date_to)
        
        # Perform analysis
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            
            task = progress.add_task("Analyzing repositories and contributions...", total=None)
            
            result = analyser.analyze(
                organization=app_config.organization,
                user=app_config.user,
                date_from=date_from,
                date_to=date_to,
                repositories=list(repositories) if repositories else None,
                exclude_repositories=list(exclude_repositories) if exclude_repositories else None
            )
            
            progress.update(task, description="Analysis complete!")
        
        # Display summary
        display_summary(result, console)
        
        # Export results
        if export_formats:
            _export_results(analyser, result, export_formats)
        
        # Create visualizations
        if app_config.output.visualizations:
            _create_visualizations(analyser, result)
        
        console.print(f"\n[bold green]Analysis complete![/bold green] Reports saved to: {app_config.output.directory}")
        
    except Exception as e:
        logger.error(f"Analysis failed: {e}")
        console.print(f"[red]Error: {e}[/red]")
        sys.exit(1)


def _display_analysis_config(config, date_from: Optional[str], date_to: Optional[str]):
    """Display analysis configuration panel."""
    info_panel = Panel(
        f"[bold]Organization:[/bold] {config.organization}\n"
        f"[bold]User:[/bold] {config.user}\n"
        f"[bold]Date Range:[/bold] {date_from or 'All time'} to {date_to or 'All time'}\n"
        f"[bold]Output Directory:[/bold] {config.output.directory}",
        title="Analysis Configuration",
        border_style="blue"
    )
    console.print(info_panel)


def _export_results(analyser: PRAnalyser, result, export_formats: List[str]):
    """Export analysis results in specified formats."""
    with console.status("Exporting results..."):
        exported_files = analyser.export_results(result, list(export_formats))
        
    console.print("\n[bold green]Export Complete![/bold green]")
    for format_type, files in exported_files.items():
        if isinstance(files, dict):
            for file_type, filename in files.items():
                console.print(f"  {format_type.upper()} ({file_type}): {filename}")
        else:
            console.print(f"  {format_type.upper()}: {files}")


def _create_visualizations(analyser: PRAnalyser, result):
    """Create visualizations for analysis results."""
    with console.status("Creating visualizations..."):
        viz_files = analyser.create_visualizations(result)
    
    if viz_files:
        console.print("\n[bold green]Visualizations Created![/bold green]")
        for filename in viz_files:
            console.print(f"  {filename}")
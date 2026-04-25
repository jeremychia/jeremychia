"""Command-line interface for the PR Analyser."""

import logging

import click
from rich.console import Console

from .commands.analyze import analyze
from .commands.auth import validate_config, init, logout

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

console = Console()


@click.group()
@click.version_option(version='0.1.0')
@click.pass_context
def cli(ctx):
    """GitHub PR and Commit Analysis Tool
    
    Analyze GitHub Pull Requests and commits made by a user within an organization,
    providing insights into contribution patterns, code quality metrics, and productivity trends.
    """
    ctx.ensure_object(dict)


# Register commands
cli.add_command(analyze)
cli.add_command(validate_config)
cli.add_command(init)
cli.add_command(logout)


def main():
    """Main entry point for the CLI."""
    cli()


if __name__ == '__main__':
    main()
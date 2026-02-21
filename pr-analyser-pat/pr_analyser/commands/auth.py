"""Authentication commands for the PR Analyser CLI."""

import sys
from pathlib import Path

import click
from rich.console import Console

from ..config import load_config
from ..core import PRAnalyser
from ..auth import AuthManager

console = Console()


@click.command()
@click.option('--config', '-c', type=click.Path(exists=True), help='Configuration file path')
@click.option('--user', '-u', help='GitHub username to validate')
def validate_config(config, user):
    """Validate configuration and GitHub credentials."""
    
    try:
        with console.status("Validating configuration..."):
            app_config = load_config(config)
        
        # Get user for validation
        target_user = user or app_config.user
        if not target_user:
            console.print("[red]Error: User not specified for validation.[/red]")
            sys.exit(1)
        
        # Check authentication
        auth_manager = AuthManager()
        token = auth_manager.get_stored_token(target_user)
        
        if not token:
            console.print(f"[red]No stored authentication found for user {target_user}[/red]")
            if click.confirm("Authenticate now?"):
                token = auth_manager.authenticate_interactive(target_user)
                if not token:
                    sys.exit(1)
            else:
                sys.exit(1)
        
        app_config.github.token = token
        app_config.user = target_user
        
        # Check organization
        if not app_config.organization:
            console.print("[yellow]Warning: No organization specified[/yellow]")
        
        # Test GitHub connection
        with console.status("Testing GitHub connection..."):
            analyser = PRAnalyser(app_config)
            if app_config.organization:
                repos = analyser.github_client.get_organization_repositories(app_config.organization)
                
                console.print("[green]✓ Configuration valid![/green]")
                console.print(f"  GitHub token: Valid for user {target_user}")
                console.print(f"  Organization: {app_config.organization} ({len(repos)} repositories found)")
            else:
                console.print("[green]✓ Authentication valid![/green]")
                console.print(f"  GitHub token: Valid for user {target_user}")
        
    except Exception as e:
        console.print(f"[red]Validation failed: {e}[/red]")
        sys.exit(1)


@click.command()
@click.option('--user', '-u', help='GitHub username')
@click.option('--org', '-o', help='GitHub organization')
def init(user, org):
    """Initialize authentication for PR Analyser."""
    
    console.print("[bold]PR Analyser Authentication Setup[/bold]\n")
    
    # Get username
    if not user:
        user = click.prompt("GitHub Username", type=str)
    
    # Get organization (optional)
    if not org:
        org = click.prompt("GitHub Organization (optional)", type=str, default="", show_default=False)
        if not org.strip():
            org = None
    
    # Authenticate
    auth_manager = AuthManager()
    token = auth_manager.authenticate_interactive(user)
    
    if token:
        console.print(f"\n[green]✓ Authentication successful for {user}[/green]")
        
        # Create/update .env file if organization is provided
        if org:
            env_content = f"GITHUB_ORG={org}\nGITHUB_USER={user}\n"
            
            env_path = Path(".env")
            with open(env_path, "w") as f:
                f.write(env_content)
            
            console.print(f"[green]✓ Configuration saved to {env_path}[/green]")
        
        console.print(f"\nYou can now run: [bold]pr-analyser analyze --user {user}" + (f" --org {org}" if org else "") + "[/bold]")
    else:
        console.print("[red]Authentication failed[/red]")
        sys.exit(1)


@click.command()
@click.option('--user', '-u', help='GitHub username to logout')
def logout(user):
    """Remove stored authentication for a user."""
    
    if not user:
        user = click.prompt("GitHub Username to logout", type=str)
    
    auth_manager = AuthManager()
    success = auth_manager.logout(user)
    
    if not success:
        sys.exit(1)
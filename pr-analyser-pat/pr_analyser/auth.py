"""Authentication management for GitHub API access."""

import logging
import keyring
import getpass
from typing import Optional
import webbrowser
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.text import Text

logger = logging.getLogger(__name__)
console = Console()

SERVICE_NAME = "pr-analyser-github"


class AuthManager:
    """Manage GitHub authentication with secure storage."""
    
    def __init__(self):
        self.console = Console()
    
    def get_stored_token(self, username: str) -> Optional[str]:
        """Retrieve stored GitHub token for user."""
        try:
            token = keyring.get_password(SERVICE_NAME, username)
            return token
        except Exception as e:
            logger.debug(f"Error retrieving stored token: {e}")
            return None
    
    def store_token(self, username: str, token: str) -> bool:
        """Store GitHub token securely."""
        try:
            keyring.set_password(SERVICE_NAME, username, token)
            return True
        except Exception as e:
            logger.error(f"Error storing token: {e}")
            return False
    
    def delete_stored_token(self, username: str) -> bool:
        """Delete stored GitHub token."""
        try:
            keyring.delete_password(SERVICE_NAME, username)
            return True
        except Exception as e:
            logger.debug(f"Error deleting token: {e}")
            return False
    
    def authenticate_interactive(self, username: str) -> Optional[str]:
        """Interactive authentication flow."""
        
        # Check if token is already stored
        stored_token = self.get_stored_token(username)
        if stored_token:
            if Confirm.ask(f"Use stored authentication for [bold]{username}[/bold]?", default=True):
                return stored_token
            else:
                # User wants to re-authenticate
                self.delete_stored_token(username)
        
        # Show authentication instructions
        self._show_auth_instructions()
        
        # Prompt for token
        token = Prompt.ask(
            "Enter your GitHub Personal Access Token",
            password=True,
            show_default=False
        )
        
        if not token:
            self.console.print("[red]No token provided. Authentication cancelled.[/red]")
            return None
        
        # Validate token by making a test API call
        if self._validate_token(token, username):
            # Ask if user wants to store the token
            if Confirm.ask("Store this token securely for future use?", default=True):
                if self.store_token(username, token):
                    self.console.print("[green]✓ Token stored securely[/green]")
                else:
                    self.console.print("[yellow]Warning: Could not store token securely[/yellow]")
            
            return token
        else:
            self.console.print("[red]Invalid token or insufficient permissions[/red]")
            return None
    
    def _show_auth_instructions(self):
        """Show GitHub token creation instructions."""
        instructions = Text()
        instructions.append("GitHub Personal Access Token Required\n\n", style="bold")
        instructions.append("1. Go to: ", style="white")
        instructions.append("https://github.com/settings/tokens/new", style="blue underline")
        instructions.append("\n2. Create a token with these permissions:\n", style="white")
        instructions.append("   • ", style="white")
        instructions.append("repo", style="green")
        instructions.append(" (Full control of private repositories)\n", style="white")
        instructions.append("   • ", style="white")
        instructions.append("read:org", style="green")
        instructions.append(" (Read org and team membership)\n", style="white")
        instructions.append("   • ", style="white")
        instructions.append("read:user", style="green")
        instructions.append(" (Read user profile data)\n\n", style="white")
        instructions.append("3. Copy the generated token and paste it below\n", style="white")
        
        panel = Panel(
            instructions,
            title="Authentication Setup",
            border_style="blue",
            expand=False
        )
        
        self.console.print(panel)
        
        # Ask if user wants to open the URL
        if Confirm.ask("Open GitHub token page in browser?", default=True):
            try:
                webbrowser.open("https://github.com/settings/tokens/new")
            except Exception as e:
                logger.debug(f"Could not open browser: {e}")
    
    def _validate_token(self, token: str, username: str) -> bool:
        """Validate GitHub token by making a test API call."""
        import requests
        
        headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        
        try:
            # Test token with user endpoint
            response = requests.get('https://api.github.com/user', headers=headers, timeout=10)
            
            if response.status_code == 200:
                user_data = response.json()
                api_username = user_data.get('login', '').lower()
                
                # Check if the token belongs to the expected user
                if username.lower() != api_username:
                    self.console.print(f"[yellow]Warning: Token belongs to '{api_username}', but you specified '{username}'[/yellow]")
                    if not Confirm.ask("Continue anyway?", default=False):
                        return False
                
                # Check rate limits
                rate_limit = int(response.headers.get('x-ratelimit-limit', 0))
                if rate_limit < 1000:
                    self.console.print("[yellow]Warning: Token has low rate limit. Consider using a different token.[/yellow]")
                
                return True
            elif response.status_code == 401:
                return False
            else:
                logger.warning(f"Unexpected response from GitHub API: {response.status_code}")
                return False
                
        except requests.RequestException as e:
            logger.error(f"Error validating token: {e}")
            return False
    
    def get_auth_token(self, username: str, force_reauth: bool = False) -> Optional[str]:
        """Get authentication token with fallback to interactive auth."""
        
        if force_reauth:
            self.delete_stored_token(username)
            return self.authenticate_interactive(username)
        
        # Try stored token first
        token = self.get_stored_token(username)
        if token:
            return token
        
        # Fallback to interactive authentication
        return self.authenticate_interactive(username)
    
    def list_stored_users(self) -> list:
        """List users with stored authentication."""
        # This is a simplified version - keyring doesn't provide a direct way to list all entries
        # In practice, you might want to maintain a separate config file listing authenticated users
        return []
    
    def logout(self, username: str) -> bool:
        """Remove stored authentication for user."""
        success = self.delete_stored_token(username)
        if success:
            self.console.print(f"[green]✓ Removed stored authentication for {username}[/green]")
        else:
            self.console.print(f"[yellow]No stored authentication found for {username}[/yellow]")
        return success
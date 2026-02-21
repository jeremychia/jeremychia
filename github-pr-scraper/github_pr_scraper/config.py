"""Configuration management for GitHub PR scraper."""

import os
import logging
from typing import Optional, List
from pathlib import Path

from pydantic import BaseModel, Field
from dotenv import load_dotenv
import yaml

logger = logging.getLogger(__name__)


class GitHubConfig(BaseModel):
    """GitHub connection settings."""
    base_url: str = "https://github.com"
    use_existing_session: bool = True  # Use existing browser session
    browser_user_data_dir: Optional[str] = None  # Custom browser profile path


class ScrapingConfig(BaseModel):
    """Web scraping behavior settings."""
    headless: bool = True
    slow_mo: int = 1000  # Milliseconds between actions
    timeout: int = 30000  # Page timeout in milliseconds
    concurrent_pages: int = 3  # Number of concurrent browser pages
    retry_attempts: int = 3
    retry_delay: int = 2000  # Milliseconds between retries


class OutputConfig(BaseModel):
    """Output and export settings."""
    output_dir: str = "./outputs"
    default_format: str = "csv"  # csv, json, both
    include_summary: bool = True
    pretty_json: bool = True
    generate_report: bool = True


class FilterConfig(BaseModel):
    """Data filtering and selection settings."""
    max_prs: Optional[int] = None
    include_drafts: bool = True
    include_closed: bool = True
    include_merged: bool = True
    repositories: List[str] = []
    exclude_repositories: List[str] = []
    labels_filter: List[str] = []  # Only PRs with these labels
    exclude_labels: List[str] = []  # Exclude PRs with these labels


class AppConfig(BaseModel):
    """Main application configuration."""
    github: GitHubConfig = GitHubConfig()  # Default config
    scraping: ScrapingConfig = ScrapingConfig()
    output: OutputConfig = OutputConfig()
    filters: FilterConfig = FilterConfig()
    
    # Logging
    log_level: str = "INFO"
    log_file: Optional[str] = None


class ConfigManager:
    """Manage application configuration from multiple sources."""
    
    def __init__(self, config_file: Optional[str] = None):
        """Initialize config manager."""
        self.config_file = config_file
        self.config: Optional[AppConfig] = None
        
        # Load environment variables
        load_dotenv()
    
    def load_config(self) -> AppConfig:
        """Load configuration from multiple sources."""
        config_data = {}
        
        # 1. Load from YAML config file if provided
        if self.config_file and Path(self.config_file).exists():
            config_data = self._load_from_yaml(self.config_file)
            logger.info(f"Loaded configuration from {self.config_file}")
        
        # 2. Override with environment variables
        env_config = self._load_from_env()
        config_data = self._deep_merge(config_data, env_config)
        
        # 3. Validate and create config object
        try:
            self.config = AppConfig(**config_data)
            logger.info("Configuration loaded successfully")
            return self.config
        except Exception as e:
            logger.error(f"Configuration validation failed: {e}")
            raise ValueError(f"Invalid configuration: {e}")
    
    def _load_from_yaml(self, config_file: str) -> dict:
        """Load configuration from YAML file."""
        try:
            with open(config_file, 'r') as f:
                return yaml.safe_load(f) or {}
        except Exception as e:
            logger.warning(f"Failed to load YAML config from {config_file}: {e}")
            return {}
    
    def _load_from_env(self) -> dict:
        """Load configuration from environment variables."""
        env_config = {}
        
        # GitHub settings
        github_config = {}
        if os.getenv('GITHUB_BASE_URL'):
            github_config['base_url'] = os.getenv('GITHUB_BASE_URL')
        if os.getenv('GITHUB_USE_EXISTING_SESSION'):
            github_config['use_existing_session'] = os.getenv('GITHUB_USE_EXISTING_SESSION').lower() == 'true'
        if os.getenv('GITHUB_USER_DATA_DIR'):
            github_config['browser_user_data_dir'] = os.getenv('GITHUB_USER_DATA_DIR')
        
        if github_config:
            env_config['github'] = github_config
        
        # Scraping settings
        scraping_config = {}
        if os.getenv('HEADLESS'):
            scraping_config['headless'] = os.getenv('HEADLESS').lower() == 'true'
        if os.getenv('SCRAPING_DELAY'):
            scraping_config['slow_mo'] = int(os.getenv('SCRAPING_DELAY'))
        if os.getenv('PAGE_TIMEOUT'):
            scraping_config['timeout'] = int(os.getenv('PAGE_TIMEOUT'))
        if os.getenv('CONCURRENT_PAGES'):
            scraping_config['concurrent_pages'] = int(os.getenv('CONCURRENT_PAGES'))
        
        if scraping_config:
            env_config['scraping'] = scraping_config
        
        # Output settings
        output_config = {}
        if os.getenv('DEFAULT_OUTPUT_FORMAT'):
            output_config['default_format'] = os.getenv('DEFAULT_OUTPUT_FORMAT')
        if os.getenv('DEFAULT_OUTPUT_DIR'):
            output_config['output_dir'] = os.getenv('DEFAULT_OUTPUT_DIR')
        
        if output_config:
            env_config['output'] = output_config
        
        # Logging
        if os.getenv('LOG_LEVEL'):
            env_config['log_level'] = os.getenv('LOG_LEVEL')
        if os.getenv('LOG_FILE'):
            env_config['log_file'] = os.getenv('LOG_FILE')
        
        return env_config
    
    def _deep_merge(self, base_dict: dict, override_dict: dict) -> dict:
        """Deep merge two dictionaries."""
        result = base_dict.copy()
        
        for key, value in override_dict.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._deep_merge(result[key], value)
            else:
                result[key] = value
        
        return result
    
    def create_sample_config(self, output_file: str = "config.yaml") -> None:
        """Create a sample configuration file."""
        sample_config = {
            'github': {
                'base_url': 'https://github.com',
                'use_existing_session': True,
                'browser_user_data_dir': None
            },
            'scraping': {
                'headless': True,
                'slow_mo': 1000,
                'timeout': 30000,
                'concurrent_pages': 3,
                'retry_attempts': 3,
                'retry_delay': 2000
            },
            'output': {
                'output_dir': './outputs',
                'default_format': 'csv',
                'include_summary': True,
                'pretty_json': True,
                'generate_report': True
            },
            'filters': {
                'max_prs': 100,
                'include_drafts': True,
                'include_closed': True,
                'include_merged': True,
                'repositories': [],
                'exclude_repositories': [],
                'labels_filter': [],
                'exclude_labels': ['wontfix', 'duplicate']
            },
            'log_level': 'INFO',
            'log_file': None
        }
        
        with open(output_file, 'w') as f:
            yaml.dump(sample_config, f, default_flow_style=False, indent=2)
        
        logger.info(f"Created sample configuration file: {output_file}")
    
    def setup_logging(self) -> None:
        """Setup logging based on configuration."""
        if not self.config:
            return
        
        log_level = getattr(logging, self.config.log_level.upper(), logging.INFO)
        
        # Configure logging
        logging.basicConfig(
            level=log_level,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(),
                *([logging.FileHandler(self.config.log_file)] if self.config.log_file else [])
            ]
        )
"""Configuration management for the PR Analyser."""

import os
import yaml
from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field
from dotenv import load_dotenv


class GitHubConfig(BaseModel):
    """GitHub API configuration."""
    token: Optional[str] = None


class AnalysisConfig(BaseModel):
    """Analysis configuration."""
    date_range: Dict[str, Optional[str]] = Field(default_factory=lambda: {"from": None, "to": None})
    filters: Dict[str, List[str]] = Field(default_factory=lambda: {
        "repositories": [],
        "exclude_repositories": [],
        "branches": [],
        "pr_status": []
    })


class OutputConfig(BaseModel):
    """Output configuration."""
    format: str = "csv"
    directory: str = "./reports"
    visualizations: bool = True


class RateLimitConfig(BaseModel):
    """Rate limiting configuration."""
    requests_per_hour: int = 4000


class LoggingConfig(BaseModel):
    """Logging configuration."""
    level: str = "INFO"


class Config(BaseModel):
    """Main configuration model."""
    github: GitHubConfig
    organization: Optional[str] = None
    user: Optional[str] = None
    analysis: AnalysisConfig = Field(default_factory=AnalysisConfig)
    output: OutputConfig = Field(default_factory=OutputConfig)
    rate_limiting: RateLimitConfig = Field(default_factory=RateLimitConfig)
    logging: LoggingConfig = Field(default_factory=LoggingConfig)


def load_config(config_path: Optional[str] = None) -> Config:
    """Load configuration from file and environment variables."""
    # Load environment variables
    load_dotenv()
    
    # Default configuration
    config_data = {
        "github": {"token": os.getenv("GITHUB_TOKEN")},
        "organization": os.getenv("GITHUB_ORG"),
        "user": os.getenv("GITHUB_USER"),
    }
    
    # Load from config file if provided
    if config_path and os.path.exists(config_path):
        with open(config_path, 'r') as f:
            file_config = yaml.safe_load(f)
            # Merge file config with defaults
            config_data.update(file_config)
    
    # Substitute environment variables in the config
    config_data = substitute_env_vars(config_data)
    
    return Config(**config_data)


def substitute_env_vars(data: Any) -> Any:
    """Recursively substitute environment variables in config data."""
    if isinstance(data, dict):
        return {key: substitute_env_vars(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [substitute_env_vars(item) for item in data]
    elif isinstance(data, str) and data.startswith("${") and data.endswith("}"):
        env_var = data[2:-1]
        return os.getenv(env_var, data)
    else:
        return data
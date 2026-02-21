# GitHub PR Scraper

Advanced GitHub Pull Request analysis tool using web scraping to gather comprehensive metrics that aren't available through the GitHub API.

## Features

- **No Authentication Required**: Uses your existing GitHub browser session - no passwords or tokens needed
- **Comprehensive PR Metrics**: Reviews, reactions, time metrics, file changes, and more
- **Web Scraping**: Uses Playwright for reliable data extraction from GitHub web interface
- **Rich Data Export**: CSV, JSON export with detailed analytics
- **Async Processing**: Fast parallel scraping of multiple PRs
- **Flexible Configuration**: Support for filtering and custom outputs

## Quick Start

```bash
# Install dependencies
poetry install

# Install Playwright browsers
poetry run playwright install

# Make sure you're logged into GitHub in your browser first!

# Create configuration
poetry run github-pr-scraper init-config

# Run analysis
poetry run github-pr-scraper --config config.yaml analyze --user your-username --org organization-name --from 2023-01-01
```

## Prerequisites

**Important**: You must be logged into GitHub in your web browser before running the scraper. The tool uses your existing browser session, so:

1. Open your web browser
2. Go to GitHub.com and login
3. Keep the browser open while running the scraper
4. The scraper will detect and use your active session

## Configuration

Create a `config.yaml` file:

```yaml
github:
  base_url: https://github.com
  use_existing_session: true
  browser_user_data_dir: null  # Optional: custom browser profile

scraping:
  headless: false  # Set to true for background operation
  slow_mo: 1000
  timeout: 30000
  concurrent_pages: 3

output:
  output_dir: ./outputs
  default_format: csv
  include_summary: true
  generate_report: true
```

## Data Points Collected

### Basic PR Information
- Repository, number, title, description
- State, creation/merge/close dates
- Author information
- Branch details

### Advanced Metrics
- **Review Data**: Number of reviewers, review comments, approval count
- **Time Metrics**: Time to first review, time to merge, review cycles
- **File Analysis**: Changed files count, file types, programming languages
- **Engagement**: Reactions (👍, 🎉, ❤️), discussion threads
- **Labels & Context**: PR labels, linked issues, milestones
- **Code Changes**: Additions/deletions breakdown by file type

### Collaboration Insights
- Co-authors and collaborators
- Review participation patterns
- Cross-repository contribution analysis

## Usage Examples

```bash
# Basic analysis (make sure you're logged into GitHub in your browser first)
github-pr-scraper --config config.yaml analyze --user jeremychia --org vinted

# Date range filtering  
github-pr-scraper --config config.yaml analyze --user jeremychia --org vinted --from 2023-08-01 --to 2024-02-01

# Specific repositories
github-pr-scraper --config config.yaml analyze --user jeremychia --repos repo1,repo2,repo3

# Quick recent analysis
github-pr-scraper --config config.yaml quick-analysis --user jeremychia --days 30

# Export formats
github-pr-scraper --config config.yaml analyze --user jeremychia --org vinted --output-dir ./my-analysis --format both
```

## How It Works

1. **Session Detection**: The scraper launches a browser and checks if you're logged into GitHub
2. **Search & Discovery**: Uses GitHub's search interface to find your PRs based on criteria
3. **Data Extraction**: Visits each PR page and extracts comprehensive metrics
4. **Processing**: Analyzes and processes the data for insights
5. **Export**: Generates CSV files, JSON data, and analysis reports

## Troubleshooting

**"Not logged into GitHub" Error**:
- Make sure you're logged into GitHub in your default browser
- Try opening GitHub.com in your browser and verifying you're logged in
- If using Chrome profiles, you may need to set `browser_user_data_dir` in config

**Browser Issues**:
- Set `headless: false` in config to see what's happening
- Increase `timeout` values if pages load slowly
- Reduce `concurrent_pages` if hitting rate limits

## Output

The tool generates rich CSV/JSON files with detailed metrics for further analysis in tools like Excel, Python pandas, or visualization platforms.

## Requirements

- Python 3.10+
- Playwright (browsers auto-installed)
- **Active GitHub session in your browser** (no credentials needed!)

## Privacy & Security

- **No credential storage**: Uses your existing browser session
- **Local processing**: All data processing happens on your machine  
- **No data transmission**: Your PR data stays on your computer
- **Open source**: Full transparency of what data is collected
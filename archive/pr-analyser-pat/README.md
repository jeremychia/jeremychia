# GitHub PR and Commit Analysis Tool

A comprehensive tool to analyze GitHub Pull Requests and commits, providing insights into contribution patterns and productivity trends with **secure interactive authentication**.

## Features

- 🔐 **Secure Authentication**: Interactive token setup with system keychain storage
- 📊 **Comprehensive Analysis**: Analyze PRs and commits for users within GitHub organizations
- 📈 **Rich Visualizations**: Generate detailed contribution metrics and visualizations
- 📤 **Multiple Export Formats**: Export data in CSV, JSON, and Markdown formats
- ⏰ **Time-based Analysis**: Flexible date range filtering and trend visualization
- 🤝 **Collaboration Insights**: Review patterns and code quality indicators
- 🎨 **Beautiful CLI**: Rich terminal interface with progress bars and colored output

## Quick Start

### 1. Install Dependencies
```bash
# Clone the repository
git clone <repository-url>
cd pr-analyser

# Install dependencies with Poetry
poetry install
```

### 2. Interactive Authentication Setup
```bash
# First time setup - will prompt for GitHub token
poetry run pr-analyser init --user jeremychia --org vinted

# Or analyze directly (will prompt for auth if needed)
poetry run pr-analyser analyze --user jeremychia --org vinted --from 2023-08-01
```

### 3. Run Analysis
```bash
# Basic analysis
poetry run pr-analyser analyze --user jeremychia --from 2023-08-01

# With organization and full export
poetry run pr-analyser analyze --user jeremychia --org vinted --from 2023-08-01 \
  --export csv json markdown --visualize
```

## Authentication

**No more environment variables!** The tool now uses secure interactive authentication:

- 🔒 **Secure Storage**: Tokens stored in system keychain (macOS Keychain, Windows Credential Manager)
- 🌐 **Browser Integration**: Automatically opens GitHub token creation page
- ✅ **Token Validation**: Verifies token permissions before storage
- 👤 **Per-User Management**: Separate authentication for different GitHub users

### Authentication Commands

```bash
# Initialize authentication
poetry run pr-analyser init --user your-username

# Validate stored credentials  
poetry run pr-analyser validate-config --user your-username

# Force re-authentication
poetry run pr-analyser analyze --user your-username --reauth

# Remove stored credentials
poetry run pr-analyser logout --user your-username
```

## Usage Examples

### Your Specific Use Cases

```bash
# 1. Analyze jeremychia user contributions from August 2023
poetry run pr-analyser analyze --user jeremychia --from 2023-08-01 \
  --export csv json markdown --visualize

# 2. Analyze jeremychia contributions within vinted organization  
poetry run pr-analyser analyze --user jeremychia --org vinted --from 2023-08-01 \
  --export csv json markdown --visualize

# 3. Quick analysis with specific date range
poetry run pr-analyser analyze --user jeremychia --org vinted \
  --from 2023-08-01 --to 2024-12-31
```

### Additional Usage Patterns

```bash
# Analyze specific repositories only
poetry run pr-analyser analyze --user myuser --org myorg \
  --repository repo1 --repository repo2

# Exclude certain repositories  
poetry run pr-analyser analyze --user myuser --org myorg \
  --exclude-repository internal-repo

# Generate only visualizations
poetry run pr-analyser analyze --user myuser --org myorg --visualize --no-export

# Custom output directory
poetry run pr-analyser analyze --user myuser --org myorg \
  --output-dir ./my-reports --export markdown
```

## Generated Reports

The tool generates comprehensive reports including:

- **📊 Summary Metrics**: Total PRs, commits, lines of code, merge rates
- **📈 Time Series**: Contribution trends over time  
- **🏢 Repository Breakdown**: Per-repository contribution statistics
- **🤝 Collaboration Data**: Reviewer patterns, comment analysis
- **📱 Interactive Charts**: Timeline, heatmaps, distribution charts (HTML)
- **📄 Detailed Reports**: CSV data, JSON exports, Markdown summaries

## Requirements

- Python 3.10+
- GitHub Personal Access Token with repository and organization read permissions
- Access to target GitHub organizations/repositories

## License

MIT License
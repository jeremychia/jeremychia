#!/bin/bash

echo "🚀 GitHub PR Analyser - Ready to Use!"
echo "======================================"
echo ""

echo "📋 Your Specific Commands:"
echo ""

echo "1️⃣ Analyze jeremychia user (personal repositories) from August 2023:"
echo "   poetry run pr-analyser analyze --user jeremychia --from 2023-08-01 --export csv json markdown --visualize"
echo ""

echo "2️⃣ Analyze jeremychia contributions in vinted organization:"
echo "   poetry run pr-analyser analyze --user jeremychia --org vinted --from 2023-08-01 --export csv json markdown --visualize"
echo ""

echo "🔧 Setup Commands:"
echo ""

echo "🔐 First time authentication setup:"
echo "   poetry run pr-analyser init --user jeremychia"
echo ""

echo "🔐 Setup with organization:"
echo "   poetry run pr-analyser init --user jeremychia --org vinted"
echo ""

echo "✅ Validate authentication:"
echo "   poetry run pr-analyser validate-config --user jeremychia"
echo ""

echo "🔄 Force re-authentication:"
echo "   poetry run pr-analyser analyze --user jeremychia --reauth --from 2023-08-01"
echo ""

echo "🚪 Logout/remove credentials:"
echo "   poetry run pr-analyser logout --user jeremychia"
echo ""

echo "💡 What happens when you run these commands:"
echo "   1. Tool checks for stored GitHub credentials for 'jeremychia'"
echo "   2. If not found, opens browser to GitHub token creation page"
echo "   3. Prompts you to create a Personal Access Token with repo permissions"
echo "   4. Validates the token and stores it securely in macOS Keychain"
echo "   5. Fetches all PRs and commits from August 1, 2023 onwards"
echo "   6. Generates comprehensive analysis with charts and reports"
echo "   7. Exports data in CSV, JSON, and Markdown formats"
echo "   8. Creates interactive HTML visualizations"
echo ""

echo "📁 Output will be saved to: ./reports/"
echo "   - pull_requests_jeremychia.csv"
echo "   - commits_jeremychia.csv"
echo "   - analysis_jeremychia.json"
echo "   - report_jeremychia.md"
echo "   - timeline_W.html (weekly timeline chart)"
echo "   - repository_breakdown.html"
echo "   - pr_status_distribution.html"
echo "   - contribution_heatmap.html"
echo "   - pr_size_distribution.html"
echo ""

echo "🔒 Security Features:"
echo "   ✅ No tokens in config files or environment variables"
echo "   ✅ Secure storage in macOS Keychain"
echo "   ✅ Token validation before storage"
echo "   ✅ Per-user credential management"
echo ""

echo "Ready to analyze your GitHub contributions! 🎉"
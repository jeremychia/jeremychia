#!/bin/bash

# Example usage commands for the PR Analyser with interactive authentication

echo "=== PR Analyser - Interactive Authentication Demo ==="
echo ""

echo "1. Analyze jeremychia user contributions:"
echo "   poetry run pr-analyser analyze --user jeremychia --from 2023-08-01 --export csv json markdown --visualize"
echo ""

echo "2. Analyze contributions within vinted organization:"
echo "   poetry run pr-analyser analyze --user jeremychia --org vinted --from 2023-08-01 --export csv json markdown --visualize"
echo ""

echo "3. Initialize authentication (first time setup):"
echo "   poetry run pr-analyser init --user jeremychia --org vinted"
echo ""

echo "4. Validate stored credentials:"
echo "   poetry run pr-analyser validate-config --user jeremychia"
echo ""

echo "5. Force re-authentication:"
echo "   poetry run pr-analyser analyze --user jeremychia --org vinted --reauth --from 2023-08-01"
echo ""

echo "6. Remove stored credentials:"
echo "   poetry run pr-analyser logout --user jeremychia"
echo ""

echo "=== Key Features ==="
echo "✅ Secure credential storage using system keychain"
echo "✅ Interactive token setup with browser integration"  
echo "✅ Token validation and user verification"
echo "✅ No more environment variables needed"
echo "✅ Per-user authentication management"
echo ""

echo "=== Security Benefits ==="
echo "🔒 Tokens stored securely in system keychain (macOS Keychain, Windows Credential Manager, etc.)"
echo "🔒 No plaintext tokens in config files"
echo "🔒 Token validation before storage"
echo "🔒 User-specific credential isolation"
echo ""

echo "When you run the commands above, the tool will:"
echo "1. Check for stored credentials for the specified user"
echo "2. If none found, prompt for GitHub Personal Access Token"
echo "3. Open browser to GitHub token creation page"
echo "4. Validate the token and store it securely"
echo "5. Proceed with analysis using authenticated API calls"
#!/usr/bin/env python3
"""
Enhanced PR Data Script - Fixed Version
Extracts detailed PR information using GitHub CLI for all PRs in the CSV.
"""

import csv
import json
import subprocess
import logging
from datetime import datetime
from urllib.parse import urlparse
import re

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_repo_from_url(url):
    """Extract owner/repo from GitHub URL."""
    # Parse URL like https://github.com/vinted/dataverse-vintedgo-dbt/pull/7200
    match = re.match(r'https://github\.com/([^/]+)/([^/]+)/pull/\d+', url)
    if match:
        owner, repo = match.groups()
        return f"{owner}/{repo}"
    return None

def get_pr_details(owner_repo, pr_number):
    """Get detailed PR information using GitHub CLI."""
    try:
        cmd = [
            'gh', 'pr', 'view', str(pr_number), 
            '--repo', owner_repo,
            '--json', 
            'number,title,body,author,state,createdAt,updatedAt,mergedAt,closedAt,'
            'additions,deletions,url,headRefName,baseRefName,labels,milestone,'
            'assignees,reviewRequests,reviews,comments,commits,files,reactionGroups'
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            return json.loads(result.stdout)
        else:
            logger.warning(f"Failed to get details for {owner_repo}#{pr_number}: {result.stderr.strip()}")
            return None
            
    except subprocess.TimeoutExpired:
        logger.warning(f"Timeout getting details for {owner_repo}#{pr_number}")
        return None
    except Exception as e:
        logger.warning(f"Error getting details for {owner_repo}#{pr_number}: {str(e)}")
        return None

def enhance_pr_data(input_csv, output_prefix):
    """Process CSV and enhance each PR with detailed information."""
    
    enhanced_prs = []
    
    with open(input_csv, 'r') as f:
        reader = csv.DictReader(f)
        
        for idx, row in enumerate(reader, 1):
            # Extract repository info from URL
            owner_repo = extract_repo_from_url(row['URL'])
            pr_number = row['PR #']
            
            if not owner_repo:
                logger.warning(f"Could not extract repository from URL: {row['URL']}")
                continue
            
            logger.info(f"Processing PR {idx}: {owner_repo}#{pr_number}")
            
            pr_details = get_pr_details(owner_repo, pr_number)
            
            if pr_details:
                # Create enhanced PR record
                enhanced_pr = {
                    # Basic info
                    'repository': owner_repo,
                    'pr_number': pr_number,
                    'title': pr_details.get('title', ''),
                    'description': pr_details.get('body', ''),
                    'author': pr_details.get('author', {}).get('login', '') if pr_details.get('author') else '',
                    
                    # States and dates
                    'current_state': pr_details.get('state', ''),
                    'original_state': row['State'],
                    'created_at_iso': pr_details.get('createdAt', ''),
                    'created_at': row['Created At'],
                    'updated_at_iso': pr_details.get('updatedAt', ''),
                    'merged_at_iso': pr_details.get('mergedAt', ''),
                    'merged_at': row.get('Merged At', ''),
                    'closed_at_iso': pr_details.get('closedAt', ''),
                    'closed_at': row.get('Closed At', ''),
                    
                    # Branch info
                    'head_branch': pr_details.get('headRefName', ''),
                    'base_branch': pr_details.get('baseRefName', ''),
                    
                    # Labels and assignees  
                    'labels': [label.get('name', '') for label in pr_details.get('labels', [])],
                    'milestone': pr_details.get('milestone', {}).get('title', '') if pr_details.get('milestone') else '',
                    'assignees': [assignee.get('login', '') for assignee in pr_details.get('assignees', [])],
                    
                    # Code metrics
                    'original_additions': int(row.get('Additions', 0)) if row.get('Additions', '').isdigit() else 0,
                    'original_deletions': int(row.get('Deletions', 0)) if row.get('Deletions', '').isdigit() else 0,
                    'net_lines': int(row.get('Net Lines', 0)) if row.get('Net Lines', '').replace('-', '').isdigit() else 0,
                    'gh_additions': pr_details.get('additions', 0),
                    'gh_deletions': pr_details.get('deletions', 0),
                    
                    # Review and engagement metrics
                    'reviews_count': len(pr_details.get('reviews', [])),
                    'comments_count': len(pr_details.get('comments', [])),
                    'commits_count': len(pr_details.get('commits', [])),
                    'files_changed': len(pr_details.get('files', [])),
                    
                    # Detailed data
                    'reviews': pr_details.get('reviews', []),
                    'comments': pr_details.get('comments', []),
                    'commits': pr_details.get('commits', []),
                    'files': pr_details.get('files', []),
                    'reactionGroups': pr_details.get('reactionGroups', []),
                    
                    # URL
                    'url': row['URL']
                }
                
                # Calculate time to merge if available
                if pr_details.get('createdAt') and pr_details.get('mergedAt'):
                    created = datetime.fromisoformat(pr_details['createdAt'].replace('Z', '+00:00'))
                    merged = datetime.fromisoformat(pr_details['mergedAt'].replace('Z', '+00:00'))
                    enhanced_pr['time_to_merge_hours'] = (merged - created).total_seconds() / 3600
                
                # Review metrics
                reviews = pr_details.get('reviews', [])
                enhanced_pr['approvals_count'] = len([r for r in reviews if r.get('state') == 'APPROVED'])
                enhanced_pr['changes_requested_count'] = len([r for r in reviews if r.get('state') == 'CHANGES_REQUESTED'])
                enhanced_pr['unique_reviewers'] = list(set([r.get('author', {}).get('login', '') for r in reviews if r.get('author')]))
                
                enhanced_prs.append(enhanced_pr)
            
            else:
                # Keep original data even if enhancement failed
                enhanced_pr = {
                    'repository': owner_repo,
                    'pr_number': pr_number,
                    'title': row['Title'],
                    'original_state': row['State'],
                    'created_at': row['Created At'],
                    'merged_at': row.get('Merged At', ''),
                    'closed_at': row.get('Closed At', ''),
                    'original_additions': int(row.get('Additions', 0)) if row.get('Additions', '').isdigit() else 0,
                    'original_deletions': int(row.get('Deletions', 0)) if row.get('Deletions', '').isdigit() else 0,
                    'net_lines': int(row.get('Net Lines', 0)) if row.get('Net Lines', '').replace('-', '').isdigit() else 0,
                    'url': row['URL'],
                    'description': '',
                    'enhancement_failed': True
                }
                enhanced_prs.append(enhanced_pr)
    
    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_output = f"{output_prefix}_{timestamp}.json"
    
    with open(json_output, 'w') as f:
        json.dump({
            'metadata': {
                'total_prs': len(enhanced_prs),
                'enhanced_timestamp': datetime.now().isoformat(),
                'source_file': input_csv
            },
            'prs': enhanced_prs
        }, f, indent=2, default=str)
    
    logger.info(f"Saved enhanced JSON data: {json_output}")
    
    # Save as CSV for easy viewing
    csv_output = f"{output_prefix}_{timestamp}.csv"
    if enhanced_prs:
        # Flatten the data for CSV
        csv_data = []
        for pr in enhanced_prs:
            flat_pr = {
                'repository': pr.get('repository', ''),
                'pr_number': pr.get('pr_number', ''),
                'title': pr.get('title', ''),
                'description_length': len(pr.get('description', '')),
                'description_preview': pr.get('description', '')[:200] + '...' if len(pr.get('description', '')) > 200 else pr.get('description', ''),
                'author': pr.get('author', ''),
                'state': pr.get('current_state', pr.get('original_state', '')),
                'created_at': pr.get('created_at_iso', pr.get('created_at', '')),
                'merged_at': pr.get('merged_at_iso', pr.get('merged_at', '')),
                'closed_at': pr.get('closed_at_iso', pr.get('closed_at', '')),
                'time_to_merge_hours': pr.get('time_to_merge_hours', ''),
                'head_branch': pr.get('head_branch', ''),
                'base_branch': pr.get('base_branch', ''),
                'labels': '|'.join(pr.get('labels', [])),
                'milestone': pr.get('milestone', ''),
                'assignees': '|'.join(pr.get('assignees', [])),
                'reviews_count': pr.get('reviews_count', 0),
                'approvals_count': pr.get('approvals_count', 0),
                'changes_requested_count': pr.get('changes_requested_count', 0),
                'unique_reviewers': '|'.join(pr.get('unique_reviewers', [])),
                'comments_count': pr.get('comments_count', 0),
                'commits_count': pr.get('commits_count', 0),
                'files_changed': pr.get('files_changed', 0),
                'total_reactions': sum([rg.get('totalCount', 0) for rg in pr.get('reactionGroups', [])]),
                'additions': pr.get('original_additions', 0),
                'deletions': pr.get('original_deletions', 0),
                'net_lines': pr.get('net_lines', 0),
                'url': pr.get('url', ''),
                'enhancement_failed': pr.get('enhancement_failed', False)
            }
            csv_data.append(flat_pr)
        
        with open(csv_output, 'w', newline='') as f:
            if csv_data:
                writer = csv.DictWriter(f, fieldnames=csv_data[0].keys())
                writer.writeheader()
                writer.writerows(csv_data)
    
    logger.info(f"Saved enhanced CSV data: {csv_output}")
    logger.info(f"Enhanced {len(enhanced_prs)} PRs total")

if __name__ == "__main__":
    input_csv = "../pr-analyser-csv/jeremychia_pr_contributions.csv"
    enhance_pr_data(input_csv, "enhanced_pr_data")
#!/usr/bin/env python3
"""
Script to update PR analysis using fresh GitHub CLI data
Processes the comprehensive PR dataset and generates updated analysis
"""

import json
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
import sys
from pathlib import Path

def load_gh_cli_data(json_path):
    """Load and process GitHub CLI JSON data"""
    print(f"Loading data from: {json_path}")
    
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    return data

def process_pr_data(pr_data):
    """Process PR data into structured format for analysis"""
    processed_prs = []
    
    for pr in pr_data:
        # Extract repository information
        repo_info = pr.get('repository', {})
        repo_name = repo_info.get('name', 'unknown')
        repo_owner = repo_info.get('nameWithOwner', 'unknown')
        
        # Process dates
        created_at = pd.to_datetime(pr.get('createdAt'))
        updated_at = pd.to_datetime(pr.get('updatedAt'))
        closed_at = pd.to_datetime(pr.get('closedAt')) if pr.get('closedAt') else None
        
        # Extract labels
        labels = [label.get('name', '') for label in pr.get('labels', [])]
        
        # Calculate metrics
        now = pd.Timestamp.now(tz='UTC')
        days_open = (closed_at - created_at).days if closed_at else (now - created_at).days
        
        processed_pr = {
            'pr_number': pr.get('number'),
            'title': pr.get('title'),
            'repository': repo_name,
            'repository_full': repo_owner,
            'state': pr.get('state'),
            'author': pr.get('author', {}).get('login', 'unknown'),
            'created_at': created_at,
            'updated_at': updated_at,
            'closed_at': closed_at,
            'comments_count': pr.get('commentsCount', 0),
            'labels': ', '.join(labels),
            'label_count': len(labels),
            'days_open': days_open,
            'url': pr.get('url'),
            'body_length': len(pr.get('body', '')),
            'year_month': created_at.strftime('%Y-%m'),
            'year': created_at.year,
            'month': created_at.month,
            'quarter': f"Q{created_at.quarter} {created_at.year}",
            'is_merged': pr.get('state') == 'merged',
            'is_closed': pr.get('state') == 'closed',
            'is_open': pr.get('state') == 'open',
        }
        
        processed_prs.append(processed_pr)
    
    return pd.DataFrame(processed_prs)

def generate_analysis_summary(df):
    """Generate comprehensive analysis summary"""
    
    total_prs = len(df)
    
    summary = {
        'analysis_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'total_prs': total_prs,
        'merged_prs': len(df[df['is_merged']]),
        'closed_prs': len(df[df['is_closed']]),
        'open_prs': len(df[df['is_open']]),
        'date_range': {
            'earliest': df['created_at'].min().strftime('%Y-%m-%d'),
            'latest': df['created_at'].max().strftime('%Y-%m-%d'),
        },
        'repositories': df['repository'].value_counts().head(10).to_dict(),
        'top_labels': df['labels'].str.split(', ').explode().value_counts().head(10).to_dict(),
        'monthly_activity': df.groupby('year_month').size().tail(12).to_dict(),
        'avg_comments_per_pr': df['comments_count'].mean(),
        'avg_days_open': df['days_open'].mean(),
        'merge_rate': (len(df[df['is_merged']]) / total_prs * 100) if total_prs > 0 else 0,
    }
    
    return summary

def create_achievement_bullets(df, summary):
    """Create professional achievement bullet points"""
    
    bullets = []
    
    # Overall contribution stats
    bullets.append(f"📊 **GitHub Contributions Overview**")
    bullets.append(f"   • Authored **{summary['total_prs']:,} pull requests** across {len(df['repository'].unique())} repositories")
    bullets.append(f"   • Achieved **{summary['merge_rate']:.1f}% merge rate** with {summary['merged_prs']:,} successful merges")
    
    # Recent activity
    cutoff_date = pd.Timestamp.now(tz='UTC') - pd.Timedelta(days=90)
    recent_3months = df[df['created_at'] > cutoff_date]
    if len(recent_3months) > 0:
        bullets.append(f"   • Maintained high velocity with **{len(recent_3months)} PRs** in last 3 months")
    
    # Repository contributions
    top_repos = df['repository'].value_counts().head(5)
    bullets.append(f"\n🏗️ **Key Repository Contributions**")
    for repo, count in top_repos.items():
        bullets.append(f"   • **{repo}**: {count} PRs ({count/summary['total_prs']*100:.1f}% of total contributions)")
    
    # Collaboration metrics
    if summary['avg_comments_per_pr'] > 0:
        bullets.append(f"\n💬 **Collaboration & Code Quality**")
        bullets.append(f"   • Engaged in **{summary['avg_comments_per_pr']:.1f} comments per PR** on average")
        bullets.append(f"   • Average PR lifecycle of **{summary['avg_days_open']:.1f} days** from creation to closure")
    
    # Recent trends
    bullets.append(f"\n📈 **Recent Activity Trends**")
    recent_months = list(summary['monthly_activity'].items())[-6:]
    for month, count in recent_months:
        bullets.append(f"   • **{month}**: {count} PRs")
    
    # Label analysis (technology/domain focus)
    if 'top_labels' in summary and summary['top_labels']:
        bullets.append(f"\n🏷️ **Technical Focus Areas**")
        for label, count in list(summary['top_labels'].items())[:5]:
            if label and label != '':
                bullets.append(f"   • **{label}**: {count} PRs")
    
    return '\n'.join(bullets)

def main():
    # Determine paths
    base_dir = Path(__file__).parent.parent
    
    # Find the most recent merged JSON file (prioritize merged files)
    merged_files = list(base_dir.glob('complete_prs_merged_*.json'))
    if merged_files:
        latest_json = max(merged_files, key=lambda x: x.stat().st_mtime)
        print(f"📁 Using latest merged data file: {latest_json.name}")
    else:
        # Fallback to comprehensive files
        json_files = list(base_dir.glob('comprehensive_prs_*.json'))
        if not json_files:
            print("❌ No PR JSON files found!")
            sys.exit(1)
        latest_json = max(json_files, key=lambda x: x.stat().st_mtime)
        print(f"📁 Using latest data file: {latest_json.name}")
    
    # Load and process data
    pr_data = load_gh_cli_data(latest_json)
    print(f"📊 Loaded {len(pr_data)} PRs from GitHub CLI")
    
    # Process into DataFrame
    df = process_pr_data(pr_data)
    print(f"✅ Processed {len(df)} PRs successfully")
    
    # Generate analysis
    summary = generate_analysis_summary(df)
    print(f"📈 Analysis complete - {summary['total_prs']} total PRs analyzed")
    
    # Create achievement bullets
    bullets = create_achievement_bullets(df, summary)
    
    # Save outputs  
    output_files = {
        'csv': base_dir / 'github_pr_analysis.csv',
        'json': base_dir / 'performance_data.json', 
        'bullets': base_dir / 'achievement_bullets.txt',
        'summary': base_dir / 'professional_achievements.md'
    }
    
    # Save CSV
    df.to_csv(output_files['csv'], index=False)
    print(f"💾 Saved CSV: {output_files['csv'].name}")
    
    # Save JSON performance data
    with open(output_files['json'], 'w') as f:
        json.dump(summary, f, indent=2, default=str)
    print(f"💾 Saved performance data: {output_files['json'].name}")
    
    # Save achievement bullets
    with open(output_files['bullets'], 'w') as f:
        f.write(bullets)
    print(f"💾 Saved achievement bullets: {output_files['bullets'].name}")
    
    # Create professional achievements markdown
    markdown_content = f"""# GitHub Contributions Analysis
*Generated: {summary['analysis_date']}*

{bullets}

## 📋 Technical Summary

| Metric | Value |
|--------|-------|
| Total PRs | {summary['total_prs']:,} |
| Merge Rate | {summary['merge_rate']:.1f}% |
| Repositories | {len(df['repository'].unique())} |
| Date Range | {summary['date_range']['earliest']} to {summary['date_range']['latest']} |
| Avg Comments/PR | {summary['avg_comments_per_pr']:.1f} |
| Avg Days Open | {summary['avg_days_open']:.1f} |

## 🔥 Recent Activity (Last 6 Months)

"""
    
    for month, count in list(summary['monthly_activity'].items())[-6:]:
        markdown_content += f"- **{month}**: {count} PRs\n"
    
    markdown_content += """
---
*This analysis is automatically generated from GitHub CLI data and updated regularly to reflect the most current contribution patterns.*
"""
    
    with open(output_files['summary'], 'w') as f:
        f.write(markdown_content)
    print(f"💾 Saved professional summary: {output_files['summary'].name}")
    
    # Print summary to console
    print(f"\n🎉 Analysis Complete!")
    print(f"📊 **Total PRs**: {summary['total_prs']:,}")
    print(f"✅ **Merge Rate**: {summary['merge_rate']:.1f}%")
    print(f"📅 **Date Range**: {summary['date_range']['earliest']} to {summary['date_range']['latest']}")
    print(f"🏢 **Repositories**: {len(df['repository'].unique())}")
    
    print(f"\n📁 **Files Generated**:")
    for file_type, file_path in output_files.items():
        print(f"   • {file_type.upper()}: {file_path.name}")

if __name__ == "__main__":
    main()
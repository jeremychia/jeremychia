#!/usr/bin/env python3
"""
GitHub PR Analysis Generator - CSV Input Version
Regenerates analysis from existing CSV data file
"""

import pandas as pd
import json
from datetime import datetime
from pathlib import Path

def load_csv_data(csv_path):
    """Load PR data from CSV file"""
    try:
        df = pd.read_csv(csv_path)
        
        # Convert date columns
        date_columns = ['created_at', 'updated_at', 'closed_at']
        for col in date_columns:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], utc=True)
        
        print(f"📊 Loaded {len(df)} PRs from CSV")
        return df
    except Exception as e:
        print(f"❌ Error loading CSV: {e}")
        return None

def generate_analysis_summary(df):
    """Generate comprehensive analysis summary"""
    
    total_prs = len(df)
    
    # Determine merged PRs (could be 'merged' or 'MERGED' state)
    merged_prs = len(df[df['state'].str.lower() == 'merged'])
    closed_prs = len(df[df['state'].str.lower() == 'closed']) 
    open_prs = len(df[df['state'].str.lower() == 'open'])
    
    summary = {
        'analysis_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'total_prs': total_prs,
        'merged_prs': merged_prs,
        'closed_prs': closed_prs, 
        'open_prs': open_prs,
        'date_range': {
            'earliest': df['created_at'].min().strftime('%Y-%m-%d'),
            'latest': df['created_at'].max().strftime('%Y-%m-%d'),
        },
        'repositories': df['repository'].value_counts().head(10).to_dict(),
        'repository_count': len(df['repository'].unique()),
        'avg_comments_per_pr': df['comments_count'].mean() if 'comments_count' in df.columns else 0,
        'avg_days_open': abs(df['days_open'].mean()) if 'days_open' in df.columns and df['days_open'].notna().any() else 0,
        'merge_rate': (merged_prs / total_prs * 100) if total_prs > 0 else 0,
    }
    
    # Add monthly activity if we have the data
    if 'year_month' in df.columns:
        summary['monthly_activity'] = df['year_month'].value_counts().sort_index().tail(12).to_dict()
    else:
        # Create year_month from created_at
        df['year_month'] = df['created_at'].dt.strftime('%Y-%m')
        summary['monthly_activity'] = df['year_month'].value_counts().sort_index().tail(12).to_dict()
    
    # Add labels analysis if available
    if 'labels' in df.columns:
        all_labels = df['labels'].fillna('').str.split(', ').explode()
        summary['top_labels'] = all_labels[all_labels != ''].value_counts().head(10).to_dict()
    
    return summary

def create_achievement_bullets(df, summary):
    """Create professional achievement bullet points"""
    
    bullets = []
    
    # Overall contribution stats
    bullets.append(f"📊 **GitHub Contributions Overview**")
    bullets.append(f"   • Authored **{summary['total_prs']:,} pull requests** across {len(df['repository'].unique())} repositories")
    bullets.append(f"   • Achieved **{summary['merge_rate']:.1f}% merge rate** with {summary['merged_prs']:,} successful merges")
    
    # Time range
    date_range_days = (df['created_at'].max() - df['created_at'].min()).days
    bullets.append(f"   • Sustained contributions over **{date_range_days} days** ({summary['date_range']['earliest']} to {summary['date_range']['latest']})")
    
    # Repository contributions
    top_repos = df['repository'].value_counts().head(5)
    bullets.append(f"\n🏗️ **Key Repository Contributions**")
    for repo, count in top_repos.items():
        bullets.append(f"   • **{repo}**: {count} PRs ({count/summary['total_prs']*100:.1f}% of total)")
    
    # Collaboration metrics
    if summary['avg_comments_per_pr'] > 0:
        bullets.append(f"\n💬 **Collaboration & Code Quality**")
        bullets.append(f"   • Engaged in **{summary['avg_comments_per_pr']:.1f} comments per PR** on average") 
        if summary['avg_days_open'] > 0:
            bullets.append(f"   • Average PR lifecycle of **{summary['avg_days_open']:.1f} days** from creation to closure")
    
    # Recent trends
    bullets.append(f"\n📈 **Recent Activity Pattern**")
    recent_months = list(summary['monthly_activity'].items())[-6:]
    for month, count in recent_months:
        bullets.append(f"   • **{month}**: {count} PRs")
    
    # Technical focus areas
    if 'top_labels' in summary and summary['top_labels']:
        bullets.append(f"\n🏷️ **Technical Focus Areas**")
        for label, count in list(summary['top_labels'].items())[:5]:
            if label and label != '':
                bullets.append(f"   • **{label}**: {count} PRs")
    
    return '\n'.join(bullets)

def create_professional_markdown(summary, bullets):
    """Create comprehensive professional achievements markdown"""
    
    markdown_content = f"""# GitHub Contributions Analysis
*Generated: {summary['analysis_date']}*

{bullets}

## 📋 Technical Summary

| Metric | Value |
|--------|-------|
| Total PRs | {summary['total_prs']:,} |
| Merge Rate | {summary['merge_rate']:.1f}% |
| Repositories | {summary['repository_count']} |
| Date Range | {summary['date_range']['earliest']} to {summary['date_range']['latest']} |
| Avg Comments/PR | {summary['avg_comments_per_pr']:.1f} |
| Avg Days Open | {summary['avg_days_open']:.1f} |

## 🔥 Recent Activity (Last 6 Months)

"""
    
    for month, count in list(summary['monthly_activity'].items())[-6:]:
        markdown_content += f"- **{month}**: {count} PRs\n"
    
    markdown_content += """
---
*This analysis is automatically generated and reflects comprehensive GitHub contribution patterns.*
"""
    
    return markdown_content

def main():
    # Determine paths
    base_dir = Path(__file__).parent.parent
    csv_path = base_dir / 'github_pr_analysis.csv'
    
    if not csv_path.exists():
        print(f"❌ CSV file not found: {csv_path}")
        return
    
    # Load data from CSV
    df = load_csv_data(csv_path)
    if df is None:
        return
    
    print(f"✅ Loaded {len(df)} PRs from CSV")
    
    # Generate analysis
    summary = generate_analysis_summary(df)
    print(f"📈 Analysis complete - {summary['total_prs']} total PRs analyzed")
    
    # Create achievement bullets
    bullets = create_achievement_bullets(df, summary)
    
    # Create professional markdown
    professional_md = create_professional_markdown(summary, bullets)
    
    # Save outputs
    output_files = {
        'json': base_dir / 'performance_data.json',
        'bullets': base_dir / 'achievement_bullets.txt',
        'summary': base_dir / 'professional_achievements.md'
    }
    
    # Save performance data JSON
    with open(output_files['json'], 'w') as f:
        json.dump(summary, f, indent=2, default=str)
    print(f"💾 Updated performance data: {output_files['json'].name}")
    
    # Save achievement bullets 
    with open(output_files['bullets'], 'w') as f:
        f.write(bullets)
    print(f"💾 Updated achievement bullets: {output_files['bullets'].name}")
    
    # Save professional summary
    with open(output_files['summary'], 'w') as f:
        f.write(professional_md)
    print(f"💾 Updated professional summary: {output_files['summary'].name}")
    
    # Print summary
    print(f"\\n🎉 Analysis Refreshed!")
    print(f"📊 **Total PRs**: {summary['total_prs']:,}")
    print(f"✅ **Merge Rate**: {summary['merge_rate']:.1f}%")
    print(f"📅 **Date Range**: {summary['date_range']['earliest']} to {summary['date_range']['latest']}")
    print(f"🏢 **Repositories**: {summary['repository_count']}")
    
    print(f"\n📁 **Files Updated**:")
    for file_type, file_path in output_files.items():
        print(f"   • {file_type.upper()}: {file_path.name}")

if __name__ == "__main__":
    main()
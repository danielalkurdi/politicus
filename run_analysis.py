#!/usr/bin/env python3
"""
Simple runner script for Politicus - Australian Political Sentiment Analysis
"""

import sys
import os
sys.path.append('src')

from src.political_analyzer import PoliticalAnalyzer


def main():
    """Run the complete political sentiment analysis"""
    print("🏛️  Welcome to Politicus - Australian Political Sentiment Analysis")
    print("="*65)
    
    analyzer = PoliticalAnalyzer()
    
    try:
        # Run the complete analysis
        print("Starting analysis... This may take a few minutes.")
        results = analyzer.run_complete_analysis(
            scrape_new_data=True,
            posts_per_query=50
        )
        
        # Display results
        analyzer.print_summary(results)
        
        # Save report
        report_file = analyzer.save_analysis_report(results)
        print(f"\n📄 Full report saved to: {report_file}")
        
    except Exception as e:
        print(f"\n❌ Error during analysis: {e}")
        print("Please check your configuration and try again.")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
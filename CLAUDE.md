# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Politicus is a machine learning project for analyzing Australian political sentiment from X.com (Twitter) data, categorizing results between Labour and Liberal parties.

## Project Status

**Early Development**: This project is in initial setup phase. No source code or dependencies have been established yet.

## Development Setup

This project will require:
- A programming language choice (Python recommended for ML/data science)
- Web scraping capabilities for X.com data collection
- Machine learning libraries for sentiment analysis
- Data storage solution for collected tweets and analysis results
- API access considerations for X.com

## Architecture Considerations

The project will need to handle:
1. **Data Collection**: X.com API integration or web scraping
2. **Data Processing**: Text cleaning, preprocessing for ML
3. **Sentiment Analysis**: ML model for political sentiment classification
4. **Political Classification**: Logic to categorize as Labour vs Liberal
5. **Data Storage**: Database for tweets, analysis results, and model training data
6. **Compliance**: Respect X.com ToS and rate limits

## Important Notes

- **Legal Compliance**: Ensure X.com Terms of Service compliance for data collection
- **Rate Limiting**: Implement proper rate limiting for API calls
- **Data Privacy**: Handle user data responsibly and consider privacy regulations
- **Model Training**: Will need labeled training data for political party classification
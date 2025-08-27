# Politicus

A machine learning project for analyzing Australian political sentiment from X.com (Twitter) data, focusing on Labor vs Liberal party sentiment analysis.

## Project Overview

Politicus scrapes political content from X.com, processes the data, and performs sentiment analysis to understand public sentiment toward Australia's major political parties - the Australian Labor Party (ALP) and the Liberal Party of Australia.

## Current Implementation

The project is currently implemented as a Jupyter notebook that:
- Fetches recent tweets using X.com API v2
- Filters for Australian political content
- Performs sentiment analysis using VADER sentiment analyzer
- Categorizes content by political party affiliation
- Analyzes engagement metrics (likes, retweets, replies)

## Quick Start

### Prerequisites
- Python 3.12+ (tested with 3.12)
- X.com API Bearer Token (for data collection)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd politicus
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env  # Create from template if available
# Edit .env and add your X_BEARER_TOKEN
```

### Usage

Open and run the Jupyter notebook:
```bash
jupyter notebook x_aus_political_sentiment_scrapper.ipynb
```

The notebook will:
1. Connect to X.com API using your bearer token
2. Search for Australian political content
3. Fetch and process tweets from the past 30 days
4. Perform sentiment analysis
5. Generate comparative analysis between Labor and Liberal parties

## Project Structure

```
politicus/
├── x_aus_political_sentiment_scrapper.ipynb  # Main analysis notebook
├── requirements.txt                           # Python dependencies
├── .env                                      # Environment variables (API keys)
├── .gitignore                               # Git ignore rules
├── CLAUDE.md                                # Claude Code instructions
└── README.md                                # This file
```

## Key Features

### Data Collection
- Uses X.com API v2 for reliable data access
- Searches with Australian political keywords and hashtags
- Includes engagement metrics (likes, retweets, replies, quotes)
- Handles API rate limiting automatically
- Filters out retweets to focus on original content

### Sentiment Analysis
- **VADER Sentiment**: Specialized for social media text analysis
- **Political Context**: Australian-specific political terminology
- **Party Classification**: Categorizes content as Labor or Liberal-leaning
- **Engagement Analysis**: Correlates sentiment with user engagement

### Search Queries
The system uses targeted search queries for each party:

**Labor Party**: Australian Labor Party, ALP, Anthony Albanese, @AlboMP, @AustralianLabor
**Liberal Party**: Liberal Party of Australia, LNP, Coalition Australia, Susan Ley

All queries include Australian context terms: #auspol, Australia, Australian, Canberra, Parliament

## Configuration

### Environment Variables
```bash
# Required: X.com API credentials
X_BEARER_TOKEN=your_bearer_token_here
```

### Analysis Parameters
- **Time Window**: Last 30 days (configurable)
- **Tweet Limit**: 100 tweets per query (configurable)
- **Language**: English only
- **Content**: Original posts only (no retweets)

## Dependencies

Core libraries:
- `tweepy==4.14.0` - X.com API client
- `pandas==2.1.4` - Data manipulation
- `vaderSentiment` - Sentiment analysis
- `matplotlib` - Data visualization
- `python-dotenv==1.0.0` - Environment variable management

## Analysis Output

The notebook generates:
- **Raw Data**: Tweet content, metadata, and engagement metrics
- **Sentiment Scores**: Positive, negative, neutral classifications
- **Party Analysis**: Breakdown of sentiment by political party
- **Engagement Correlation**: How sentiment relates to user engagement
- **Visualizations**: Charts showing sentiment trends and comparisons

## Important Notes

### Legal & Ethical Compliance
- Complies with X.com Terms of Service
- Only collects publicly available data
- Respects API rate limits with built-in delays
- No private user information is stored

### Data Handling
- Temporary data storage in memory during analysis
- No persistent database (respects privacy)
- Results can be exported as needed for research

### Australian Political Context
- Correctly spells "Labor" (not "Labour") for Australian Labor Party
- Focuses on federal Australian politics
- Includes relevant Australian political hashtags and terminology
- Accounts for Australian political figures and current leadership

## Development Status

This is an active research project currently in development. The current implementation provides a solid foundation for Australian political sentiment analysis with room for expansion into:
- Historical trend analysis
- Additional political parties (Greens, One Nation, etc.)
- Regional sentiment variations
- Policy-specific sentiment tracking

## Contributing

This project is designed for research and educational purposes. Contributions should maintain focus on:
- Accurate Australian political context
- Ethical data collection practices
- Robust sentiment analysis methods
- Clear documentation and reproducible results
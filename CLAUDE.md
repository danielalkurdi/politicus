# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Politicus is a machine learning project for analyzing Australian political sentiment from X.com data, categorizing results between Labour and Liberal parties. The system scrapes X.com posts about Australian politics, processes the data, and performs sentiment analysis with political party classification.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment (copy and configure)
cp .env.example .env

# Run complete analysis
python run_analysis.py
```

## Project Structure

```
src/
├── x_scraper.py          # X.com data scraping (API + web scraping)
├── data_processor.py     # Text cleaning and preprocessing
├── sentiment_analyzer.py # Sentiment analysis pipeline
└── political_analyzer.py # Main orchestrator class

config/
└── search_queries.py     # Search queries and keywords for Australian politics

data/                     # Generated data files (ignored by git)
├── political_sentiment.db # SQLite database
├── *.log                 # Log files
└── *.json               # Analysis reports

tests/                    # Test files (when implemented)
```

## Core Components

### XScraper (`src/x_scraper.py`)
- Scrapes X.com posts using official API or web scraping
- Searches for Australian political content with targeted queries
- Stores data in SQLite database with engagement metrics

### DataProcessor (`src/data_processor.py`)
- Cleans and preprocesses scraped post text
- Removes duplicates and filters for political relevance
- Extracts hashtags, mentions, and engagement features

### SentimentAnalyzer (`src/sentiment_analyzer.py`)
- Performs sentiment analysis using TextBlob + keyword matching
- Classifies posts by political party (Labor/Liberal)
- Generates comprehensive sentiment reports

### PoliticalAnalyzer (`src/political_analyzer.py`)
- Main orchestrator that coordinates all components
- Runs complete end-to-end analysis pipeline
- Generates Labour vs Liberal comparison reports

## Database Schema

**posts** table: Raw scraped post data
**processed_posts** table: Cleaned and processed data
**analysis** table: Sentiment analysis results

## Configuration

### Environment Variables (.env)
```bash
# X.com API credentials (optional - fallback to web scraping)
TWITTER_BEARER_TOKEN=your_token
TWITTER_API_KEY=your_key
TWITTER_API_SECRET=your_secret

# Database
DATABASE_PATH=data/political_sentiment.db
```

### Search Queries (`config/search_queries.py`)
- Australian political party keywords
- Policy-focused search terms
- Location-based queries
- Relevant hashtags (#AusPol, etc.)

## Usage Examples

```python
from src.political_analyzer import PoliticalAnalyzer

# Run complete analysis
analyzer = PoliticalAnalyzer()
results = analyzer.run_complete_analysis(
    scrape_new_data=True,
    posts_per_query=50
)

# Get Labour vs Liberal comparison
comparison = analyzer.analyze_labour_vs_liberal()
```

## Output

The system generates:
- **Sentiment analysis**: Positive/negative/neutral classification
- **Political party classification**: Labor vs Liberal vs unknown
- **Engagement metrics**: Likes, reposts, replies analysis
- **Comparative reports**: Labour vs Liberal sentiment comparison
- **JSON reports**: Detailed analysis saved to `data/` directory

## Dependencies

Key libraries:
- `tweepy`: X.com API access
- `pandas`, `numpy`: Data processing
- `textblob`: Sentiment analysis
- `scikit-learn`: Machine learning utilities
- `sqlite3`: Database storage

## Important Notes

- **API Limits**: Respects X.com rate limits with built-in delays
- **Legal Compliance**: Designed to comply with X.com Terms of Service
- **Data Privacy**: Stores only public post content and metadata
- **Fallback Options**: Works with API or web scraping methods
- **Australian Focus**: Specifically tuned for Australian political content
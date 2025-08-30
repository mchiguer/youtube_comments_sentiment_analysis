# YouTube Comments – Sentiment Analysis about NFT, Crypto and Bitcoin

This project collects YouTube comments, cleans them, performs **sentiment analysis**, and generates **visualizations**.

> I have a report that explains the context, the methodology (YouTube API key, comment retrieval, TextBlob for sentiment analysis, and plots), and provides a summary of the results, contact me to have it.

---

## Repository Contents

- `yt-comment-scraper.py`  
  Script to **download comments** from multiple YouTube videos (list of URLs and you can use IDs).
- `comments.txt`  
  **Raw** comments collected
- `comments_clean.txt`  
  **Cleaned** version of the comments and its optional
- `analyze_sentiment.py`  
  Analyzes each line from `comments.txt` (or `comments_clean.txt`) with **TextBlob** and generates a CSV of results.
- `sentiment_analysis_results.csv`  
  Tabular output: comment + polarity + label (`Positive|Neutral|Negative`).
- `visualize.py`  
  Generates visualizations (pie and bar chart) from the CSV.


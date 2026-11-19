# Web Scraper for Headlines & Quotes

## Project Overview
This project is a Python web scraper that extracts publicly available quotes, authors, and tags from Quotes to Scrape.

## Features
- Fetches public web pages using Requests.
- Extracts quotes using BeautifulSoup.
- Collects author names and tags.
- Scrapes up to 20 quotes from two pages.
- Saves extracted data in JSON format.
- Handles HTTP errors, timeouts, and missing HTML elements.
- Uses a one-second delay between page requests.

## Source Website
https://quotes.toscrape.com/

## Why This Source?
I selected Quotes to Scrape because it is a public practice website for learning web scraping. It does not require login or personal information.

## Technologies Used
- Python
- Requests
- BeautifulSoup
- JSON
- Time Module

## Installation
Install the required libraries:

`python -m pip install -r requirements.txt`

## How to Run
Run the following command:

`python web_scraper.py`

## Output
The extracted quotes, authors, and tags are saved in `quotes.json`.

## Learning Outcomes
- HTTP requests
- HTML parsing
- CSS selectors
- Error handling
- JSON data storage

## Responsible Scraping
The program makes only two page requests, waits one second between requests, and does not collect personal information.
# Yellow Pages Scraper

## Overview
This Python script scrapes job listings from Yellow Pages for a given city and job title, and updates a Google Sheets document with the scraped data. It utilizes the `requests`, `BeautifulSoup`, and `gspread` libraries.

## Requirements
- Python 3.x (**Recommended: 3.6 or later**)
- `requests` ([requests](URL requests library python ON Read the Docs docs.python-requests.org))
- `beautifulsoup4` ([BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/))
- `gspread` ([gspread](https://gspread.readthedocs.io/))

## Installation
1. Clone this repository to your local machine:
git clone https://github.com/mujtabach2/yellowPagesScraper.git
2. Install the required Python libraries:
pip install requests beautifulsoup4 gspread

3. **Important:** Create a file named `creds.json` in the root directory of the project. This file will store your Google service account credentials, which are necessary for accessing Google Sheets. **Keep this file confidential as it contains sensitive information.**

4. Change the name of the sheet within the script (`sh = gc.open("ScrapeToSheets").sheet1`) to match your actual sheet name.

## Usage
1. Run the `scrape.py` script:
python3 scrape.py

2. Follow the prompts to enter the city you want to search in and the job title you are looking for.

3. The script will scrape job listings from Yellow Pages for the specified city and job title, and update the Google Sheets document with the scraped data.

4. The script will pause for 60 seconds between each scrape to comply with rate limits.


import requests
from bs4 import BeautifulSoup
import json
import time

# Website settings
BASE_URL = "https://quotes.toscrape.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0 BeginnerPythonWebScraper"
}

# CSS selectors
QUOTE_SELECTOR = "div.quote"
TEXT_SELECTOR = "span.text"
AUTHOR_SELECTOR = "small.author"
TAG_SELECTOR = "a.tag"


def scrape_quotes():

    all_quotes = []

    # Scrape first two pages
    for page in range(1, 3):

        url = f"{BASE_URL}/page/{page}/"

        print(f"\nScraping page {page}...")

        try:
            response = requests.get(
                url,
                headers=HEADERS,
                timeout=15
            )

            response.raise_for_status()

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            quote_items = soup.select(QUOTE_SELECTOR)

            if not quote_items:
                print("No quotes found.")
                break

            for item in quote_items:

                quote_element = item.select_one(TEXT_SELECTOR)
                author_element = item.select_one(AUTHOR_SELECTOR)
                tag_elements = item.select(TAG_SELECTOR)

                # Check missing HTML elements
                if quote_element is None or author_element is None:
                    continue

                quote_data = {
                    "quote": quote_element.get_text(strip=True),
                    "author": author_element.get_text(strip=True),
                    "tags": [
                        tag.get_text(strip=True)
                        for tag in tag_elements
                    ]
                }

                all_quotes.append(quote_data)

            print("Quotes found:", len(quote_items))

        except requests.exceptions.Timeout:
            print("Request timed out.")
            break

        except requests.exceptions.HTTPError as error:
            print("HTTP error:", error)
            break

        except requests.exceptions.RequestException as error:
            print("Connection error:", error)
            break

        # Wait before requesting another page
        if page < 2:
            time.sleep(1)

    return all_quotes


def save_quotes(quotes):

    with open("quotes.json", "w", encoding="utf-8") as file:

        json.dump(
            quotes,
            file,
            indent=4,
            ensure_ascii=False
        )

    print("\nData saved in quotes.json")


def main():

    print("==============================")
    print("       WEB SCRAPER")
    print("==============================")

    quotes = scrape_quotes()

    if quotes:

        save_quotes(quotes)

        print("\nTotal quotes extracted:", len(quotes))

        print("\nFirst 3 extracted quotes:")

        for index, quote in enumerate(quotes[:3], start=1):

            print(f"\nQuote {index}:")
            print("Text:", quote["quote"])
            print("Author:", quote["author"])
            print("Tags:", ", ".join(quote["tags"]))

    else:
        print("\nNo quotes extracted.")
        print("Please check your internet connection or website.")


if __name__ == "__main__":
    main()

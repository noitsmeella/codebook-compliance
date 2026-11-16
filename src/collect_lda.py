"""collect_lda.py — collect LDA filings (pseudo-code skeleton; write the implementation by hand)

Input:  filing years (2021, 2022)
Output: raw API responses (JSON) under data/raw/, one file per page
Checks: notes/verification_guide.md B4, B5 (collection)

Before starting (R0.4):
- Confirm the current API address, whether an API key is needed, and the rate limits in the official docs.
- Open one real response and write down the field names you will keep:
  filing year, registrant, client, activity description, issue code, filing ID.
"""

# Constants: API address, list of years, page size, wait between requests, output folder
# (If an API key is needed, read it from an environment variable; never hard-code it.)


def fetch_page(year, page):
    """Request one page and return the response as a dict.

    1. Build request parameters from the year and page number
    2. Send a GET request (with a timeout)
    3. If the status code means rate-limited, wait and retry (decide a maximum number of retries)
    4. Raise an exception on any other error
    5. Parse the JSON and return it
    """
    raise NotImplementedError


def save_page(data, year, page):
    """Save the response unmodified under data/raw/.

    Put the year and page number in the file name (used for resuming).
    """
    raise NotImplementedError


def collect_year(year):
    """Download every page for one year.

    1. Check which page numbers are already saved (resume after an interruption)
    2. Repeat until there is no next page:
       a. fetch_page
       b. save_page
       c. wait
    3. Return the number of pages and filings downloaded
    """
    raise NotImplementedError


def main():
    """1. collect_year for each year
    2. Print the collection date and per-year counts → copy them into data/README.md and Research Journal
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()

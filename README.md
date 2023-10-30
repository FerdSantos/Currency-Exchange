# Currency Exchange Rate History Scraper

This is a Python script that scrapes historical currency exchange rate data from the website `exchangerates.org.uk`. The script allows you to specify a base currency and a starting year, and it will collect historical exchange rate data for that currency against a list of other currencies.

## Prerequisites

Before running this script, make sure you have the following prerequisites installed:

- Python 3.x
- Required Python packages: `requests`, `BeautifulSoup`, and `datetime`

You can install the required packages using `pip`:

```bash
pip install requests
pip install beautifulsoup4
```

## Usage

1. Import the necessary modules and functions:

   ```python
   import requests
   from bs4 import BeautifulSoup
   import datetime
   import time
   ```

2. Define the `updateCurrencyHistory` function to update currency exchange rate history. You can specify the base currency and the starting year as function parameters. By default, the base currency is 'EUR' and the starting year is 2010.

   ```python
   def updateCurrencyHistory(fromYear=2010, currencyBase='EUR'):
       # Function code here
   ```

3. Specify the list of target currencies in the `currencies` variable. You can modify this list as needed.

4. The script checks and removes the base currency from the list of target currencies.

5. Define the start and end date for data collection. The script generates a list of dates within the specified range.

6. The script loads existing data from a text file (if it exists) to avoid re-scraping data that has already been collected.

7. Iterate through each target currency and update its historical exchange rate data. The script collects data for missing dates and years.

8. After updating the data, the script saves it to a text file for future use.

9. The `if __name__ == "__main__":` block ensures that the script is executed when the module is run directly. You can call the `updateCurrencyHistory` function with your desired parameters to start the data collection.

## Example Usage

To update the historical exchange rate data for the base currency 'EUR' starting from the year 2010, you can run the script as follows:

```python
if __name__ == "__main__":
    updateCurrencyHistory(fromYear=2010, currencyBase='EUR')
```

This will scrape and update the exchange rate history for 'EUR' against a list of other currencies, saving the data to a text file.

## Note

- The script may take some time to run, depending on the number of target currencies and the range of dates to collect.

- The script uses web scraping techniques, which are subject to website structure changes. If the website structure changes, the script may need to be updated accordingly.

- The historical exchange rate data is saved to a text file with a name like "Currency Exchange History - Base EUR.txt," where 'EUR' is the base currency. You can modify the filename as needed.

- The script includes commented lines that can be uncommented to measure the execution time if desired.

Please be aware of web scraping ethics and respect the website's terms of service when using this script.

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


# Currency Exchange Rate Query

This Python script allows you to query historical currency exchange rates using data collected and saved by the "Currency Exchange Rate History Scraper" script provided earlier.

## Prerequisites

Before using this script, make sure you have the following prerequisites:

- Python 3.x
- The `datetime` module
- The `webscrapALL` module, which should contain the `updateCurrencyHistory` function from the previous script.

## Usage

1. Import the necessary modules and functions:

   ```python
   from datetime import datetime
   from webscrapALL import updateCurrencyHistory
   ```

2. Define the `currencyRate` function to query historical exchange rates. This function takes three parameters: `currencyBase`, `currencyQuote`, and `date`.

   ```python
   def currencyRate(currencyBase, currencyQuote, date):
       # Function code here
   ```

3. The script attempts to load existing exchange rate data from the text file "Currency Exchange History - Base {currencyBase}.txt." It then checks if the requested exchange rate data is available for the given date.

4. If the data is available, the script returns the exchange rate for the requested date.

5. If the data is not available for the requested date, the script tries to format the date in different formats to match the stored data. If none of the date formats match, it returns "Invalid date format."

6. If the date format is valid but the data is not available, the script attempts to update the exchange rate data for the missing date using the `updateCurrencyHistory` function and then queries the data again recursively.

7. If the text file is empty or not found, the script assumes there is no existing data and attempts to update the data for the missing date using the `updateCurrencyHistory` function and then queries the data again recursively.

8. If the text file is not found at all, the script assumes there is no existing data and proceeds to update the data for the missing date using the `updateCurrencyHistory` function and then queries the data again recursively.

9. The example usage at the end of the script demonstrates how to use the `currencyRate` function to query the exchange rate for the base currency 'EUR' against the quote currency 'USD' on the date '01/01/2010'.

## Example Usage

To query the historical exchange rate for 'EUR' against 'USD' on the date '01/01/2010', you can use the `currencyRate` function as follows:

```python
print(currencyRate('EUR', 'USD', '01/01/2010'))
```

This will attempt to retrieve the exchange rate for the specified date. If the data is not available, the script will update it and try the query again.



## Currencies available:

'US Dollar', 'Euro', 'United Arab Emirates Dirham', 'Danish Krone', 'British Pound', 'Malaysian Ringgit', 'Nigerian Naira', 'Norwegian Krone', 'Chinese Yuan', 'Hungarian Forint', 'Czech Koruna', 'Polish Zloty', 'Romanian Leu', 'Swedish Krona', 'Thai Baht', 'Australian Dollar', 'Indian Rupee', 'Moroccan Dirham', 'New Zealand Dollar', 'Omani Rial', 'Albanian Lek', 'Bulgarian Lev', 'Croatian Kuna', 'Icelandic Krona', 'Kazakhstan Tenge', 'Macedonian Denar', 'Moldovan Leu', 'Russian Rouble', 'Swiss Franc', 'Turkish Lira', 'Ukraine Hryvnia', 'Argentine Peso', 'Aruba Florin', 'Bahamian Dollar', 'Barbadian Dollar', 'Belize Dollar', 'Bermuda Dollar', 'Bolivian Boliviano', 'Brazilian Real', 'Canadian Dollar', 'Cayman Islands Dollar', 'Chilean Peso', 'Colombian Peso', 'Costa Rica Colon', 'Dominican Peso', 'East Caribbean Dollar', 'El Salvador Colon', 'Fiji Dollar', 'Guatemala Quetzal', 'Haiti Gourde', 'Honduras Lempira', 'Jamaican Dollar', 'Mexican Peso', 'Neth Antilles Guilder', 'Panamanian Balboa', 'Paraguayan Guarani', 'Peruvian Nuevo Sol', 'Swaziland Lilageni', 'Trinidad Tobago Dollar', 'Uruguayan New Peso', 'Venezuelan bolivar', 'Australian Dollar', 'Bangladesh Taka', 'Bhutan 
Ngultrum', 'Brunei Dollar', 'Indonesian Rupiah', 'Japanese Yen', 'Macau Pataca', 'Nepalese Rupee', 'Pacific Franc', 'Pakistani Rupee', 'Papua New Guinea Kina', 'Philippine Peso', 'Seychelles Rupee', 'Singapore Dollar', 'Solomon Islands Dollar', 'South Korean Won', 'Sri Lankan Rupee', 'Taiwan Dollar', 'Thai Baht', 'Vanuatu Vatu', 'Egyptian Pound', 'Hong Kong Dollar', 'Iran Rial', 'Iraqi Dinar', 'Kuwaiti Dinar', 'Qatari Riyal', 'Yemen Riyal', 'Saudi Riyal', 'Algerian Dinar', 'Rwanda Franc', 'Tunisian Dinar', 'Israeli Sheqel', 'Jordanian Dinar', 'Lebanese Pound', 'Mongolian Tugrik', 'Burundi Franc', 'Central African CFA franc', 'Comoros Franc', 'Ethiopian Birr', 'Gambian Dalasi', 'Guinea Franc', 'Kenyan Shilling', 'Lesotho Loti', 'Malawi Kwacha', 'Mauritius Rupee', 'Namibian Dollar', 'Nicaragua Cordoba', 'Samoa Tala', 'Sierra Leone Leone', 'South African Rand', 'Tanzanian Shilling', 'Tonga Paanga', 'Ugandan Shilling', 'West African CFA franc'


## Note

- The script assumes that the historical exchange rate data is stored in text files with filenames like "Currency Exchange History - Base EUR.txt." You can modify the filename as needed.

- The script deals with various date formats to ensure compatibility with the stored data. If you encounter issues with date formatting, you can adjust the format in the script.

- Make sure that the `webscrapALL` module contains the `updateCurrencyHistory` function to update the currency exchange rate data.

- The script may take some time to run, depending on the number of target currencies and the range of dates to collect.

- The script uses web scraping techniques, which are subject to website structure changes. If the website structure changes, the script may need to be updated accordingly.

- The historical exchange rate data is saved to a text file with a name like "Currency Exchange History - Base EUR.txt," where 'EUR' is the base currency. You can modify the filename as needed.

- The script includes commented lines that can be uncommented to measure the execution time if desired.

Please be aware of web scraping ethics and respect the website's terms of service when using this script.

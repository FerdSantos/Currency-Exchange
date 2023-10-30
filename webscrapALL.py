import requests
from bs4 import BeautifulSoup
import datetime


import time

def updateCurrencyHistory(fromYear = 2010, currencyBase = 'EUR'):
    # start_time = time.time() # Uncomment In case you would like to check how long it takes to the code run



    currencies = ['EUR €', 'USD $', 'AED د.إ', 'DKK kr', 'GBP £', 'MYR RM', 'NGN ₦', 'NOK kr', 'CNY ¥', 'HUF Ft', 'CZK Kč', 'PLN zł',
'RON lei', 'SEK kr', 'THB ฿', 'AUD $', 'INR ₹','MAD د.م.', 'NZD $', 'OMR ﷼','ALL Lek', 'BGN лв', 'HRK kn', 'ISK kr', 'KZT ₸', 'MKD ден', 'MDL L', 'RUB ₽', 'CHF CHF', 'TRY ₤', 'UAH ₴', 'ARS $', 'AWG ƒ', 'BSD $', 'BBD $',
        'BZD BZ$', 'BMD $', 'BOB $', 'BRL R$', 'CAD $', 'KYD $', 'CLP $', 'COP $', 'CRC ₡', 'DOP RD$', 'XCD $', 'SVC $', 'FJD $', 'GTQ Q', 'HTG G', 'HNL L', 'JMD J$', 'MXN $',
                'ANG ƒ', 'PAB B/.', 'PYG Gs', 'PEN S/.', 'SZL L', 'TTD $', 'UYU $U', 'VEF Bs', 'AUD $', 'BDT ৳', 'BTN Nu.', 'BND $', 'IDR Rp', 'JPY ¥', 'MOP MOP$', 'NPR ₨', 'XPF F', 'PKR ₨',
                'PGK K', 'PHP ₱', 'SCR ₨', 'SGD $', 'SBD $', 'KRW ₩', 'LKR ₨', 'TWD NT$', 'THB ฿', 'VUV VT', 'EGP E£', 'HKD $', 
                'IRR ﷼', 'IQD ع.د', 'KWD د.ك', 'QAR ﷼', 'YER ﷼', 'SAR ﷼', 'DZD دج', 'RWF ر.س', 'TND د.ت',
                'ILS ₪', 'JOD JD', 'LBP £', 'MNT ₮', 'BIF FBu', 'XAF FCFA', 'KMF CF', 'ETB Br', 'GMD D', 'GNF FG', 'KES KSh', 'LSL L', 'MWK MK', 'MUR ₨', 'NAD $', 'NIO C$',
                    'WST WS$', 'SLL Le', 'ZAR R', 'TZS TSh', 'TOP T$', 'UGX USh', 'XOF FCFA']
    


    # Check and Remove the CurrencyBase from list
    for i in currencies:
        i = i.split(' ')
        if i[0] == currencyBase:
            currencies.remove(' '.join(i))



    # Define the start and end date 
    start_date = datetime.date(fromYear, 1, 1)
    end_date = datetime.date.today()

    # Create a list of all dates from start_date to end_date
    date_range = [start_date + datetime.timedelta(days=x) for x in range((end_date - start_date).days)]

    
    # Load existing data from 'Currency Exchange History - Base {currencyBase}.txt' if it exists
    try:
        with open(f'Currency Exchange History - Base {currencyBase}.txt', 'r') as r:
            try:
                CurrencyHistory = eval(r.read())
            except:
                CurrencyHistory = {}
    except FileNotFoundError:
        CurrencyHistory = {}


    # Start iteration through all currencies
    for currency in currencies:
        currency = currency.split(' ')
        
        if f'{currencyBase}/{currency[0]}' not in CurrencyHistory:
            CurrencyHistory[f'{currencyBase}/{currency[0]}'] = {}



        # Access the Currency key to get the inner dictionary
        currencyKey = CurrencyHistory[f'{currencyBase}/{currency[0]}']

        # Create a list to store already saved dates
        dates_hist = []

        # Iterate through the dates and their corresponding rates
        for date, rate in currencyKey.items():
            dates_hist.append(date)
        
        # Create a list to store missing dates
        missing_dates = []

        # Iterate through the dates in the date range and check what needs to be updated
        for date in date_range:
            date_str = '{}/{}/{}'.format(date.day, date.month, date.year)
            
            if date_str not in dates_hist:
                missing_dates.append(date_str)
                
            
        # Create a list to store missing years
        yearsToUpdate = []

        for missingYear in missing_dates:
            if missingYear[-4:] not in yearsToUpdate:
                yearsToUpdate.append(missingYear[-4:])
        
        # print(yearsToUpdate)


        
        # Iterate through all dates on the years missing
        for year in yearsToUpdate:


            url = f'https://www.exchangerates.org.uk/{currencyBase}-{currency[0]}-spot-exchange-rates-history-{year}.html'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all table rows with class "colone"
            rows = soup.find_all('tr', class_=['colone', 'coltwo'])

            # Iterate over the rows and extract the information
            for row in rows:
                
                # Deal with dates format
                date = (row.find('td').text).split(' ')
                if date[1] == '':
                    day = date[2]
                    month = date[3]
                    year = date[4]
                else:
                    day = date[1]
                    month = date[2]
                    year = date[3]
               
                month = datetime.datetime.strptime(month, "%B").month
                # month = month.month
                

                date = f'{day}/{month}/{year}'

                
                exchange_rate = (row.find('td', string=lambda text: 'EU' in text).text).split(f' {currency[1]}')[1]

                
                
                CurrencyHistory[f'{currencyBase}/{currency[0]}'][date] = exchange_rate
        
        CurrencyHistory[f'{currencyBase}/{currency[0]}']= dict(sorted(CurrencyHistory[f'{currencyBase}/{currency[0]}'].items()))
        print(f'{currencyBase}/{currency[0]}', 'done')

    
    # Save to the file the updated currencies
    with open(f'Currency Exchange History - Base {currencyBase}.txt', 'w') as w:
        w.write(str(CurrencyHistory))



    # end_time = time.time()                                                       # Uncomment In case you would like to check how long it takes to the code run
    # execution_time = end_time - start_time                                        # Uncomment In case you would like to check how long it takes to the code run
    # print(f"Execution time: {execution_time} seconds")                            # Uncomment In case you would like to check how long it takes to the code run




if __name__ == "__main__":
    # This block will only be executed when the module is run directly
    updateCurrencyHistory()  # Call the function to update currency history

from datetime import datetime
from webscrapALL import updateCurrencyHistory




def currencyRate(currencyBase, currencyQuote, date):

    # Load existing data from 'Currency Exchange History - Base {currencyBase}.txt' if it exists
    try:
        with open(f'Currency Exchange History - Base {currencyBase}.txt', 'r') as r:
            try:
                hist = eval(r.read())
                parity = f'{currencyBase.upper()}/{currencyQuote.upper()}'
                
                # Deal with different kinds of possible format dates such as DD/MM/YY; MM/DD/YY; YY/MM/DD
                try:
                    date_obj = datetime.strptime(date, '%m/%d/%Y')
                    day, month, year = date_obj.day, date_obj.month, date_obj.year
                except ValueError:
                        try:
                            date_obj = datetime.strptime(date, '%Y/%m/%d')
                            day, month, year = date_obj.day, date_obj.month, date_obj.year
                        except ValueError:
                            try:
                                date_obj = datetime.strptime(date, '%d/%m/%Y')
                                day, month, year = date_obj.day, date_obj.month, date_obj.year
                            except ValueError:
                                return "Invalid date format"

                formatted_date = f"{day}/{month}/{year}"
                date = formatted_date.replace("/0", "/")

                try:
                    return hist[parity][date]
                except:

                    print(f"This date is not available, let's updated it!")
                    updateCurrencyHistory(int(date[-4:]), currencyBase)
                    return currencyRate(currencyBase, currencyQuote, date)
            except:
                print(f"Empty database, let's update it!")
                updateCurrencyHistory(int(date[-4:]), currencyBase)
                return currencyRate(currencyBase, currencyQuote, date)

    except:
        updateCurrencyHistory(int(date[-4:]), currencyBase)
        return currencyRate(currencyBase, currencyQuote, date)
    

    

print(currencyRate('EUR', 'USD', '01/01/2010'))

import forex_python as fxp
import datetime
from forex_python.converter import CurrencyRates
import pandas as pd

base_date = datetime.datetime.today()
base_date = datetime.datetime(base_date.year, base_date.month, base_date.day)

date_list = [base_date-datetime.timedelta(days = x) for x in range(366)]

c = CurrencyRates()

currency_list = []
for d in date_list:
    try:
        rates_list = c.get_rates('MXN',d)
        for r in rates_list:
            row = {}
            row['date'] = d
            row['currency'] = r
            row['rates'] = rates_list[r]
            currency_list.append(row)
    except Exception as e:
        print('Error: {} for day: {}'.format(e, d))
    

    


pd.DataFrame(currency_list).to_csv('mxn.csv', index = False)







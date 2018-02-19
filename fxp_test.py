import forex_python.converter as fxp
import datetime
import pandas as pd

base_date = datetime.datetime.today()
base_date = datetime.datetime(base_date.year, base_date.month, base_date.day)

date_list = [base_date-datetime.timedelta(days = x) for x in range(366)]
total = len(date_list)

c = fxp.CurrencyRates()

print('MXN to AUD rate: {}'.format(c.get_rate('AUD', 'MXN')))

currency_list = []
x=0
for d in date_list:
    x+=1
    print('processing {} out of {}'.format(x, total))
    try:
        rates_list = c.get_rate('MXN',d)
        for r in rates_list:
            row = {}
            row['date'] = d
            row['currency'] = r
            row['rates'] = rates_list[r]
            currency_list.append(row)
    except Exception as e:
        print('Error: {} for day: {}'.format(e, d))

pd.DataFrame(currency_list).to_csv('mxn.csv', index = False)







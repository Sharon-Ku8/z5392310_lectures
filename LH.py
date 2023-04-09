happy = True
if happy is True:
    print("I am happy")

print("This will print regardless of the value of happy")

happy = True
very_happy = True

if happy is True:
    print("I am happy")                         # <-- four-spaces indentation
    if very_happy is True:                      # <-- four-spaces indentation
        print("Actually, I'm really happy!")    # <-- eight-spaces indentation

happy = True
if happy:
    print("I am happy")

happy = 5
if happy:
    print("I am happy")

happy = 0
if happy:
    print("I am happy") # <-- will not be printed

s = {'a', 'c'}
'a' in s or 'b' not in s

'a' in s or not ('b' in s)

not ('a' not in s and 'b' in s)

for i in range (1,11):
    print(i)

if not False:
   print("not False is True")

if not True is False:
   print("not True is False")

less_than_test = "That" < "This"
print(f'"That" < "This" yields {less_than_test}')
greater_than_test = "That" > "This"
print(f'"That" > "This" yields {greater_than_test}')

b = False
if b is True:
   print("b is True")
else:
   print("b is not True")

if x > 0 and y is True:
    # Write code for this case later
    pass
elif x <= 0 and y is True:
    # Write code for this case later
    pass
else:
    # Write code for this case later
    pass



# NOTE: You won't be able to execute this code in ED
import yfinance

start = '2020-01-01'
end = None

tickers = ["QAN.AX", "WES.AX"]
for tic in tickers:
    df = yfinance.download(tic, start, end, ignore_tz=True)
    print(df)
    tic_base = tic.lower().split('.')[0]
    df.to_csv(f'{tic_base}_stk_prc.csv')

d = {
    "beauty": True,
    "truth": True,
    "red wheelbarrow": 100000,
    5: "fingers",
    }
for val in d.values():
    print(val)

import pandas as pd

# Part (a)
# Create a pandas series called series_abc with
# index ['a', 'b', 'c'] and values [1, 2, 3]
series_abc = pd.Series(data = {'a':1, 'b':2, 'c':3})
print(series_abc)

# Part (b)
# Given the stock price-date dictionary prc_date
# listed below, create a pandas series series_stk
# with the dates as indices and the prices as values.
prc_date = {
    7.1600: '2020-01-02',
    7.1900: '2020-01-03',
    7.0000: '2020-01-06',
    7.1000: '2020-01-07',
    6.8600: '2020-01-08',
    6.9500: '2020-01-09',
    7.0000: '2020-01-10',
    7.0200: '2020-01-13',
    7.1100: '2020-01-14',
    7.0400: '2020-01-15',
    }
series_stk = pd.Series(data={v:k for k,v in prc_data.items()})
print(series_stk)

# Part c
# Given the dictionary
dic = {i:i+1 for i in range(10000)}
# create a Pandas series called series_ones
# with indices from 0 through 9999 and with
# all values equal to 1.
# Do not use a secondary dictionary to create the series in Pandas.
# Instead, specify the data and index arguments directly.
series_ones = pd.Series(data=1, index=dic.keys())


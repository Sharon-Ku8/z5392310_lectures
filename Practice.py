a = True
b = 5
print (f"The value of a is {a} and the value of b is {b}")
print ("The value of a is {} and the value of b is {}".format(a , b))

date = "2/23/2023"
mins = 5
print (f"The exam's date is {date}, you will have {mins} minutes.")
print ("The exam's date is {}, you will have {} minutes.".format(date, mins))

print (' some text '.strip)
print (' some text '.strip(None))
print (' some text '.strip(' '))
print (' some text '.strip('some text'))
print (' some text '.strip())

w = "What"
i = "IS"
c = "CamelCase?"
print (f'{w} {i} {c}')
print ('{} {} {}'.format(w, i.lower, c))
print ('{} {} {}'.format(w, i.lower(), c))
print ('{} {} {}'.format(w, i, c).lower())

x = 1
y = 2
y = x
x = y
print (x)

# Downloads Qantas share price beginning 1 January 2020
import yfinance
tic = "QAN.AX"
start = '2020-01-01'
end = None
df = yfinance.download(tic, start, end)
print(df)
df.to_csv('qan_stk_prc.csv')

# Downloads Qantas share price beginning 1 January 2020
import yfinance as df
df.download("QAN.AX", '2020-01-01', None).to_csv('qan_stk_prc.csv')

import json
help(json.load)

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(len(l))
print(l[2:10])
print(l[2:11])
print(l[2:])

t = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(len(t))
print(t[-8:10])
print(t[-8:11])
print(t[-8:])
print(t[-8:12])

dic0 = {'a': 1, 'b': 2, 'c': 3}
dic1 = dic0.update({'a': 0, 'd': 4})
print(dic0)
print(dic1)

tup = (1, 2, ('a', 'b'))
dic = {tup: 'value'}

# Use the dictionary f_suburbs as given as your starting point.
# This dictionary contains Sydney suburb/population pairs,
# with the mapping going from suburb keys to population values.

# Do the following steps:
# 1. Remove all suburbs that don't start with a F
# 2. Ensure that your dictionary contains:
#
#     Fairfield: 18081
#     Fairfield East: 5273
#     Fairfield Heights: 7517
#     Fairfield West: 11575
#     Fairlight: 5840
#     Fiddletown: 233
#     Five Dock: 9356
#     Flemington: None
#     Forest Glen: None
#     Forest Lodge: 4583
#     Forestville: 8329
#     Freemans Reach: 1973
#     Frenchs Forest: 13473
#     Freshwater: 8866

# The None values indicate the Wikipedia did not have population data.
# These should be INCLUDED in your dictionary.

f_suburbs = {"Frenchs Forest": 13473, "Flemington": None}

#f_suburbs.pop('Randwick')
#f_suburbs.pop('Kensington')

f_suburbs.update({
      'Fairfield': 18081,
      'Fairfield East': 5273,
      'Fairfield Heights': 7517,
      'Fairfield West': 11575,
      'Fairlight': 5840,
      'Fiddletown': 233,
      'Five Dock': 9356,
      'Flemington': None,
      'Forest Glen': None,
      'Forest Lodge': 4583,
      'Forestville': 8329,
      'Freemans Reach': 1973,
      'Frenchs Forest': 13473,
      'Freshwater': 8866
})










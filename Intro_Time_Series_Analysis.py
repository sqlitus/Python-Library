# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 15:42:03 2018

https://towardsdatascience.com/time-series-analysis-in-python-an-introduction-70d5a5b1d52a
"""

# quandl for financial data
import quandl
# pandas for data manipulation
import pandas as pd

# key to retreive data
quandl.ApiConfig.api_key = 'RDU2iDsz-RVF5355rWzo'

# Retrieve TSLA data from Quandl
tesla = quandl.get('WIKI/TSLA')

# Retrieve the GM data from Quandl
gm = quandl.get('WIKI/GM')
gm.head(5)


# The adjusted close accounts for stock splits, so that is what we should graph
import matplotlib.pyplot as plt
plt.plot(gm.index, gm['Adj. Close'])
plt.title('GM Stock Price')
plt.ylabel('Price ($)');
plt.show()

plt.plot(tesla.index, tesla['Adj. Close'], 'r')
plt.title('Tesla Stock Price')
plt.ylabel('Price ($)');
plt.show();


# Yearly average number of shares outstanding for Tesla and GM. Dictionary.
tesla_shares = {2018: 168e6, 2017: 162e6, 2016: 144e6, 2015: 128e6, 2014: 125e6, 2013: 119e6, 2012: 107e6, 2011: 100e6, 2010: 51e6}

gm_shares = {2018: 1.42e9, 2017: 1.50e9, 2016: 1.54e9, 2015: 1.59e9, 2014: 1.61e9, 2013: 1.39e9, 2012: 1.57e9, 2011: 1.54e9, 2010:1.50e9}

# Create a year column 
tesla['Year'] = tesla.index.year

# Take Dates from index and move to Date column 
tesla.reset_index(level=0, inplace = True)
tesla['cap'] = 0

# Calculate market cap for all years
for i, year in enumerate(tesla['Year']):
    # Retrieve the shares for the year
    shares = tesla_shares.get(year)
    
    # Update the cap column to shares times the price
    tesla.ix[i, 'cap'] = shares * tesla.ix[i, 'Adj. Close']




# reference: subsetting dataframes w/ pandas
# https://stackoverflow.com/questions/509211/understanding-pythons-slice-notation
gm.index # not a column
gm['Adj. Close']
gm['Open']
vars(gm)
dir(gm)
gm.head(1)
gm[['Open']]
gm.columns[2]
gm[gm.columns[1:3]]
gm[:1] # rows x:1
gm.columns[-1]
gm.columns[1:3]
gm.columns[-2:]
gm.columns[:-5]

# reference: object properties & type
# https://stackoverflow.com/questions/2225038/determine-the-type-of-an-object
tesla.index
tesla.index.year
tesla.index.month
tesla.index.time
type(tesla)
type(tesla.index)
type(tesla.index.year)
tesla.Open
type(tesla.Open)
tesla['Open']
type(tesla['Open'])
type(tesla.Year)
len(tesla.Year)
type(tesla['Adj. Close'])

# piping

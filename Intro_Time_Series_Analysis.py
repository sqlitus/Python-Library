# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 15:42:03 2018

https://towardsdatascience.com/time-series-analysis-in-python-an-introduction-70d5a5b1d52a

analysis required my additions to GM data
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
gm['Year'] = gm.index.year

# Take Dates from index and move to Date column 
tesla.reset_index(level=0, inplace = True)
tesla['cap'] = 0
gm.reset_index(level = 0, inplace = True)
gm['cap'] = 0

# Calculate market cap for all years - TESLA
for i, year in enumerate(tesla['Year']):
    # Retrieve the shares for the year
    shares = tesla_shares.get(year)
    # Update the cap column to shares times the price
    tesla.loc[i, 'cap'] = shares * tesla.loc[i, 'Adj. Close']

# Calculate market cap for all years - GM
for i, year in enumerate(gm['Year']):
    shares = gm_shares.get(year)
    gm.loc[i, 'cap'] = shares * gm.loc[i, 'Adj. Close']

# Merge the two datasets and rename the columns
cars = gm.merge(tesla, how='inner', on='Date')
cars.rename(columns={'cap_x': 'gm_cap', 'cap_y': 'tesla_cap'}, inplace=True)

# Select only the relevant columns
cars = cars.loc[:, ['Date', 'gm_cap', 'tesla_cap']]

# Divide to get market cap in billions of dollars
cars['gm_cap'] = cars['gm_cap'] / 1e9
cars['tesla_cap'] = cars['tesla_cap'] / 1e9
cars.head()

# plot market cap for GM vs Tesla
plt.figure(figsize=(10, 8))
plt.plot(cars['Date'], cars['gm_cap'], 'b-', label = 'GM')
plt.plot(cars['Date'], cars['tesla_cap'], 'r-', label = 'TESLA')
plt.xlabel('Date'); plt.ylabel('Market Cap (Billions $)'); plt.title('Market Cap of GM and Tesla')
plt.legend();

import numpy as np

# Find the first and last time Tesla was valued higher than GM
first_date = cars.loc[np.min(list(np.where(cars['tesla_cap'] > cars['gm_cap'])[0])), 'Date']
last_date = cars.loc[np.max(list(np.where(cars['tesla_cap'] > cars['gm_cap'])[0])), 'Date']

print("Tesla was valued higher than GM from {} to {}.".format(first_date.date(), last_date.date()))




cars.loc[np.min(list(np.where(cars['tesla_cap'] > cars['gm_cap'])[0])), 'Date']
np.where(cars['tesla_cap'] > cars['gm_cap'])
print(list(np.where(cars['tesla_cap'] > cars['gm_cap'])))

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
gm.columns[-1] # column name
gm.columns[1:3]
gm.columns[-2:]
gm.columns[:-5]
gm.ix[1]
gm.iloc[1]
gm.iloc[1,1]
gm.iloc[:2] # 1st 2 rows
gm.iloc[0] # 1st row
tesla.ix[0, 'cap']
tesla.iloc[0, 'cap'] # index position 
tesla.loc[0, 'cap'] # name the index location label (if index is not integer)
tesla.loc[0, 'Open']
tesla.loc[:,'Open']
tesla['Open']

# reference: object properties & type
# https://stackoverflow.com/questions/2225038/determine-the-type-of-an-object
tesla.index
dir(tesla.index)
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

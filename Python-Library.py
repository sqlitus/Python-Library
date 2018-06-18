# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 15:01:07 2018

"""

# hello world
x=1
print(x)
print('not x')
print(x+2)
print(' ')
y = 'the fox was 5'
print(y)
print(int(y)+2)
print('5', 5, 'something else 555', 4, sep = ' ', end = '\nthis is the end\n')
x.bit_length()

z = 555
z.bit_length()
z.conjugate()

y.capitalize()
y.casefold()





# list manipulation & indexing
y = 'bob'
mylist = [x, y, 10, 5, '6']
mylist[0]
mylist[1]
mylist[2]
mylist[3]
mylist[0:3]
mylist[0:2]
mylist[0:1]
sum([5,6])
mylist * 5
mylist.count('5')
mylist.count('bob')
mylist.index('6')
mylist[1]
mylist[0]
mylist.append(mylist) # affects list object directly
mylist.clear()
mylist.copy()
mylist.count(5)
mylist.extend(mylist)
mylist.index('bob')
mylist[1]
mylist.insert(1, 2) # before element, adds object
mylist.pop(4) # removes the object & returns it
mylist.remove('bob') # just removes the value period.
mylist.reverse()
mylist = [1,5,3,33,11]
mylist.sort() # sorts numerically
mylist.reverse()
mylist
mylist.__add__(mylist) # lengthens the list w/ another list?
mylist.__class__()
x.__class__()
mylist.__contains__(33) # boolean check


# for loops & list arithmatic
for i in mylist:
    print(i)
mynums = [1,2,3]
print(mynums)
for i in mynums:
    print(i)
mynums * 3
for i in mynums:
    print(5*i)

    
# navigate files
import os
os.getcwd()
os.listdir('.')
os.chdir("\\\\cewp1650\\Chris Jabr Reports\\ONOW Exports\\")
os.getcwd()


# import files
# https://www.datacamp.com/community/tutorials/python-excel-tutorial
import pandas as pd
ticketdata = pd.ExcelFile("\\\\cewp1650\\Chris Jabr Reports\\ONOW Exports\\incident.xlsx")
print(ticketdata.sheet_names)
df1 = ticketdata.parse()


# dataframes
# https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/
my_data_frame = pd.DataFrame(
        {
                'col_1': [1,2,3,4,5],
                'col_2': ['here','are','some','sample','values']
        }
)
my_data_frame.shape
my_data_frame.head()
my_data_frame.dtypes
my_data_frame['col_2']
my_data_frame.describe()


# github
# https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/
import sys
print(sys.path)


# time series manipulation
# https://towardsdatascience.com/basic-time-series-manipulation-with-pandas-4432afee64ea
import pandas as pd
from datetime import datetime
import numpy as np

date_rng = pd.date_range(start='1/1/2018', end='1/08/2018', freq='H')
date_rng[0]
type(date_rng[0])

df = pd.DataFrame(date_rng, columns=['date'])
df['data'] = np.random.randint(0,100,size=(len(date_rng))) # new column
df.head(15)

df['datetime'] = pd.to_datetime(df['date'])
type(df['date'])
df = df.set_index('datetime') # change index to datetime series
df.drop(['date'], axis=1, inplace=True)
df.head()

string_date_rng = [str(x) for x in date_rng]
string_date_rng

timestamp_date_rng = pd.to_datetime(string_date_rng, infer_datetime_format=True)
timestamp_date_rng

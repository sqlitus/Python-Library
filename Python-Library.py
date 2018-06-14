# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 15:01:07 2018

@author: Chris.J
"""

# hello world
x=5
print(x)
print('not x')
print(x+2)
print(' ')
y = '5'
print(y)
print(int(y)+2)
print('5', 5, 'something else 555', 4, sep = ' ', end = '\nthis is the end\n')


# lists & indexing
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


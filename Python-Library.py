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


x = 5
range(5)
range(x)
for i in range(5):
    print(x)
    x+=1
    
for i in range(x):
    print("x = " + str(x))
    print("i = " + str(i))
    



    
# navigate files
import os
os.getcwd()
os.listdir('.')
os.chdir("\\\\cewp1650\\Chris Jabr Reports\\ONOW Exports\\")
os.getcwd()


# import files & create dataframe
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
# to continue


# basic ide tips
import matplotlib.pyplot as plt
import numpy
# from numpy import * - don't have to invoke package for each function

t = numpy.arange(0,1,.01)
y = numpy.sin(2*numpy.pi*t)

plt.figure(1)
plt.clf()
plt.plot(t,y)

mylist = [1,2,3,4]
for item in mylist:
    print(item)
bob = 5



# data science #1 - decision tree demo
from sklearn import tree

x = [[181, 80, 44], [177, 70, 43], [160,60,38]] # feed in body metrics
y = ['male', 'female', 'female']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

prediction = clf.predict([[190,70,43]]) # predict these
print(prediction)
tree.export_graphviz(clf)

# visualize descision tree
# https://chrisalbon.com/machine_learning/trees_and_forests/visualize_a_decision_tree/
import pydotplus
from IPython.display import Image
dot_data = tree.export_graphviz(clf, out_file = None)
graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())

# not run
import os     
os.environ["PATH"] += os.pathsep + 'C:\\Anaconda3\\Library\\bin\\graphviz'








#### advanced dataframe operations ----
# all here: https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python#question3
# also refer to pandas.pydata.org for list of OO functions
# R comparison: https://pandas.pydata.org/pandas-docs/stable/comparison_with_r.html
import pandas as pd
ticketdata = pd.ExcelFile("\\\\cewp1650\\Chris Jabr Reports\\ONOW Exports\\incident.xlsx")
print(ticketdata.sheet_names)
df = ticketdata.parse()
df = pd.DataFrame(df)

# dataframe attributes (purple, indexable)
df.shape
df.size
df.columns
df.values[0,1]
df.ndim
df.dtypes

# dataframe methods (functions) (orange)
df.aggregate('Reopen count')
df.boxplot('Updates')
df.describe()

# dataframe subsetting
x = 5; y = 2
z = ['Number', 'Category', 'Location']
df.iloc[0,0]
df.iloc[0][0]
df.iloc[0,1]
df.iloc[:,0]
df.iloc[0:5,0:2]
df.iloc[0:5] # just row index
df.iloc[0:5,] # just row index
df.loc[0:5, 'Number']
df.loc[0:5, ['Number', 'Category']]
df.loc[0:x, z]
print(df.at[0,'Number']) # use 'at' for single values
print(df.iat[x,0]) # use 'at' for single values

# dataframe create new calculated columns
df['UpdateAvgByReassignment'] = df['Updates'] / (df['Reassignment count'] + 1)

# dataframe drop columns remove column delete columns
df['mynewcol'] = 1
df = df.drop(columns = ['mynewcol']) # or..
df.drop(columns = ['mynewcol'], inplace=True)

# dataframe remove duplicates
mydf = pd.DataFrame(
        {
            'col_1': [1,2,3,4,5,1,2,3,4,5],
            'col_2': ['here','are','some','sample','values','again','are','some','new','values']
            , 'col_3': [11,22,33,44,55,66,77,88,99,55]
        }
)
mydf
mydf.drop_duplicates() # entire row value
mydf.drop_duplicates(subset = ['col_1', 'col_2']) # which row [combinations] to check for duplicates

# dataframe filter by exact string values, regex
exact_searches = ['FL UTC', 'MA SOS']
out = df.loc[df['Location'] == "MA SOS"]
out = df.loc[df["Location"].isin(['FL UTC', 'MA SOS'])]
out = df.loc[df["Location"].isin(exact_searches)]

search_for = ['hst', 'Sos', 'UTC']
out = df[df['Location'].str.contains("HST|SOS")==True] # using regex
out = df[df['Location'].str.contains("(?i)hst|SOS")==True]
out = df[df['Location'].str.contains("|".join(search_for))==True]
out = df[df['Location'].str.contains("(?i)"+"|".join(search_for))==True]
out = df[df['Location'].str.contains("(?i)"+"|".join(["hst","sos","utc"]))==True]

print("something" + " " + "something else" + "and also these")
print("(?i)"+"|".join(["hst","sos"]))




# regex label columns
# conditional value columns...
# create small 'label' table to join & filter, aggregate by...

# dataframe calculated columns with time & time conversions. datediff.
df['my resolve time'] = df['Resolved'] - df['Created']
df['my resolve time 2'] = (df['Resolved'] - df['Created']).astype('timedelta64[h]') # floor hours
df['my resolve time 3'] = (df['Resolved'] - df['Created']).astype('timedelta64[D]') # floor days

# create time series
pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
pd.Series(pd.date_range('2012-1-1', periods=1, freq='D'))
pd.Series(pd.date_range(start='2018-1-1', end='2018-05-01'))

# general date functions. global variables. create a date.
import datetime
datetime.datetime.now()
datetime.datetime.today() # now = today. both datetime.
datetime.datetime.now().date()
datetime.datetime.now().date().weekday()
datetime.datetime.strptime('2018-06-25', "%Y-%m-%d")
datetime.datetime.strptime('2018-06-25', "%Y-%m-%d").weekday() # monday=0, sunday=6
datetime.datetime.strptime('2018-06-25', "%Y-%m-%d").weekday()

# weekday functions
df['Cweekday'] = df['Created'].dt.dayofweek
df['Cweekday_name'] = df['Created'].dt.weekday_name
df['Cdate_add'] = df['Created'] + datetime.timedelta(days=5)
df['Cdate_add_2'] = df['Created'] + pd.DateOffset(days=5) # preferred, faster

# dataframe week ending calculdated date column
df['Cweek_ending'] = df['Created'] + pd.DateOffset(days=(6 - df['Created'].dt.dayofweek)) # not working
df['Cweek_ending'] = df['Created'] + (6-df['Created'].dt.weekday.astype('timedelta64[D]'))

type(df['Created'].dt.dayofweek)
df['Created'].dt.weekday.astype('timedelta64[D]')
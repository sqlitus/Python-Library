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





#### list manipulation & indexing
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


#### for loops & list arithmatic
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
    



    
#### navigate files
import os
os.getcwd()
os.listdir('.')
os.chdir("\\\\cewp1650\\Chris Jabr Reports\\ONOW Exports\\")
os.getcwd()


#### import files & create dataframe
# https://www.datacamp.com/community/tutorials/python-excel-tutorial
import pandas as pd
ticketdata = pd.ExcelFile("\\\\cewp1650\\Chris Jabr Reports\\ONOW Exports\\incident.xlsx")
df = ticketdata.parse()
df = pd.DataFrame(df)
stores = pd.read_excel("C:\\Work\\Resources\\Store Deployment Schedule.xlsx", sheet_name="sql table")


#### dataframe EDA
# https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/
my_data_frame = pd.DataFrame(
        {
                'col_1': [1,2,3,4,5],
                'col_2': ['here','are','some','sample','values']
        }
)
my_data_frame.shape
my_data_frame.head()
my_data_frame.tail()
my_data_frame.dtypes
my_data_frame['col_2']
my_data_frame.describe()
df.sample(3)
df.dtypes
df.query('Updates > 44')
df[df['Updates'] > 44]
pd.isnull(df)

# github
# https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/
import sys
print(sys.path)


#### time series manipulation
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


#### basic ide tips
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



#### data science #1 - decision tree demo
from sklearn import tree

x = [[181, 80, 44], [177, 70, 43], [160,60,38]] # feed in body metrics
y = ['male', 'female', 'female']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

prediction = clf.predict([[190,70,43]]) # predict these
print(prediction)
tree.export_graphviz(clf)

#### visualize descision tree
# https://chrisalbon.com/machine_learning/trees_and_forests/visualize_a_decision_tree/
import pydotplus
from IPython.display import Image
dot_data = tree.export_graphviz(clf, out_file = None)
graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())

# not run
import os     
os.environ["PATH"] += os.pathsep + 'C:\\Anaconda3\\Library\\bin\\graphviz'





#### ADVANCED DATAFRAME OPERATIONS ----
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
df.sort_values('Priority')
df.aggregate('Updates')

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

# dataframe filtering & sorting
zzdf = df[df['Created']>'2018-06-06']
zzdf = df[(df['Created']>'2018-06-06') & (df['Contact type']=='Phone')]
zzdf = df[(df['Created']>'2018-06-06') & 
          (df['Contact type']=='Phone')].sort_values(['Created'], ascending=False)
zzdf = df[(df['Created']>'2018-06-06') & 
          (df['Contact type']=='Phone')].sort_values(['Priority','Created'])
zzdf = df[(df['Created']>'2018-06-06') & 
          (df['Contact type']=='Phone')].sort_values(['Priority','Created'], ascending=[False,True])

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

print("(?i)"+"|".join(["hst","sos"]))

# conditional column values
import numpy as np
df['Conditional_1'] = np.select(
        condlist = [
                (df['Updates'] > 5) & (df['assignee change counter'] > 4),
                (df['Updates'] > 3) & (df['assignee change counter'] > 2)]
        , choicelist = ['very high maintenance', 'high maintenance'])

# regex column values
df['Conditional_2'] = np.select(
        condlist = [df['Location'].str.contains("(?i)NE")==True,
                    df['Location'].str.contains("(?i)"+"|".join(search_for))==True]
        , choicelist = ['ne region','store of interest']
        , default = "--")

# dataframe calculated columns with time & time conversions. datediff.
df['resolve time'] = df['Resolved'] - df['Created']
df['resolve time hours'] = (df['Resolved'] - df['Created']).astype('timedelta64[h]') # floor hours
df['resolve time days'] = (df['Resolved'] - df['Created']).astype('timedelta64[D]') # floor days

# create time series
pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
pd.Series(pd.date_range('2012-1-1', periods=1, freq='D'))
pd.Series(pd.date_range(start='2018-1-1', end='2018-05-01'))

# general date functions. global variables. convert series to date.
import datetime
datetime.datetime.now()
datetime.datetime.today() # now = today. both datetime.
datetime.datetime.now().date()
datetime.datetime.now().date().weekday()
datetime.datetime.strptime('2018-06-25', "%Y-%m-%d").weekday() # monday=0, sunday=6
df['Cdate'] = pd.to_datetime(df['Created']).dt.date

# weekday functions
df['Cweekday'] = df['Created'].dt.dayofweek
df['Cweekday_name'] = df['Created'].dt.weekday_name
df['Cdate_add'] = df['Created'] + datetime.timedelta(days=5)
df['Cdate_add_2'] = df['Created'] + pd.DateOffset(days=5) # preferred, faster
df['Created'].dt.dayofweek
df.drop(columns = ['Cdate_add','Cdate_add_2'], inplace=True)

# dataframe week start week ending
df['Cweek_beginning'] = (df['Created'] - pd.to_timedelta(df['Created'].dt.dayofweek, unit='d')).dt.date
df['Cweek_beginning2'] = (df['Created'] - pd.to_timedelta(df['Created'].dt.dayofweek, unit='d')).dt.normalize()
df['Cweek_ending'] = (df['Created'].where( df['Created'] == 
  (( df['Created'] + pd.tseries.offsets.Week(weekday=6) ) - pd.tseries.offsets.Week()), 
  df['Created'] + pd.tseries.offsets.Week(weekday=6))).dt.normalize()

# join tables
stores = pd.read_excel("C:\\Work\\Resources\\Store Deployment Schedule.xlsx", sheet_name="sql table")
stores.describe()
joined = pd.merge(df, stores, how='left', left_on='BU', right_on='BU')
joined = pd.merge(df, stores, how='left', on='BU')
# not working. some duplicates.

# column (series) unique values & table count, etc
stores['BU'].unique()
stores.BU.value_counts()
stores['BU'].value_counts()
stores.xs('BU', axis=1)
df['BU'].value_counts()
df['BU'].value_counts(normalize=True)
len(stores['BU'].unique())

# clear workspace
%reset


#### to do:
## find all NaN/nulls in column
## difference between dataframes (anti-join?).
## subset dataframe by id in another table





# experimenting w/ beautifulsoup4 ###

import requests

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
page
page.status_code  # 200 means downloaded successfully, 4.* or 5.* means error

page.content

from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())  # print HTML content

# finding 1 single line
# find & number all children tags
list(soup.children)  # soup.children is a list iterator
[type(item) for item in list(soup.children)]
html = list(soup.children)[2]
list(html.children)
for i, child in enumerate(list(html.children)):
    print(i, child)

body = list(html.children)[3]
list(body.children)  # all content in index 1

p = list(body.children)[1]
p
p.get_text()

# finding all instances of a tag
soup.find_all('p')  # returns a list
soup.find_all('head')
soup.find_all('title')

soup.find_all('p')[0].get_text()  # use on single element of list
soup.find('p')  # finds first instance

### classes and ids ### # Find All Instances of a Tag at Once ###
page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
soup
print(soup.prettify())

# search all p(aragraph) tag w/ class
soup.find_all('p', class_='outer-text')

# search all class
soup.find_all(class_="outer-text")  # same thing as above
soup.find_all(class_="outer-text")

# search by id
soup.find_all(id="first")

# Using CSS Selectors ###

# find all p tags inside div
soup.select("div p")  # returns list
soup.select("body div p")  # body w/ child div w/ child p
soup.select("p b")  # paragraph with bold text inside

# reference: lambda one line function
myfunc = lambda x, y: x + y
myfunc(1, 2)  # 1 + 2





#####################################################
############## Official Python Tutorial #############
### https://docs.python.org/3/tutorial/index.html ###
#####################################################



#### 3.1 Using Python as a Calculator

# 3.1.1 Numbers
2 + 2
50 - 5 * 6
(50 - 5 * 6) / 4
8 / 5  # division always returns float
# Out[12]: 1.6
8 / 4  # even if done with ints
# Out[13]: 2.0

16 // 5  # floor division
# Out[14]: 3
16 % 5   # modulo remainder
# Out[16]: 1
16 == (16 // 5) * 5 + (16 % 5)  # floor division result * divisor + remainder == first number
# Out[19]: True

3 ** 3  # powers

5 + 5 + 2
_ + 3  # last printed expression = '_' char



#### 3.1.2 Strings

# raw strings
print('some stuff here')
print('C:\some\name')
print(r'C:\some\name')  # preface with 'r' for raw string

# span multiple lines
print('''some things
and other things
printed on new lines''')

# concatenate
print('my' + ' ' + 'house' + ' is ' + str(5))
'py' 'thon'
print('several together '
      'have themselves joined')
print('py' 'thon', 'struff')  # separates w/ space

# index (subscript) strings
word = 'Python'
word[0]     # at place 0
word[:2]    # first 2 chars slice
word[-1]    # last char
word[-2]    # second to last char
word[-2:]   # last 2 chars slice. omitted second index = size of string
word[-2:6]  # (same as above)

print('''
'slice from i to j is all chars between edges'
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
''')

len(word)  # length of string
str(555)  # convert to string
555



#### 3.1.3 Lists


# indexes just like strings
squares = [1, 4, 9, 16, 25]
squares
squares[-3:]
squares[:]

# concatenate list
squares + [1, 2, 3]

# mutable - change their content
squares[0] = "lol"
squares

# add new items
squares.append(1)
squares.append(['another', 'list'])  # only appends 1 object. nested list

# assignment to slices changes object
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[0] = 'A'
# ['A', 'b', 'c', 'd', 'e', 'f', 'g']
letters[-3:] = []  # removes items
# Out[75]: ['A', 'b', 'c', 'd']

len(letters)

# slice list within list
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x[0][2]  # int
# Out[81]: 'c'
x[0][:2] # list
# Out[88]: ['a', 'b']
a
a[:] = ['slice', 'notation']  # still writes over list

x[0][:2] = ['new', 'values']
x
# Out[92]: [['new', 'values', 'c'], [1, 2, 3]]



#### 3.2 first steps towards programming

a, b, c = 0, 1, 'hi mom'  # multiple variable assignment
while a < 10:
    print(a)
    a, b = b, a+b  # right hand side is evaluated before any variable assignments occur

a, b = 0, 1
while a < 10:
    print(a, end = '--')
    a, b = b, a+b



#### 4. More Control Flow Tools


# 4.1 if
x = int(input("enter a number"))
if x < 0:
    x = 0
    print('negative chanted to 0')
elif x < 10:
    print('x is less than 10')
elif x >= 10 and x < 20:
    print('x is between 10 & 20')
else:
    print(x, 'is more than 20')


# 4.2 for
words = ['cat', 'window', 'defenestrate']
for word in words:  # iterates over items in the sequence (for each)
    print(word, len(word))

for word in words[:]:  # requires slice copy? otherwise infinite loop
    if len(word) > 6:
        words.insert(0, word)
words


# 4.3 range
for i in range(5):  # 0-4
    print(i)
for i in range(0, 10, 2):  # never includes end point
    print(i)
for i in range(10, 1, -2):
    print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):  # index of list
    print(i, a[i])
for item in a:  # easy solution
    print(item)

# enumerate
list(enumerate(a, start = 1))  # default start 0


# 4.4 break and continue

# for 'else'
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:  # runs when loop breaks w/o 'break' statement
        print(n, 'is a prime number')

for n in range(5):
    if n == 3:
        print('is 3')
    else:
        print('not 3')
    if n == 4:
        print('4 found. breaking loop')
        break  # jumps out of loop
else:
    print('end of loop')

# continue (go to beginning of loop)
for num in range(2, 10):
    if num % 2 == 0:
        print(num, "is even")
        continue
    print('number found')


# 4.5 pass

class MyEmptyClass:
    pass  # empty placeholder

def initlog(*args):
    pass  # silently ignored



### 4.6 Defining Functions ###
### 4.7 More on Defining Functions ###


### 4.7.1 Default Argument Values
def ask_ok(prompt, retries=4, reminder="try again."):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
ask_ok("here is a yes or no question")

# default argument that will change
def f(a, L=[]):  # default arg value evaluated once
    L.append(a)  # lists are mutable, so this will change the value on subsequent calls
    return L

print(f(1))
print(f(2))  # default param list accumulates each time function is run

# default argument not shared between calls (default value will reset each time)
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))


### 4.7.2 Keyword Arguments

# (invoke arguments using parameter name 'kwarg=value')

# *tuples & **dictionaries as optional formal parameters
def cheeseshop(kind, *arguments, **keywords):
    print("do you have any", kind, "?")
    print("I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("something", "arg 1?", "arg 2?", person="my keyword 1")
cheeseshop("only required param")


# 4.7.3 Arbitrary Argument Lists
def concat(*args, sep="/"):  # *arbitrary length
    return sep.join(args)

concat("earth", "venus", "mars")


# 4.7.4 Unpacking *Argument Lists
list(range(3,6))
args = [3, 6]
list(range(*args))  # unpacking from a list in function call

def parrot(voltage, action='jump'):
    print("This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it")

my_dictionary = {"voltage": "10,000", "action": "jump"}
parrot(**my_dictionary)  # unpack from dictionary


# 4.7.5 Lambda Expressions
def incrementor(n):
    return lambda x: x + n

f = incrementor(10)  # adds n to whatever num is passed
f(2)  # 12

# pass function as argument
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

pairs.sort(key=lambda pair: pair[1])
# Out[69]: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]


# 4.7.6 Documentation Strings
def fib(n = 5):
    """(Here is the docstring for this function.) Creates fibonacci sequence up to (not including) n

    Uses some clever variable reassignment + addition to create the sequence.
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()  # function with no return statement will return 'None'

fib(10)
fib()
print(fib.__doc__)  # prints function docstring

def fib2(n=5):
    """Fib function returning a list"""

    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)  # equivalent to result = result + a
        a, b = b, a+b
    return result
fib2(5)


# 4.7.7 Function Annotations
def f(ham: str, eggs: str = 'eggs') -> str:  # -> str is return annotation. doesn't affect anything.
    print("Annotations:", f.__annotations__)
    print("Arguments: ", ham, eggs, sep=';')
    return ham + ' and ' + eggs

f('myhamvariable')



### 5. Data Structures ###


# 5.1 more lists
a = [1, 2, 3]
# Out[69]: [1, 2, 3]
a.append('555')  # just 1 item
# Out[71]: [1, 2, 3, '555']
a.extend(['another', 'list', 'items'])  # multiple items
# Out[73]: [1, 2, 3, '555', 'another', 'list', 'items']
a.insert(1, 'my insertion')  # insert at index
# Out[77]: [1, 'my insertion', 2, 3, '555', 'another', 'list', 'items']
a.remove('my insertion')  # remove by value
# Out[79]: [1, 2, 3, '555', 'another', 'list', 'items']

a.pop()  # removes & returns the [last] item in the list
a.pop(1)
# Out[81]: 'items'
# Out[82]: 2
# resulting list:
# Out[85]: [1, 3, '555', 'another', 'list']

a.index('555')  # returns index
a.index('555', 1)  # finds next '555' starting at position 1
# Out[87]: 2
a.count('another')  # counts value

''.join(str(item) for item in a)  # concatenates list items
[str(item) for item in a]  # converts list items to str
list(map(str, a))          # converts list items to str
# Out[133]: ['1', '3', '555', 'another', 'list']

a2.sort()  # sorts nums then chars
# Out[135]: ['1', '3', '555', 'another', 'list']
a2.reverse()
# Out[137]: ['list', 'another', '555', '3', '1']
a2.copy()
a2[:]  # also 'shallow' copy
# Out[139]: ['list', 'another', '555', '3', '1']

a2.extend(['test', '44'])
# Out[142]: ['list', 'another', '555', '3', '1', 'test', '44']
a2.sort()
# Out[144]: ['1', '3', '44', '555', 'another', 'list', 'test']


# 5.1.1 lists as stacks
stack = [3, 4, 5]
stack.pop()  # Last-In-First-Out
# Out[147]: 5  # returned
# Out[148]: [3, 4]
stack.append(6)
# Out[152]: [3, 4, 6]


# 5.1.2 lists as queues
from collections import deque
myqueue = ['Eric', 'John', 'Michael']
queue = deque(myqueue)  # <class 'collections.deque'>

queue.popleft()  # First-In-First-Out
# returns 'Eric'
# deque(['John', 'Michael'])
queue.append('Bobbert')
# deque(['John', 'Michael', 'Bobbert'])
for item in queue:  # functions like list
    print(item)



### 5.1.3 List Comprehensions

# this...
squares = []
for x in range(10):
    squares.append(x**2)

# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# ...same as...
squares = list(map(lambda x: x**2, range(10)))

# ...same as (list comprehension)
squares = [x**2 for x in range(10)]


# this...
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]            # nested for loops
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# ...is same as
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x !=y:
            combs.append((x, y))


mylistcomp = [x for x in [1,2,3] for y in [5,6]]                # just iterates through x
# [1, 1, 2, 2, 3, 3]

mylistcomp = [y for x in [1,2,3] for y in [5,6]]                # just iterates through  y
# [5, 6, 5, 6, 5, 6]

mylistcomp_crossproducts = [x*y for x in [1, 2, 3] for y in [5, 6]]
# [5, 6, 10, 12, 15, 18]

mylistcomp_crossproducts = [x*y for x in [1, 2, 3] for y in [5, 6] if x*y >= 10]
# [10, 12, 15, 18]

mylistcomp_crossproducts = [x*y for x in [1, 2, 3] for y in [5, 6] if 10 <= x*y <= 15]   # chained comparison operators
# [10, 12, 15]

vec = [-4, -2, 0, 2, 4]
[item*2 for item in vec]             # new list with doubled values
[item for item in vec if item >= 0]  # filter the list to just include positive numbers
[abs(item) for item in vec]          # apply a function to all elements

freshfruit = ['  banana', '  loganberry  ', 'passion fruit  ']
[x.strip() for x in freshfruit]      # call a method on each element
[(x, x**2) for x in range(6)]        # create a tuple w/ calculations
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[num for elem in vec for num in elem]

# complex expressions & nested functions in list comprehensions
from math import pi
[str(round(pi, i)) for i in range (1, 6)]



### 5.1.4 Nested List Comprehensions

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

[row for row in matrix]
[i for i in range(4)]

# this...
[[row[i] for row in matrix] for i in range(4)]   # transposes matrix
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# ...same as
transposed = []
for i in range(4):
    transposed.append(row[i] for row in matrix)

# ...same as
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

transposed
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# ...same as zip: built in function to transpose
list(zip(*matrix))
# [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]



# 5.2 The del statement

# remove item from list by index
a = [-1, 1, 66, 33, 33, 1234]
del a[0]
# [1, 66, 33, 33, 1234]
del a [2:4]
# [1, 66, 1234]
del a[:]
# []
del a
a
# NameError: name 'a' is not defined



### 5.3 Tuples and Sequences

t = 12345, 54321, 'hello!'      # a tuple definition doesn't need parenthesis
t = (12345, 54321, 'hello!')    # same thing

u = t, ('another', 'tuple')
# ((12345, 54321, 'hello!'), ('another', 'tuple'))      # nested

t[0] = "won't work. tuples are immutable"
# File "<input>", line 1, in <module>

# but tuples can hold mutable objects
list1 = [1,2,3]
list2 = [4,4,4]
v = (list1, list2)
# ([1, 2, 3], [4, 4, 4])

list1.append(5)
v
# ([1, 2, 3, 5], [4, 4, 4])     # changes to list variable shown in tuple containing it


empty = ()
# ()
singleton = ('hello', )         # tuples w/ 1 item require comma
# ('hello',)
two_things = ('hello', 'how are you')
# ('hello', 'how are you')


# sequence unpacking. put tuple values into variables
t
# (12345, 54321, 'hello!')
x, y, z = t             # must be same # of items
x, y, z
# (12345, 54321, 'hello!')
x
# 12345

a, b = t[:2]            # unpack variable # of items
a, b
# (12345, 54321)



### 5.4 Sets ###

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}       # create with {}
mybasket = set(['apple', 'apple', 'orange'])                            # create with set([list])

basket
# {'banana', 'pear', 'orange', 'apple'}
mybasket
# {'orange', 'apple'}


print(basket)       # sets are unique and unordered
'orange' in basket  # membership testing
# True
'bob' in basket
# False

basket - mybasket
# {'pear', 'banana'}

a = set('abracadabra')
b = set('alacazam')

a
# {'a', 'c', 'r', 'd', 'b'}
b
# {'a', 'c', 'm', 'l', 'z'}

# set difference
a - b
# {'b', 'r', 'd'}

# set union
a | b
# {'a', 'c', 'r', 'm', 'l', 'd', 'b', 'z'}

# set intersect
a & b
# {'a', 'c'}

# set XOR
a ^ b
# {'r', 'm', 'b', 'l', 'z', 'd'}

# set comprehensions
a = {x for x in 'abracadabra'}
# {'a', 'c', 'r', 'd', 'b'}

b = {x for x in 'abracadabra' if x not in 'abc'}
# {'r', 'd'}



### 5.5. Dictionaries ###










### Interlude - playing with regex ###
import re
mystring = "this is the string I will search with regex. It has 50+ chars. All chars."
re.findall("bob", mystring)
re.search("bob", mystring)
re.search("\.", mystring)
re.findall("\.", mystring)
re.findall("(?i)w.*?l{2}", mystring)
re.search("(?i)w.*?l{2}", mystring)
re.sub("(?i)will", "bobbert", mystring)
re.findall("\d\d", mystring)
re.findall("\\d\\d", mystring)  # same thing??

mydataframe = {'col1': [1,2,3,4],
               'col2': ['here are some values', 'in the column', 'puppies 555', None]}

# none of this working
import pandas as pd
mydataframe['find num'] = mydataframe['col2'].apply(re.findall('\d\d'))

search = []
for values in mydataframe['col2']:
    search.append(re.search('\d+', values).group())

mydataframe['col2'].str.extract('\d+')

### End interlude ###









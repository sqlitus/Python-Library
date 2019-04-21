import pandas as pd
import datetime

nests = pd.read_excel(r"C:\Users\k\Documents\pokemon nest.xlsx", skiprows=1)

nests.head()

list(nests)[:8]


df = nests[['Species',
 'Spawn Density',
 'Name of Nest',
 'Google Maps link to Nest',
 'General location',
 'Location Descriptor',
 '# of Pokestops',
 'Confirmation Date']]


df = nests[list(nests)[:8]].copy()

df.head()
list(df)
len(list(df))


for i in df:
    print(i, type(i))

df.dtypes

df['Cdate'] = pd.to_datetime(df['Confirmation Date'])
df['confirmation_date_age'] = pd.to_datetime(pd.datetime.now().date()) - df['Cdate']

pd.datetime.now().date()


df['confirmation_date_age']



x=3
y=2
z=4
n=3


ar = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if (i+j+k !=n):
                ar.append([i,j,k])
ar

[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]

print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])




arr = map(int, input().split())
numbers = [20,67,3,2.6,7,74,2.8,90.8,52.8,4,3,2,5,7]
numbers.remove(max(numbers))
numbers.remove(max(numbers))
max(numbers)



def second_largest(numbers):
    count = 0
    m1 = m2 = float('-inf')
    for x in numbers:
        count += 1   # as long as this loops twice, we'll have a second largest
        if x > m2:  # look at current number, and check if larger than second largest
            if x > m1:  # if it's the largest...
                m1, m2 = x, m1  # set it as the largest, and set the former largest as second largest
            else:
                m2 = x  # if it wasn't the largest (but it's already largesr than the second largest), then make it the second largest
    return m2 if count >= 2 else None  # return a second largest if there were at least 2 numbers






students = [['Harry', -50], ['Berry', -50], ['Tina', -50], ['Akriti', -50], ['Harsh', 44]]
students

min1 = min2 = float('inf')
print(min1)

# gets us our 1st & 2nd minimums
for student in students:
    print(student)
    if student[1] < min1:
        min1, min2 = student[1], min1


for s in students:
    if student[1] < min2:
        if student[1] < min1:
            min1, min2 = student[1], min1
            print(min1, min2)
        elif student[1] != min1:
            min2 = student[1]
            print('min2 is ', min2)


print(min1, min2)

# get names of 2nd minim scores
slist = []
for student in students:
    if student[1] == min2:
        slist.append(student[0])

# print alphabetically
slist.sort()
for student in slist:
    print(student)


mylist = ['harry', 'barry', 'carry']
mylist


float(str(round(0.0556781255, 2)))

'50.123'.format('.2f')


239 / 3
round(239 / 3, 2)

56.0
round(56.0, 2)
str(56.0)
print(str(56.0))
print('%.2f' % 56.0)



list = [12]
list.insert(1, 0)
print(list)
list.insert(0, 5)
print(list)
list.insert(1, 33)
print(list)
list.insert(3, 1)
print(list)

list.remove(1)
print(list)

list.append(6)
print(list)

list.sort()
print(list)

list.pop()
print(list)

list.reverse()
print(list)

list.sort()
print(list)
list.pop(len(list)-2)
print(list)
list.pop(2)
print(list)

list.extend([5,6,7])
list

list.index(5)
list.append(1)
list
list.count(1)



mylist = []
mylist.insert(0, 5)
print(mylist)






############ PANDAS PRACTICE ##############

import pandas as pd
import numpy as np

myseries = pd.Series([2,5,8,3,7])
myseries
myseries[:2]


print(myseries)

list = myseries.tolist()
list
myseries

s2 = [2,2,2,3,3]

myseries * s2

mult = myseries * s2
mult

df = pd.DataFrame({'myseries': myseries,
              's2': s2,
              'mult': mult})


df
df[df['myseries'] == 2]

import numpy as np

df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                    "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                    "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                             pd.NaT]})


df
df.dropna(subset=['toy'])  # drop rows w/ NA column value
df['toy2'] = 'toy - ' + df['toy']

















a = "this is a string yo"
b = a.split()
a
b

"--".join(b)






#################### STRING FORMATS

num = 55.12345

print(f'my number is {num:2.2f}')
print('my number is {:2.2f}'.format(num))
















import os
os.getcwd()





####################### test LAT/LONG EXAMPLE
##### 1 - create df, round num, sample rows, export csv, create df, union, create df, merge (joined), dates, random, group by, aggregate, rename columns, merge on column+index...
##### 2 - age datediff, , groupby, agg column, rename, sort (order by), merge (join on multi-criteria), merge, rename
# (ref: dates & random, get column names)
# (ref: NUMPY)

import pandas as pd
import numpy as np

geo = pd.DataFrame({'id': [1,2,3,4],
                    'country': ['USA', 'USA', 'CAN', 'JAP'],
                    'latitude': [36.12345, 43.111, 33.1313, 90.178],
                    'longitude': [25.234, 39.818, 56.00, 30.30]
                    })
geo


geo.round({'latitude': 2, 'longitude': 2}).sample(frac=.25).to_csv("test geo data.csv", index=False)


geo_2 = pd.DataFrame({'id': [5, 6, 7],
                      'country': ['USA', 'UK', 'USA']
                      })
geo_2



out = pd.concat([geo, geo_2], ignore_index=True, sort=False)
out

geo_description = pd.DataFrame({'country_id': ['USA', 'CAN', 'UK', 'FRA'],
                                'description': ['first country to do business', 'small and centralized markets', 'expanding influence', 'not successful'],
                                'country_rank': [1, 2, 3, 4]
                                })

geo_description


out = out.merge(geo_description, how='left', left_on='country', right_on='country_id')
out



geo_events = pd.DataFrame({'date': pd.date_range('2018-01-01', '2018-01-12'),
                           'country': np.random.choice(geo['country'], 12)})

geo_events

geo_events_grouped = geo_events.groupby('country').agg('count').rename(columns={'date': 'Count'})
geo_events_grouped
geo_events_grouped.columns  # group by column became index

out.merge(geo_events_grouped, how='left', on='country')  # column & index had same name
out = out.merge(geo_events_grouped, how='left', left_on='country', right_index=True)   # (same)




##### 2 - age datediff, , groupby, agg column, rename, sort (order by), merge (join on multi-criteria)

geo_events['Age'] = pd.datetime.now() - geo_events['date']
geo_events
geo_events.groupby('country').agg({'Age': 'max'}).rename(columns={'Age': 'Oldest Age'}).sort_values('Oldest Age')
geo_mins = geo_events.groupby('country').agg({'Age': 'max'}).rename(columns={'Age': 'Oldest Age'}).sort_values('Oldest Age').merge(geo_events, how='left', left_on=['country', 'Oldest Age'], right_on=['country', 'Age']).copy()
geo_mins = geo_mins.drop('Age', 1)
geo_mins



out = out.merge(geo_mins, on='country', how='left').copy().rename(columns={'date': 'Original Date'})













### dates & randomness stuff ###

'2017-01-01'
type('2017-01-01')
pd.to_datetime('2017-01-01')

pd.to_timedelta(np.random.randn(5))
pd.to_datetime(np.random.randn(5))
np.random.randint(1, 15, 3)

pd.date_range('2018-01-01', '2018-01-12') # start to end (inclusive)
np.random.randn(5)

np.random.choice(geo['country'], 3)

pd.NaT
np.NaN
type(np.NaN)
type(pd.NaT)





### NUMPY ###

out.sum()
out.min()
out.max()
out.median()
out.count()
out['Count']
out['Count'].max()
out['Count'].count()

















################### ALGORITHMS #######################

ar = [1,2,1,2,1,3,2]
ar.count(1) // 2
ar.count(3) // 2
set(ar)

1 // 2
3 // 2
4 // 2
5 // 2
6 // 2

test = 0
test
test += ar.count(1) // 2
test


for i in range(1, 4):
    print(i)
    print(ar.count(i))


def sockMerchant(ar):

    sock_types = []
    for sock in ar:
        if sock not in sock_types:
            sock_types.append(sock)

    pairs = 0

    for sock in sock_types:
        pairs += (ar.count(sock) // 2)

    return pairs




sockMerchant(ar)



c = list(map(int, '0 0 0 0 1 0 1 0'.split()))
c

i = jumps = 0
end = len(c) - 1

while i < end:
    if i < end-1 and c[i + 2] == 0:
        i += 2
    else:
        i += 1
    jumps += 1

print(jumps)
# prints


list = [5, 6, 7, 8, 9]


def find_idx(input_list):
    total_sum = sum(input_list)
    running_total = 0

    for i in range(len(input_list)):

        running_total = running_total + input_list[i]

        ## pass 0th element
        left_sum = sum(input_list[:i])
        right_sum = sum(input_list[i + 1:])

        if left_sum == right_sum:
            # print(i, left_sum, right_sum)
            return i

    if left_sum != right_sum:
        return -1


print(find_idx(list))



### merge two dictionaries

d1 = {'chris': 1, 'laura': 2}
d1
d2 = {'sales': 54000, 'chris': 'lolol'}
d2

{**d1, **d2}

d3 = {}
d3.update(d1)
d3.update(d2)
d3

d1
d2
d3



#### 2019-04-20 - Data types review ####

# Variables
a = 5
a
b = a
b
b

b = b + 1  # b != a still
b
a

b == a


# Lists
a = [1,2,3]
a
b = a  # LISTS ARE SYNONYMS
b
a == b
a.append(7)  # AFFECTS A AND B.
a
b


a
a.count(6)  # counts OF
a.index(7)  # index OF
a.append(5) # append THIS
a.pop()     # remove & return LAST ITEM
a.sort()    # SORT ASCENDING
a.sort(reverse=True)  # SORT DESCENDING
a
a.extend('!')  # can't extend integers.
a.append('bob')
a
a.reverse()  # REVERSES LIST
a.remove(3)  # remove THIS
a.insert(1,'bob')  # insert THIS INDEX, THIS OBJECT
a
a.clear()  # EMPTIES LIST
a
b
a = [1,2,3, 'bob', 28]
b = a.copy()  # MAKES A COMPLETELY SEPARATE OBJECT. NOT A SYNONYM
a
b
a.append(7)
a
b
for item in a:
    print(type(item))

a_types = [type(item) for item in a]
a
a_types
type(a)

b.extend('!')
b
a
a.count('bob')

a

a
b
c = a+b  # COMBINE BOTH LISTS INTO ONE
c

c[:4]  # INDEX - FIRST 4 ITEMS
c[-4:] # INDEX - LAST 4 ITEMS
c[1:4] # INDEX - GRABS INDEX 1, 2, 3
c[-4:8]  # weird combo don't do this

c > 2

for item in c:
    if type(item) == 'int':
        print(item, ': yes is integer', sep='')
        if item > 2:
            print('integer is > 2')
    else:
        print(item, ': not an integer. Skipping evaluation', sep='')

type(type(5)) == "<class 'int'>"
str(type(5))

len(c)


## golf: keep list of stuff w/ high length, print last character?
longs = []
for item in c:
    if len(str(item)) > 1:
        longs.append(str(item))


len(longs[0])
longs[0][:2]
longs[0][len(longs[0])-1]
len(longs[0])-1
longs
# print last chars

list_last_char = []
for item in longs:
    last_char = item[len(item)-1]
    print(last_char)
    list_last_char.append(last_char)
list_last_char


# efficient version of above high length, print last character...
c.append('something')
c  # [1, 2, 3, 'bob', 28, 7, 1, 2, 3, 'bob', 28, 'something']
longs = []
longs_last_chars = []

for item in c:

    item_str = str(item)
    if len(item_str) > 1:
        longs.append(item_str)
        last_char = item_str[len(item_str)-1]
        longs_last_chars.append(last_char)

longs
longs_last_chars



# NEXT: DICTS, SETS, REGEX W/ STR. PANDAS.
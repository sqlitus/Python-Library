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

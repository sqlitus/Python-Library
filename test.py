#### Regex pandas test ----

import pandas as pd
import numpy as np


inc_list = pd.read_excel(r"path...\incident.xlsx")  # read raw string file location
df = inc_list.copy()

# regex calculated attributes
df['title_extracted_BU'] = df['Short description'].str.extract("(\\b\d{5}\\b)")  # double escape \b
df['title_extracted_deviceName'] = df['Short description'].str.extract("(?i)(wfm\s?\d{5}\s?[a-z]{3}\s?\d{2,3})")
df['title_extracted_deviceName_BU'] = df['title_extracted_deviceName'].str.extract("(\d{5})")

# if statement
df['high_vol'] = np.where(df['assignee change counter'] > 5, 'trouble ticket', 'regular ticket')

# switch statements
df['derived_BU'] = np.select(
    condlist=[df['title_extracted_BU'].notnull(), df['title_extracted_deviceName_BU'].notnull()],
    choicelist=[df['title_extracted_BU'], df['title_extracted_deviceName_BU']],
    default=df['BU'])
df['derived_BU_fieldUsed'] = np.select(
    condlist=[df['title_extracted_BU'].notnull(), df['title_extracted_deviceName_BU'].notnull()],
    choicelist=['short desc BU#', 'short desc device name'],
    default='BU field')


df['']


df.drop(columns='high_vol', inplace=True)
# out
df.to_excel(r"C:\Users\...\Documents\pandas_test.xlsx", index=False)









#### test time ----
import time
print('test')
time.sleep(3)
print('3 secs later')








#### test basics 11/14/2018 ----
# variables
# while loop
# for loop, list, if/else, strings
# os file manipulation
# iterating over a list. list comprehension. try/except
# functions




x = 5
y = x

x = x + 1

print(x)
print(y)
# 6, 5

x+=1
print(x)
# 7


counter = 0
while counter < 10:
    print(counter)
    counter += 1


alist = ['here', 'is', 'a', 'list']
for item in alist:
    print(f'the word is "{item}"', '(' + str(len(item)) + ' letters)')
    if len(item) % 2 == 0:
        print(item, 'is an even number')
    else:
        print(item + 'is not an even number')
    print()


## scan files. if contains allie & totals > num then COPY into folders.
# method 1: import each data file as df, then check values...?
# method 2: simple scan of data file.

import os
import re



list_of_csvs = []
for file in os.listdir(r'C:\Work\Development\py move files'):
    if file.endswith(".csv"):
        print(file)
        list_of_csvs.append(file)  # strings

        f = open(file)
        f_lines = f.readlines()




# test open & search file for data
testfile = open(r"C:\Work\Development\py move files\L1 Ticket Metrics 2017_10_15.csv")
testfile_lines = testfile.readlines()

for line in testfile_lines:
    print(line)  # string
    if line.__contains__("M"):
        print("this line contains a capital 'M'")
    if re.search("M", line):
        print("Regex finds capital 'M'")
    if re.search("(?i)alicea bush", line):
        print('Allie record')

    line_list = line.split(',')
    print(line_list)

    line_checker = 0
    line_checker_results = []
    if len(line_list) != 6:
        line_checker+=1
        line_checker_results.append(line_list)


    print('the number of created, worked, and resolved is ', line_list[2:5])
    # if re.search("(?i)alicea bush", line) and sum(line_list[2:5]) > 100:
    #     print(testfile.name, 'is a flagged file')
    # re.search("^\d+$", line_list)
    print('-----------')

print(line_checker)
print(line_checker_results)

testfile.close()



## regex on list

reglist = ['this 123', 'is 444', 'a 333', 'list to search']
r = re.compile("this")
for item in reglist:
    r.findall(item)

[re.findall("\d+", item) for item in reglist]


numlist = [3, 2, 6, 4, 5]
sum(numlist[1:3])  # sums right
type(numlist[1:3])  # list


# extract numbers from list
randomlist = ['a list', 5, '28', 7]
[s for s in randomlist if s.isdigit()]  # only operates on string...


randomlist_numbers = []
for value in randomlist:
    try:
        randomlist_numbers.append(int(value))
    except:
        continue

randomlist
randomlist_numbers


# using function
def extract_integers(list):
    for value in list:
        try:
            yield int(value)
        except:
            continue

list(extract_integers(randomlist))




convlist = ['1', '2', '5']
[int(i) for i in convlist]  # convert list of strings to integers
















#### Excel & CSV sheets ----
# identify data sheets. loop through data sheets. Read data, move files

import os

mypath = r"C:\Work\Development\py move files"
myfiles = os.listdir(mypath)  # file names

mypath

for i in len(myfiles):
    mypath.join(myfiles, file[file])



# (( List comprehension VS similar for loop ))
[f for f in os.listdir(mypath) if f.endswith('.csv')]

throwaway = []
for f in os.listdir(mypath):
    if f.endswith('.csv'):
        throwaway.append(f)

throwaway
del throwaway






import os
import xlrd
import pandas as pd



append_data = []

for file in os.listdir(r"C:\Work\Development\py move files"):
    if os.path.isfile(file):
        print(file)
        print()

#         workingfile = pd.read_csv(file)
#
#         df = workingfile.parse('sheet1', header=3)
#         append_data.append(df)
#
# append_data






os.path
os.pa
book = xlrd.open_workbook("myfile.xls")
print("The number of worksheets is {0}".format(book.nsheets))
print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(0)
print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))
for rx in range(sh.nrows):
    print(sh.row(rx))
###################################################################
##################### Official Pandas Tutorial ####################
### https://pandas.pydata.org/pandas-docs/stable/tutorials.html ###
###################################################################


############################
### 10 minutes to pandas ###
############################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



### Intro to Data Structures ###


### Series ###

# create series w/ index
from pandas._libs.writers import write_csv_rows

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
# a   -0.253536
# b    0.247352
# c    0.942270
# d    2.095199
# e    0.517629

s.index
# Index(['a', 'b', 'c', 'd', 'e'], dtype='object')

# create series
pd.Series(np.random.randn(5))           # default index = 0 -> n
# 0   -0.407519
# 1   -0.458943
# 2   -1.247311
# 3   -0.294388
# 4    0.528827

# create series from dictionary
d = {'b': 1, 'a': 0, 'c': 2}            # index: value
pd.Series(d)
# b    1
# a    0
# c    2
# dtype: int64

pd.Series(d).index                      # ordered by insertion order for Python >= 3.6
# Index(['b', 'a', 'c'], dtype='object')


s = pd.Series([1,3,5, np.nan, 6, 8])
s



### DataFrame ###

# create date series
dates = pd.date_range('20180101', periods=6)

# create dataframe with NumPy array
np.random.randn(6, 4)  # creates array of dimensions
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
df

# create dataframe with dict
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20180901'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),  # this series has multiple values
                    'D': 'a string',
                    'E': pd.Categorical(["test", "train", "bob", "tom"])})
df2
df2.dtypes












################## Pandas Cheat Sheet ##################
#### http://pandas.pydata.org/Pandas_Cheat_Sheet.pdf ####
#########################################################


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.DataFrame({
    'a': [4, 5, 6],
    'b': [7, 8, 9],
    'c': [10, 11, 12]
})

df
#    a  b   c
# 0  4  7  10
# 1  5  8  11
# 2  6  9  12









###########################################################################
##################### Intro to pandas data structures #####################
### http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/ ###
###########################################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('max_columns', 50)


### Series ###

pd.Series([7, 'Heisenberg', 3.14, -17829734, 'Happy eating!'])
pd.Series([7, 'Heisenberg', 3.14, -17829734, 'Happy eating!'], index=['a', 'b', 'c', 'd', 'e'])

# via dictionary
d = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100,
     'Austin': 450, 'Boston': None}
cities = pd.Series(d)
cities
# (INDEX, VALUE)
# Chicago          1000.0
# New York         1300.0
# Portland          900.0
# San Francisco    1100.0
# Austin            450.0
# Boston              NaN

# select items w/ index
cities['Chicago']
cities[['Chicago', 'New York']]
# Chicago     1000.0
# New York    1300.0

# boolean indexing
cities[cities < 1000]
# Austin      450
# Portland    900

cities < 1000  # results in boolean series
# Chicago          False
# New York         False
# Portland          True
# San Francisco    False
# Austin            True
# Boston           False

# change values in series
print(cities['Chicago'])
# 1000.0

cities['Chicago'] = 1400

print(cities['Chicago'])
# 1400.0

# changing values with boolean logic
cities[cities < 1000] = 750
cities
# Chicago          1400.0
# New York         1300.0
# Portland          750.0
# San Francisco    1100.0
# Austin            750.0
# Boston              NaN

# check if item in series
'Boston' in cities
# True

# arithmetic
cities_squares = np.square(cities)
cities_squares
# Chicago          1960000.0
# New York         1690000.0
# Portland          562500.0
# San Francisco    1210000.0
# Austin            562500.0
# Boston                 NaN

# add series on shared index (NaN where not found in both series)
cities[:3] + cities_squares[:2]
# Chicago     1961400.0
# New York    1691300.0
# Portland          NaN

# null checking
cities.isnull()   # returns boolean series, opposite
cities.notnull()  # returns boolean series




### DataFrame ###

# create dataframe
data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
football = pd.DataFrame(data)
football


# write & import data to csv
football.to_csv('football_data.csv', index=None)  # don't write the df index
import_data = pd.read_csv("football_data.csv")
import_data
#    year     team  wins  losses
# 0  2010    Bears    11       5
# 1  2011    Bears     8       8
# 2  2012    Bears    10       6
# 3  2011  Packers    15       1
# 4  2012  Packers    11       5
# 5  2010    Lions     6      10
# 6  2011    Lions    10       6
# 7  2012    Lions     4      12

# write & import data to Excel
football.to_excel('football_data.xlsx', index=None)  # don't write index
import_from_excel = pd.read_excel('football_data.xlsx')
import_from_excel
#    year     team  wins  losses
# 0  2010    Bears    11       5
# 1  2011    Bears     8       8
# 2  2012    Bears    10       6
# 3  2011  Packers    15       1
# 4  2012  Packers    11       5
# 5  2010    Lions     6      10
# 6  2011    Lions    10       6
# 7  2012    Lions     4      12



#############################################
############## Pandas Cookbook ##############
## https://github.com/jvns/pandas-cookbook ##
#############################################

import pandas as pd
import matplotlib.pyplot as plt

football
#    year     team  wins  losses
# 0  2010    Bears    11       5
# 1  2011    Bears     8       8
# 2  2012    Bears    10       6
# 3  2011  Packers    15       1
# 4  2012  Packers    11       5
# 5  2010    Lions     6      10
# 6  2011    Lions    10       6
# 7  2012    Lions     4      12


# 1.2 Selecting a column
football['year']

# 1.3 Plotting a column
football['year'].plot()



### Chapter 2: Selecting data ###

football['year']        # column
football[:3]            # rows
football['year'][:3]    # combined
football[:3]['year']    # combined

# 2.3 Selecting multiple columns
football[['year', 'wins']]
football[['year', 'wins']][:5]
football[['team', 'year', 'wins']][football['team'] == "Lions"]
#     team  year  wins
# 5  Lions  2010     6
# 6  Lions  2011    10
# 7  Lions  2012     4

# 2.4 Count Series Values
football['team'].value_counts()
# Lions      3
# Bears      3
# Packers    2
# Name: team, dtype: int64

top_10_teams_by_appearance = football['team'].value_counts()
top_10_teams_by_appearance
top_10_teams_by_appearance.plot(kind='bar')

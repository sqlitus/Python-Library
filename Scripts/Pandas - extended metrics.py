import pandas as pd
import numpy as np


inc_list = pd.read_excel(r"\\cewp1650\Chris Jabr Reports\ONOW Exports\incident.xlsx")  # read raw string file location
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
df.to_excel(r"C:\Users\chris.jabr\Documents\pandas_test.xlsx", index=False)


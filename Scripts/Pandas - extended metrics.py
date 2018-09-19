### Extended Metrics: adding additional fields to Incident List ###

import pandas as pd
import numpy as np


inc_list = pd.read_excel(r"\\cewp1650\Chris Jabr Reports\ONOW Exports\incident.xlsx")  # read raw string file location
df = inc_list.copy()  # create copy to not alter original


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

# more regex - concat multiple capture groups into a single string
df['derived_Lane'] = (df['Short description'].str.extract("(?i)(lane|reg|tab|pck|svr|aha)(\W{0,2}\d{2,3})")[0] + \
                      df['Short description'].str.extract("(?i)(lane|reg|tab|pck|svr|aha)(\W{0,2}\d{2,3})")[1]) \
    .str.upper() \
    .str.replace('\W', '') \
    .str.replace('(?i)(lane)', 'REG')

df['phase_num'] = (df['Short description'].str.extract("(\d{1,2}?|\d[ ]?\d/\d)([ ]?[.]\d[.]\d)")[0] + \
                   df['Short description'].str.extract("(\d{1,2}?|\d[ ]?\d/\d)([ ]?[.]\d[.]\d)")[1])


# drop 'extracted' columns (keep derived ones)
df.drop(columns=list(df.filter(regex="extracted")), inplace=True)
df.drop(columns='derived_lane_2', inplace=True)


# out
df.to_excel(r"C:\Users\chris.jabr\Documents\pandas_test.xlsx", index=False)


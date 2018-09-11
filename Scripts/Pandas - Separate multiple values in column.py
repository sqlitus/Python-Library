#### Separate multiple comma-separated values from a column ####

import pandas as pd

### my data ###
tt = pd.DataFrame({'IR': ['IR1', 'IR2', 'IR3', 'IR4', 'IR5'],
                   'category': ['vpn', 'vpn', 'teradata', 'account request', 'vpn'],
                   'approvers': ['UO1', 'UO1,UO2,UO3', 'UO1,UO2,UO3,UO4,UO5', 'UO1,SO1,SO3', 'SO3,UO1']})

tt

## create dataframe w/ rows for each ticket + approver
tt_spread = tt.set_index('IR').approvers.str.split(',', expand=True).stack().reset_index(1, drop=True).reset_index(name='approvers')
tt_spread
tt_spread['approvers'].value_counts()

## append back to original dataframe
out = pd.merge(tt, tt_spread, how='inner', on='IR')
out
out['approvers_y'].value_counts()



##### tickets #####


cr = pd.read_excel("C:\\Work\\Requests\\Don Richards\\2018-08-15 change log text mining\\tickets_type.xlsx")
df = cr
list(df)

df['approvers'] = df['approvers'].str.replace(' ','')
df['approvers']

df_split = df.set_index('Req ID').approvers.str.split(',', expand=True).stack().reset_index(1, drop=True).reset_index(name='approver')

list(df_split)

out = pd.merge(df, df_split, how='inner', on='Req ID')

out.to_excel("C:\\Work\\Requests\\Don Richards\\2018-08-15 change log text mining\\approver_dataset.xlsx",
             index=False)


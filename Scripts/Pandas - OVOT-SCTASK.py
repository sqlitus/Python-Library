### OVOT for SC Tasks - equiv of R file ###


import pandas as pd
from datetime import datetime
import glob  # pathname filtering

from sqlalchemy import engine

start_time = datetime.now()
print('Starting:', start_time.strftime('%m/%d %H:%M:%S %p'))


# grab list of correct sc_task data files from path
path = r'\\cewp1650\Chris Jabr Reports\ONOW Exports\GHD SC Task History'
sc_task_history_files = glob.glob(path+'/*sc_task*.xlsx')


def import_and_merge_files_and_clean(files):

    # concat files
    df = pd.concat((pd.read_excel(file) for file in files), ignore_index=True) \
        .drop_duplicates()

    # ALTERNATE (VERBOSE) METHOD
    # df = pd.DataFrame()
    # for file in files:
    #     data = pd.read_excel(file)
    #     df = pd.concat([df, data], ignore_index=True)
    #     df = df.drop_duplicates()

    # exclude Start == End records via anti-join (Keep in A not in B)
    filter_out = df[df['Start'] == df['End']].copy()
    df = df.merge(filter_out, how='left', indicator=True)
    df = df[df['_merge'] == 'left_only'].drop(columns='_merge')

    return df


# compile history
team_history = import_and_merge_files_and_clean(sc_task_history_files)


# get all distinct tasks
distinct_tasks = team_history[['Number']].drop_duplicates().reset_index(drop=True)
# team_history['Number'].unique()  ## ALTERNATE METHOD


# create calendar table for last x weeks
# start x weeks mondays ago: current date, minus weekday num to get to Monday, minus weeks
calendar = pd.DataFrame({
    'Date': pd.date_range(
        datetime.now().date()
        - pd.Timedelta(days=int(datetime.now().strftime('%u')))
        - pd.Timedelta(days=(7*14-1))
        , datetime.now().date())})
calendar['Datetime'] = calendar['Date'] + pd.Timedelta(8, unit='h')


# construct open volume list by day
ovot = pd.DataFrame()
for i in range(calendar.shape[0]):

    insert_day = distinct_tasks \
        .assign(Date=calendar['Date'][i], Datetime=calendar['Datetime'][i]) \
        .merge(team_history)

    insert_day = insert_day[
        (insert_day['Start'] <= insert_day['Datetime'])
        & ((insert_day['Datetime'] < insert_day['End'])
           | ((insert_day['End'].isnull()) & (insert_day['Datetime'] < insert_day['Closed']))
           | ((insert_day['End'].isnull()) & (insert_day['Closed'].isnull())))
    ]

    ovot = pd.concat([ovot, insert_day], ignore_index=True)
## TODO: Number column name

print('Exporting now at', datetime.now().strftime('%m/%d %H:%M:%S %p'), '; Elapsed time:', (datetime.now() - start_time))
ovot.to_excel(path+'\\ovot_GHD_tasks2.xlsx', index=False)
print('DONE.', '\nStart time:', start_time.strftime('%m/%d %H:%M:%S %p'),
      '\nEnd time:', datetime.now().strftime('%m/%d %H:%M:%S %p'), '\nElapsed time:', (datetime.now() - start_time))




'''
reference: excelwriter

# print('Creating Excel Writer object', datetime.now().strftime('%m/%d %H:%M:%S %p'), '; Elapsed time:', (datetime.now() - start_time))
# writer = pd.ExcelWriter(path+'\\ovot_GHD_tasks3.xlsx', engine='xlsxwriter')  # using xlsxwriter library
# ovot.to_excel(writer, index=False)
# print('Exporting now at', datetime.now().strftime('%m/%d %H:%M:%S %p'), '; Elapsed time:', (datetime.now() - start_time))
# writer.save()
# writer.close()
'''
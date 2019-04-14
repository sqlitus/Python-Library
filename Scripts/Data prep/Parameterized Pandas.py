#### Pandas data prep script; parameterized to accept any I/O ####

# Purpose:
"""
Purpose:
parameterized input/output any excel file, run data prep algorithms, output file

Directions:
Run -> Edit Configurations -> (Choose python template) -> (Paste in arguments verbatim, no quotes)

TODO:
make configurations work with any filename. Currently can't work with spaces (quoted arguments??)
"""



import pandas as pd
import os
import argparse



def get_args():
    """
    point to Excel file to import
    :return:
    """

    parser = argparse.ArgumentParser(description='Get some input excel data. Make a column. Output resulting DF')

    # Arguments
    parser.add_argument('input_file', type=str, help='input Excel data file')
    parser.add_argument('output_file', type=str, help='output path and Excel filename')

    # Compile
    args = parser.parse_args()
    return args



def main():
    """
    imports excel file, renames columns, creates calculated columns, exports to excel
    :return:
    """

    args = get_args()
    input_file = args.input_file
    output_file = args.output_file

    # Import file
    try:
        my_df = pd.read_excel(input_file)  # read raw string file location
        print(f'Data imported successfully.\nNum rows: {my_df.shape[0]}\nNum columns: {my_df.shape[1]}')
    except:
        print("ERROR: Data NOT imported successfully. Check filetype")

    # Change symbols in column names so I can view the DF in pycharm
    my_df.columns = my_df.columns.str.replace("%", "Percent")

    # CALC: first 4 chars of another columns
    my_df['first year'] = my_df['Years'].str[:4]  # first 4 chars

    # OUTPUT: df w/ new columns
    my_df.to_excel(output_file, index=False)



if __name__ == '__main__':
    main()

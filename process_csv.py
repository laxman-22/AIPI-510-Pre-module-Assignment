"""
Author: Aryan Laxman Sirohi

This file contains all the function definitions to process any CSV file in this directory

"""

# Necessary libraries
import pandas as pd


"""
Function that counts the number of columns in the CSV file

@params pandas dataframe containing CSV file contents
@returns the number of columns in the CSV file
"""
def count_columns(df):
    return df.shape[1]


"""
Function that counts the number of rows in the CSV file

@params pandas dataframe containing CSV file contents
@return the number of rows in the CSV file
"""
def count_rows(df):
    return df.shape[0]


"""
Function that retrieves all the names of the columns in the CSV file

@params pandas dataframe containing CSV file contents
@return a list of the column names in the CSV file
"""
def get_column_names(df):
    return list(df.columns.values)

"""
If the tool is invoked on its own, proceed with processing the CSV file

"""
if __name__ == "__main__":
    df = pd.read_csv("sample_data.csv")
    print("Processing CSV...\n")
    print("Number of Columns: ", count_columns(df))
    print("Number of Rows: ", count_rows(df))
    print("Column Names: ", get_column_names(df))
    print("\nDone")


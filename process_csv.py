"""
Author: Aryan Laxman Sirohi

This file contains all the function definitions to process any CSV file in this directory

"""

# Necessary libraries
import pandas as pd



def count_columns(df):
    """
    Function that counts the number of columns in the CSV file

    Parameters: Pandas dataframe containing CSV file contents
    Returns: Number of columns in the CSV file
    """
    return df.shape[1]


def count_rows(df):
    """
    Function that counts the number of rows in the CSV file

    Parameters: Pandas dataframe containing CSV file contents
    Returns: Number of rows in the CSV file
    """
    return df.shape[0]



def get_column_names(df):
    """
    Function that retrieves all the names of the columns in the CSV file

    Parameters: Pandas dataframe containing CSV file contents
    Returns: A list of the column names in the CSV file
    """
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


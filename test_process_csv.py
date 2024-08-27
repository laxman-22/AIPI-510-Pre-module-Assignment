"""
Author: Aryan Laxman Sirohi

This file contains the test cases for each function in process_csv.py.
"""

# Necessary libraries
import pytest
from process_csv import count_columns, count_rows, get_column_names
import pandas as pd

# Read the CSV file
df = pd.read_csv("sample_data.csv")

# Testcases for each function with expected values based on the sample CSV data
def test_count_columns():
    assert count_columns(df) == 3

def test_count_rows():
    assert count_rows(df) == 16

def test_get_column_names():
    assert get_column_names(df) == ['Name', 'HEX', 'RGB']
    assert isinstance(get_column_names(df), list)



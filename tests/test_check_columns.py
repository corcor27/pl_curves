#!/usr/bin/env python3
from pl_curve import check_columns
import pandas


def test_check_columns_correct():
    '''
    Checks all columns in the data frame sum to 1
    Parameters
    ----------
    dataframe
        The data frame to check
    Returns
    -------
    Bool
        False if a column doesn't sum to 1, True if they all do
    '''
    for col in dataframe.columns:
        total = sum(dataframe.loc[:, col])
        # print(col, "total=", total)
        if total < 0.9999 or total > 1.0001:
            # print("Error column ", col, "doesn't sum to 1.0")
            return False
    return True


def test_check_columns_incorrect():
    df = pandas.DataFrame([0.1, 0.8])
    assert check_columns(df) is False

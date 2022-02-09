"""
    @ Laurenz

    Script to clean date formats.
"""

import pandas as pd


def fix_date_value(original_date, replacement="/", to_replace=["."]):
    """
    Replaces "." with "/" and strips all white spaces.

    :param original_date: str
    :param replacement: str, optional
    :param to_replace: list, optional
    :return fixed_date: str
    """
    for replace_string in to_replace:
        fixed_date = original_date.replace(replace_string, replacement)
    fixed_date = "".join(fixed_date.split())
    return fixed_date


def load_data(filename):
    data = pd.read_csv(filename)
    return data


def fix_file(data, labels_to_fix):
    """
    Calls the fix_date_value function for each element with label in <labels_to_fix>
    :param data: Pandas.DataFrame
    :param labels_to_fix: list
    :return data: Pandas.DataFrame
    """
    for i, line in enumerate(data.iterrows()):
        for label in labels_to_fix:
            date = line[1][label]
            data.loc[i, label] = fix_date_value(date)
    return data


if __name__=='__main__':
    filename = "test.csv"
    labels_to_fix = ["Datum"]

    data = load_data(filename)
    data_fixed = fix_file(data, labels_to_fix)
    data_fixed.to_csv(filename[:-4]+"_fixed_dates.csv")

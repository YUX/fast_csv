import pandas as pd

from fast_csv import fast_csv


def read_csv(p):
    assert type(p) == str
    data = pd.read_csv(p)
    optimized_data = fast_csv.reduce_data(data)
    return optimized_data

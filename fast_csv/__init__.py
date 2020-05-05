import pandas as pd

from fast_csv import fast_csv as fc


def read_csv(p):
    assert type(p) == str
    data = pd.read_csv(p)
    optimized_data = fc.compression(data)
    return optimized_data


def reduce_df(data):
    assert type(data) == pd.core.frame.DataFrame
    optimized_data = fc.compression(data)
    return optimized_data

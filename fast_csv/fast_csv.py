import numpy as np


def compression(data):

    for col in data.columns:
        col_type = data[col].dtypes
        if str(col_type)[:3] == 'int':
            c_min = data[col].min()
            c_max = data[col].max()
            if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                data[col] = data[col].astype(np.int8)
            elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                data[col] = data[col].astype(np.int16)
            elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                data[col] = data[col].astype(np.int32)
            elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                data[col] = data[col].astype(np.int64)
        elif str(col_type)[:5] == 'float':
            c_min = data[col].min()
            c_max = data[col].max()
            if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                data[col] = data[col].astype(np.float16)
            elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                data[col] = data[col].astype(np.float32)
            else:
                data[col] = data[col].astype(np.float64)
        elif col_type == 'object':
            num_unique_values = len(data[col].unique())
            num_total_values = len(data[col])
            if num_unique_values / num_total_values <= 0.5:
                data.loc[:, col] = data[col].astype('category')
            else:
                data.loc[:, col] = data[col]

    return data

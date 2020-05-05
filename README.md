[![Build Status](https://travis-ci.com/YUX-IO/fast_csv.svg?branch=master)](https://travis-ci.com/YUX-IO/fast_csv)
![PyPI - Downloads](https://img.shields.io/pypi/dm/fast_csv?color=4AC41C)
[![Coverage Status](https://coveralls.io/repos/github/YUX-IO/fast_csv/badge.svg?branch=master)](https://coveralls.io/github/YUX-IO/fast_csv?branch=master)
[![codebeat badge](https://codebeat.co/badges/82ca9fd2-b2e1-439e-b0ac-54fc948127f7)](https://codebeat.co/projects/github-com-yux-io-fast_csv-master)
## requirements

- Pandas
- Numpy

## installation

`pip install fast_csv`

`!pip install fast_csv` for Google Colab or Kaggle notebook

## usage

```python
import fast_csv as fc
data = fc.read_csv('$PATH/$FILE.csv')
```

```python
import pandas as pd
import fast_csv as fc

data = fc.reduce_df(pd.DataFrame())
```

## vs pd.read_csv

See `data.info()`

- it reduces 50% of memory usage on average
- it reduces 90%+ of memory usage on a good day

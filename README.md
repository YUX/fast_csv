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

## vs pd.read_csv

See `data.info()`

- it reduces 50% of memory usage on average
- it reduces 90%+ of memory usage on a good day


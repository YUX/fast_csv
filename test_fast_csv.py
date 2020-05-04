import fast_csv as fc
import pandas as pd
import unittest


class TestFastCsv(unittest.TestCase):
    """
    Test fast_csv.read_csv()
    """

    def test_read_csv(self):
        test_data = {'int8': [1, 2], 'int16': [32760, -32700], 'int32': [214748364, -21474837], 'int64': [-922337203685477580, 922337203685477580], 'float16': [3.1, 3.14],
                     'float32': [1e3, 3.14], 'float64': [0.1, -1e10], 'object': ['pi', 'pi']}
        test_df = pd.DataFrame(data=test_data)
        for col in test_df:
            test_df[str(col)] = test_df[str(col)].astype(str(col))
        test_df.to_csv('test.csv', index=False)

        data = fc.read_csv('test.csv')
        self.assertIsInstance(data, pd.core.frame.DataFrame)
        self.assertEqual(len(data), 2)


if __name__ == '__main__':
    unittest.main()

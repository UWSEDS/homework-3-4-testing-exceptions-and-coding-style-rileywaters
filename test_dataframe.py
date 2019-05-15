'''Runs unit tests for read_weather_data()'''

import unittest
from dataframe import read_weather_data

class UnitTests(unittest.TestCase):
    '''Contains unit test functions'''

    def test_one_row(self):
        '''Tests that the dataframe has at least one row'''

        data_frame = read_weather_data()
        self.assertTrue(data_frame.shape[0] >= 1)

    def test_no_nan(self):
        '''Tests that there are no nan values'''

        data_frame = read_weather_data()
        self.assertFalse(data_frame.isnull().values.any())

if __name__ == '__main__':
    unittest.main()

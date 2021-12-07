"""THIS IS THE DATAMANAGER CLASS"""
import pandas as pd
from faker import Faker


class DataManager:
    """ This Class is used to get values from external source"""

    def __init__(self):
        self.fake = Faker()

    @staticmethod
    def get_data(filename: str):
        """THIS IS GET DATA"""
        return pd.read_csv(filename).itertuples(index=False, name=None)

    def generate_data(self):
        """THIS WILL GENERATE DATA"""
        data_frame = self.generate_data_csv()
        path = '/home/myuser/tests/test_data/values.csv'
        data_frame.to_csv(path, sep=',')
        return path

    def generate_data_csv(self):
        """THIS WILL CREATE DATAFRAME"""
        data_frame = pd.DataFrame(columns=('value_1', 'value_2', 'sum', 'multiply', 'divide'))
        for i in range(self.fake.random_int(10, 50)):
            x_values = self.fake.random_int(2, 100)
            y_values = self.fake.random_int(2, 100)
            stuff = [x_values, y_values, x_values + y_values
                             , x_values * y_values, x_values / y_values]
            # pylint: disable=unnecessary-comprehension
            data_frame.loc[i] = [i for i in stuff]
        return data_frame

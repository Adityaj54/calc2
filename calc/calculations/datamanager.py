import pandas as pd
from faker import Faker


class DataManager:
    """ This Class is used to get values from external source"""

    def __init__(self):
        self.fake = Faker()

    @staticmethod
    def get_data(filename: str):
        return pd.read_csv(filename).itertuples(index=False, name=None)

    def generate_data(self):
        df = self.generate_data_csv()
        path = '/home/myuser/tests/test_data/values.csv'
        df.to_csv(path, sep=',')
        return path

    def generate_data_csv(self):
        data_frame = pd.DataFrame(columns=('value_1', 'value_2', 'sum', 'multiply', 'divide'))
        for i in range(self.fake.random_int(10, 50)):
            x = self.fake.random_int(2, 100)
            y = self.fake.random_int(2, 100)
            stuff = [x, y, x + y, x * y, x / y]
            data_frame.loc[i] = [i for i in stuff]
        return data_frame

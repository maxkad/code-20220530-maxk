"""
Class: Generic class
Author: Max
Date: 30/05/2022

Description: support reading files.
"""

import pandas as pd


class ReadData:
    data = pd.DataFrame

    def __init__(self, path, file_name):
        self.path = path
        self.file_name = file_name

    def get_data(self):
        return self.data

    def display_summary(self):
        print("Source data file name: " + self.file_name)
        print("Source data summary:")
        print('--------------------')
        print(self.data.info())

    def display_file_location(self):
        print("File Location: {}".format(self.path + self.file_name))



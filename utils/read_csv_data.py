"""
Module: read CSV file
Author: Max
Date: 30/05/2022

Description: reads CSV file.
"""


import pandas as pd
from utils.read_data import ReadData
from pathlib import Path

root = Path('/')


class CSVReadData(ReadData):
    """
        Class to read CSV file.

        Attribute:
        ----------

        Methods:
        --------



        """

    def __init__(self, path, file_name):
        super().__init__(path, file_name)

    def read_csv_data(self):
        print("Start reading source data: read_csv_data()")
        self.data = pd.read_csv(root / self.path / self.file_name)

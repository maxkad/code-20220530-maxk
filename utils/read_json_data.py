"""
Module: read JSON file
Author: Max
Date: 30/05/2022

Description: reads JSON file.
"""

import pandas as pd
from utils.read_data import ReadData
from pathlib import Path

root = Path('/')


class JSONReadData(ReadData):
    """
    Class to read JSON file.

    Attribute:
    ----------

    Methods:
    --------



    """
    def __init__(self, path, file_name):
        super().__init__(path, file_name)

    def read_json_data(self):
        print("Start reading source data: read_json_data()")
        self.data = pd.read_json(root / self.path / self.file_name)

"""
Main file:
Author: Max
Date: 30/05/2022

Description: reads patient details data in JSON format and calculates BMI for each patient.
"""

import pandas as pd
import os
from utils import read_json_data as ds
from calculate_bmi import calculate_patient_bmi as bmi

dir_name = os.path.dirname(__file__)

# logging.basicConfig(filename='warning.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
# logging.warning('This will get logged to a file')



print("This is the beginning of patients BMI task:")
print('-------------------------------------------')

def read_json_file(input_path: str, json_file_name: str) -> pd.DataFrame:

    data_source_obj = ds.JSONReadData(input_path, json_file_name)
    data_source_obj.display_file_location()
    data_source_obj.read_json_data()
    data_source_obj.display_summary()
    return data_source_obj.get_data()


def print_patient_data(patient_df):
    print("Printing patients dataframe:")
    print(patient_df)


def main():

    # can go into a config file
    list_of_bmi_ranges = [18.4, (18.5, 24.9), (25, 29.9), (30, 34.9), (35, 39.9), 40]
    input_path = dir_name + '/calculate_bmi/data'
    json_file_name = "patient_details.json"

    patient_details_df = read_json_file(input_path, json_file_name)
    print(patient_details_df)

    bmi_obj = bmi.CalculatePatientBMI(patient_details_df, list_of_bmi_ranges)
    bmi_obj.calculate_bmi()
    print(bmi_obj.get_patient_details())
    bmi_obj.calculate_bmi_metrics()
    print(bmi_obj.get_patient_details())
    total_bmi_category = bmi_obj.count_category_by_bmi_range((25, 29.9))
    print(total_bmi_category)
    total_bmi_category = bmi_obj.count_category_by_bmi_category('Overweight')
    print(total_bmi_category)


if __name__ == '__main__':
    main()


























# """
# This is my main script
#
# Author: Max Kadoche
#
# """
#
# import pandas as pd
#
# import logging
#
# from calculate_bmi import read_json_data as ds
#
#
# def read_json_file(input_path: str, json_file_name: str) -> pd.DataFrame:
#
#     patients_data = ds.JSONReadData(input_path, json_file_name)
#     # ds.display_file_location(patients_data.path, patients_data.file_name)
#     patients_data.read_json_data()
#     patients_data.display_summary()
#     return patients_data.get_data()
#
#
# def main():
#
#     # can go into a config file
#     list_of_bmi_ranges = [18.4, (18.5, 24.9), (25, 29.9), (30, 34.9), (35, 39.9), 40]
#     input_path = "/home/maxk/PycharmProjects/tesco/data"
#     json_file_name = "patient_details.json"
#     patient_df = read_json_file(input_path, json_file_name)
#
#
#
# if __name__ == '__main__':
#     main()
#








# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

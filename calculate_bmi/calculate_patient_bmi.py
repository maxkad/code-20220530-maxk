"""
Module: calculate patients bmi
Author: Max
Date: 30/05/2022

Description: Enrich the patient details and calculates the patients bmi.
"""

import pandas as pd


class CalculatePatientBMI:
    """
        Class to read JSON file.

        Attribute:
        ----------



        Methods:
        --------



        """

    patient_details_df = pd.DataFrame
    list_of_bmi_ranges = list()

    def __init__(self, patient_details_df: pd.DataFrame, list_of_bmi_ranges: list):
        """
            :param patient_details_df: patients DataFrame.
            :param list_of_bmi_ranges: list: BMI category ranges.

        """
        self.patient_details_df = patient_details_df
        self.list_of_bmi_ranges = list_of_bmi_ranges

    def get_patient_details(self):
        return self.patient_details_df

    def calculate_bmi(self):
        print("Calculating patients BMI:")
        print('-------------------------')
        self.patient_details_df['bmi'] = self.patient_details_df['WeightKg'] / (self.patient_details_df['HeightCm'] / 100) ** 2

    def calculate_bmi_metrics(self):
        """:param

        """
        print("Calculating BMI metrics: {bmi_category, health_risk} columns:")
        print('-------------------------------------------------------------')

        self.patient_details_df.loc[(self.patient_details_df['bmi'] <= self.list_of_bmi_ranges[0]), ['bmi_category', 'health_risk']] \
            = ['Underweight', 'Malnutrition risk']
        self.patient_details_df.loc[(self.patient_details_df['bmi'] >= self.list_of_bmi_ranges[1][0]) & (self.patient_details_df['bmi']
                                    <= self.list_of_bmi_ranges[1][1]), ['bmi_category', 'health_risk']] = ['Normal weight', 'Low risk']
        self.patient_details_df.loc[(self.patient_details_df['bmi'] >= self.list_of_bmi_ranges[2][0]) & (self.patient_details_df['bmi']
                                    <= self.list_of_bmi_ranges[2][1]), ['bmi_category', 'health_risk']] = ['Overweight', 'Enhanced risk']
        self.patient_details_df.loc[(self.patient_details_df['bmi'] >= self.list_of_bmi_ranges[3][0]) & (self.patient_details_df['bmi']
                                    <= self.list_of_bmi_ranges[3][1]), ['bmi_category', 'health_risk']] = ['Moderately obese', 'Medium risk']
        self.patient_details_df.loc[(self.patient_details_df['bmi'] >= self.list_of_bmi_ranges[4][0]) & (self.patient_details_df['bmi']
                                    <= self.list_of_bmi_ranges[4][1]), ['bmi_category', 'health_risk']] = ['Severely obese', 'High risk']
        self.patient_details_df.loc[(self.patient_details_df['bmi'] >= self.list_of_bmi_ranges[5]), ['bmi_category', 'health_risk']] \
            = ['Very severely obese', 'Very high risk']

    def count_category_by_bmi_category(self, bmi_category: str) -> int:
        """
            :param bmi_category: str: bmi categoty type.
            :return int: the number of patients within the category.

        """
        print("Counting the total number of patients by bmi_category: " + bmi_category)
        print('-----------------------------------------------------------------------')
        return self.patient_details_df.loc[(self.patient_details_df['bmi_category'] == bmi_category), 'bmi_category'].count()

    def count_category_by_bmi_range(self, bmi_range: (float, float)) -> int:
        """
            :param bmi_range: tuple: bmi category range.
            :return int: the number of patients within the range.
        """
        print("Counting the total number of patients by bmi range: %s" % (bmi_range,))
        print('-----------------------------------------------------------------------')
        return self.patient_details_df.loc[(self.patient_details_df['bmi'] >= bmi_range[0]) & (self.patient_details_df['bmi']
                                                                                               <= bmi_range[1]), 'bmi'].count()
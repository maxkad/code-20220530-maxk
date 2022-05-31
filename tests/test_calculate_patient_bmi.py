"""
Module: Unit test
Author: Max
Date: 30/05/2022

Description: testing patients bmi methods.
"""

import pandas as pd
import json
import unittest
from calculate_bmi.calculate_patient_bmi import CalculatePatientBMI


class TestCalculatePatientBMI(unittest.TestCase):
    list_of_bmi_ranges = [18.4, (18.5, 24.9), (25, 29.9), (30, 34.9), (35, 39.9), 40]

    # patients data
    test_patient_details = '[{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}, ' \
                           '{"Gender": "Male", "HeightCm": 172, "WeightKg": 85}]'

    a_json = json.loads(test_patient_details)
    test_patient_details_df = pd.DataFrame.from_dict(a_json)

    bmi_obj = CalculatePatientBMI(test_patient_details_df, list_of_bmi_ranges)
    bmi_obj.calculate_bmi()
    bmi_obj.calculate_bmi_metrics()
    print(bmi_obj.get_patient_details())

    def test_count_category_by_bmi_category(self):
        print("Unit test starting for method: count_category_by_bmi_category")
        self.assertEqual(self.bmi_obj.count_category_by_bmi_category('Overweight') == 2, True)
        # pass

    def test_count_category_by_bmi_range(self):
        print("Unit test starting for method: count_category_by_bmi_range")
        self.assertEqual(self.bmi_obj.count_category_by_bmi_range((25, 29.9)) == 2, True)
        # pass


if __name__ == '__main__':
    unittest.main()

import unittest
import web_services.conversions.formulas as formulas


class FormulaTests(unittest.TestCase):

    def test_kilometers_to_miles(self):
        kilometer_test_values = [
            {'value': 3, 'expected_value': 1.86},
            {'value': 3.0, 'expected_value': 1.86},
            {'value': 3.5, 'expected_value': 2.17},
            {'value': 2375, 'expected_value': 1475.75},
            {'value': 22.698, 'expected_value': 14.10},
            {'value': 0.0, 'expected_value': ValueError},
            {'value': -10.5, 'expected_value': ValueError}
        ]

        for item in kilometer_test_values:
            try:
                self.assertEqual(
                    formulas.kilometers_to_miles(kilometers=item.get('value')),
                    item.get('expected_value'))
            except ValueError as e:
                if isinstance(e, item.get('expected_value')):
                    pass

    def test_miles_to_kilometers(self):
        miles_test_values = [
            {'value': 3, 'expected_value': 4.83},
            {'value': 3.0, 'expected_value': 4.83},
            {'value': 3.5, 'expected_value': 5.63},
            {'value': 2375, 'expected_value': 3822.19},
            {'value': 22.698, 'expected_value': 36.53},
            {'value': 0.0, 'expected_value': ValueError},
            {'value': -10.5, 'expected_value': ValueError}
        ]

        for item in miles_test_values:
            try:
                self.assertEqual(
                    formulas.miles_to_kilometers(miles=item.get('value')),
                    item.get('expected_value'))
            except ValueError as e:
                if isinstance(e, item.get('expected_value')):
                    pass

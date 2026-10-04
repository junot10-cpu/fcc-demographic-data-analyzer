"""Learning tests for Junot's dataset; these are not the official FCC tests."""
import contextlib
import io
import unittest

from demographic_data_analyzer import calculate_demographic_data


class DemographicDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Calculate once, without printing, and share the results across tests.
        cls.results = calculate_demographic_data(print_data=False)

    def test_race_count(self):
        expected = {
            'White': 27816,
            'Black': 3124,
            'Asian-Pac-Islander': 1039,
            'Amer-Indian-Eskimo': 311,
            'Other': 271
        }
        self.assertEqual(self.results['race_count'].to_dict(), expected)

    def test_average_age_men(self):
        # The function must return the expected average, rounded to one decimal.
        self.assertEqual(self.results['average_age_men'], 39.4)

    def test_percentage_bachelors(self):
        self.assertEqual(self.results['percentage_bachelors'], 16.4)

    def test_higher_education_rich(self):
        self.assertEqual(self.results['higher_education_rich'], 46.5)

    def test_lower_education_rich(self):
        self.assertEqual(self.results['lower_education_rich'], 17.4)

    def test_min_work_hours(self):
        self.assertEqual(self.results['min_work_hours'], 1)

    def test_rich_percentage(self):
        self.assertEqual(self.results['rich_percentage'], 10.0)

    def test_highest_earning_country(self):
        self.assertEqual(self.results['highest_earning_country'], 'Iran')

    def test_highest_earning_country_percentage(self):
        self.assertEqual(self.results['highest_earning_country_percentage'], 41.9)

    def test_top_IN_occupation(self):
        self.assertEqual(self.results['top_IN_occupation'], 'Prof-specialty')

    def test_print_data_false_is_silent(self):
        captured_output = io.StringIO()
        with contextlib.redirect_stdout(captured_output):
            calculate_demographic_data(print_data=False)
        self.assertEqual(captured_output.getvalue(), '')


if __name__ == '__main__':
    unittest.main(verbosity=2)

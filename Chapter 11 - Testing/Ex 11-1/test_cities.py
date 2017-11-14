import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for city_functions.py"""
    def test_city_country(self):
        """Does Auckland, New Zealand work?"""
        formatted_city_country = city_country("Auckland", "New Zealand")
        self.assertEqual(formatted_city_country, "Auckland, New Zealand")

    def test_city_country_population(self):
        """Does Shenzhen, China - 11910000 work?"""
        formatted_city_country = city_country("Shenzhen", "China", "11910000")
        self.assertEqual(formatted_city_country, "Shenzhen, China - population 11910000")


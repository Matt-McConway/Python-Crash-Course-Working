from employee import Employee
import unittest

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp = Employee("Bob", "Seddon", 10000)

    def test_default_raise(self):
        self.emp.give_raise()
        self.assertEqual(self.emp.annual_salary, 15000)

    def test_10k_raise(self):
        self.emp.give_raise(10000)
        self.assertEqual(self.emp.annual_salary, 20000)
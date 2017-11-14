class Employee():
    def __init__(self, first, last, salary):
        self.first_name = first
        self.last_name = last
        self.annual_salary = int(salary)

    def give_raise(self, raise_=5000):
        self.annual_salary += int(raise_)

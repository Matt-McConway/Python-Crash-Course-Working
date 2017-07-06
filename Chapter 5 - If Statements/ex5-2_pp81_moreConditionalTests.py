"""
5-2. More Conditional Tests: You don’t have to limit the number of tests you
     create to 10 . If you want to try more comparisons, write more tests and
     add them to conditional_tests.py.
     Have at least one True and one False result for each of the following:
     •	Tests for equality and inequality with strings
     •	Tests using the lower() function
     •	Numerical tests involving equality and inequality, greater than and
        less than, greater than or equal to, and less than or equal to
     •	Tests using the and keyword and the or keyword
     •	Test whether an item is in a list
     •	Test whether an item is not in a list
"""
pizza = "Pepperoni"
print("String Equality")
print(pizza == "Pepperoni")
print(pizza == "Cheese")
print(pizza != "Pepperoni")
print(pizza != "Cheese")
print()

print("Using .lower()")
print(pizza.lower() == "pepperoni")
print(pizza.lower() == "Pepperoni")
print()

print("Numerical equality")
print(5 == 3)
print(5 != 3)
print(5 > 3)
print(5 < 3)
print(3 >= 3)
print(3 <= 5)
print()

num1 = 22
num2 = 11
print("And/Or")
print(num1 > 30 or num1 < num2)
print(num1 > 30 and num1 < num2)
print()

print("List contents check")
weather = ["stormy", "raining", "sunny"]
print("windy" in weather)
print("stormy" in weather)

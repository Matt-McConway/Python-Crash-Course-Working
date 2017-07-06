"""
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
     describing each test and your prediction for the results of each test.
     Your code should look something like this:
        car = 'subaru'
        print("Is car == 'subaru'? I predict True.")
        print(car == 'subaru')
        print("\nIs car == 'audi'? I predict False.")
        print(car == 'audi')

     •	Look closely at your results, and make sure you understand why each
        line evaluates to True or False.
     •	Create at least 10 tests. Have at least 5 tests evaluate to True and
        another 5 tests evaluate to False.
"""

pizza = "Pepperoni"
print("Is pizza == Pepperoni? I predict True.")
print(pizza == "Pepperoni")
print("Is pizza.lower() == pepperoni? I predict True.")
print(pizza.lower() == "pepperoni")
print("Is pizza still == Pepperoni? I predict True.")
print(pizza == "Pepperoni")
print("Is pizza == cheese? I predict False.")
print(pizza == "cheese")
print("Is pizza == Cheese? I predict False.")
print(pizza == "Cheese")


pizza = "Cheese"
print("Pizza has been changed to Cheese")
print("Is pizza.lower() == cheese? I predict True.")
print(pizza.lower() == "cheese")
print("Is pizza != Cheese? I predict False.")
print(pizza != "Cheese")
print("Is pizza != Pepperoni? I predict True.")
print(pizza != "Pepperoni")
print("Is pizza.lower() == pepperoni? I predict False.")
print(pizza.lower() == "pepperoni")
print("Is pizza == Pepperoni? I predict False.")
print(pizza == "Pepperoni")

"""

"""

sandwich_orders = ["BLT", "Pastrami", "Bacon & Egg", "Pastrami", "Steak",
                   "Chicken & Avocado", "Pastrami"]
finished_sandwiches = []

print("This restaurant is out of Pastrami!")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich")
    finished_sandwiches.append(sandwich)

print("Your sandwich should be in the list below")
print(finished_sandwiches)

"""

"""

favorite_numbers = {"Matt": [3, 1, 5],
                    "Joe": [12],
                    "John": [13, 4],
                    "Samantha": [16, 32, 64],
                    "Simone": [32]
                   }

for name, numbers in favorite_numbers.items():
    if len(numbers) > 1: # Added this for correct pluralisation :)
        print(name + "\'s favorite numbers are:")
    else:
        print(name + "\'s favorite number is:")
    for number in numbers:
        print(number)
    print("\n")

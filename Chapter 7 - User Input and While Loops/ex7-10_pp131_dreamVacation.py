"""
"""
responses = {}

polling_active = True # Flag for while loop

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Where would you like to visit? ")

    responses[name] = response

    repeat = input("Would you like to continue? y/n")
    if repeat == "n":
        polling_active = False

print("\n Time for the results: ")
for name, response in responses.items():
    print(name + " would like to vist " + response + ".")

"""

"""

toPurchase = 5 # Number of people waiting in line to purchase a ticket
# Active variable ^
while toPurchase > 0:
    age = input("What is your age?")
    if age == "quit":
        break # Break on quit value
    elif age < 3:
        print("Your ticket is free!")
    elif age < 12:
        print("Your ticket is $10")
    else:
        print("Your ticket is $15")
    toPurchase -= 1

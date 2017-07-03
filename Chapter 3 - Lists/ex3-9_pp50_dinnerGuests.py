"""
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through
     3-7 (page 46), use len() to print a message indicating the number of
     people you are inviting to dinner.
"""

guestList = ["Tina", "Katrina", "Fenton", "Thomas"]
message = "! Thank you for coming!"

print("Hi " + guestList[0] + message)
print("Hi " + guestList[1] + message)
print("Hi " + guestList[2] + message)
print("Hi " + guestList[3] + message)

print("Number of guests: ")
print(len(guestList))

"""
3-6. More Guests: You just found a bigger dinner table, so now more space is
     available . Think of three more guests to invite to dinner.

     •	Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
        statement to the end of your program informing people that you found a
        bigger dinner table.

     •	Use insert() to add one new guest to the beginning of your list.

     •	Use insert() to add one new guest to the middle of your list.

     •	Use append() to add one new guest to the end of your list.

     •	Print a new set of invitation messages, one for each person in your
        list.
"""

guestList = ["Tina", "Katrina", "Fenton", "Thomas"]
message = "! Thank you for coming!"

canNotAttend = guestList.pop(2)

print("Oh no! " + canNotAttend + " can't attend your dinner!")

guestList.insert(2, "Geoff")

print("We've found a larger table. Time to invite some more people!")

guestList.insert(0, "Koon")

guestList.insert(2, "Andrew")

guestList.append("Sophie")


print("Hi " + guestList[0] + message)
print("Hi " + guestList[1] + message)
print("Hi " + guestList[2] + message)
print("Hi " + guestList[3] + message)
print("Hi " + guestList[4] + message)
print("Hi " + guestList[5] + message)
print("Hi " + guestList[6] + message)

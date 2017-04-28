"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t
     arrive in time for the dinner, and you have space for only two guests.

     •	Start with your program from Exercise 3-6. Add a new line that prints a
        message saying that you can invite only two people for dinner.

     •	Use pop() to remove guests from your list one at a time until only two
        names remain in your list. Each time you pop a name from your list,
        print a message to that person letting them know you’re sorry you can’t
        invite them to dinner.

     •	Print a message to each of the two people still on your list, letting
        them know they’re still invited.

     •	Use del to remove the last two names from your list, so you have an
        empty list. Print your list to make sure you actually have an empty list
        at the end of your program.
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

print("Now I can only invite 2 people to dessert :(")

print("Sorry " + guestList.pop() + "Your dinner ends here.")
print("Sorry " + guestList.pop() + "Your dinner ends here.")
print("Sorry " + guestList.pop() + "Your dinner ends here.")
print("Sorry " + guestList.pop() + "Your dinner ends here.")
print("Sorry " + guestList.pop() + "Your dinner ends here.")

print("You can come to dessert, " + guestList[0] +".")
print("You can come to dessert, " + guestList[1] +".")

del guestList[0]
del guestList[1]

print(guestList)

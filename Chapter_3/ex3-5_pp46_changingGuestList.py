"""
3-5. Changing Guest List: You just heard that one of your guests can’t make the
     dinner, so you need to send out a new set of invitations. You’ll have to
     think of someone else to invite.

     •	Start with your program from Exercise 3-4. Add a print statement at the
        end of your program stating the name of the guest who can’t make it.

     •	Modify your list, replacing the name of the guest who can’t make it with
        the name of the new person you are inviting.

     •	Print a second set of invitation messages, one for each person who is
        still in your list.
"""

guestList = ["Tina", "Katrina", "Fenton", "Thomas"]
message = "! Thank you for coming!"

canNotAttend = guestList.pop(2)

print("Oh no! " + canNotAttend + " can't attend your dinner!")

guestList.insert(2, "Geoff")


print("Hi " + guestList[0] + message)
print("Hi " + guestList[1] + message)
print("Hi " + guestList[2] + message)
print("Hi " + guestList[3] + message)

"""

"""

usernames = ["admin", "matt", "tina", "tom", "katrina"]

if usernames: # This is a much better way than "if len(usernames) != 0"
    for user in usernames:
        if user == "admin":
            print("Hello " + user + ", would you like to see a status report?")
        else:
            print("Hello " + user + ", welcome back!")
else:
    print("We need to find some users!")

print("")

usernames = []

if usernames:
    for user in usernames:
        if user == "admin":
            print("Hello " + user + ", would you like to see a status report?")
        else:
            print("Hello " + user + ", welcome back!")
else:
    print("We need to find some users!")

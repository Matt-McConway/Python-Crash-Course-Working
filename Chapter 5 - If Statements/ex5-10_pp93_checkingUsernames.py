"""

"""

current_users = ["admin", "matt", "tina", "tom", "katrina"]

new_users = ["bob", "joe", "sam", "matt", "TINA"]

for user in new_users:
    if user.lower() in current_users:
        print("Sorry, this username is not available")
    else:
        print("This username is available - Thank you for signing up!")

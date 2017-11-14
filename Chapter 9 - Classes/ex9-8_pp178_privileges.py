class User():
    def __init__(self, first_name, last_name, username, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.location = location

    def describe_user(self):
        print("##########################")
        print("User information for: " + self.username)
        print("First name: " + self.first_name)
        print("Last name: " + self.last_name)
        print("Location: " + self.location)
        print("##########################")

    def greet_user(self):
        print("Hello, " + self.username + "!")

class Admin(User):
    def __init__(self, first_name, last_name, username, location):
        super().__init__(first_name, last_name, username, location)
        self.privileges = Privileges()



class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

user1 = Admin("Max", "Power", "Admin", "Unknown")
user1.privileges.show_privileges()
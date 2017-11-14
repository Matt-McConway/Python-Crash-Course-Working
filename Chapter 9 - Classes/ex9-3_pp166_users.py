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

user1 = User("James", "Jones", "JJ123", "Wales")
user2 = User("Jill", "Jackson", "JJUSA", "USA")
user3 = User("Joe", "Bloggs", "Bloggsmeister", "Unknown")

user1.describe_user()
user1.greet_user()
print()
user2.describe_user()
user2.greet_user()
print()
user3.describe_user()
user3.greet_user()
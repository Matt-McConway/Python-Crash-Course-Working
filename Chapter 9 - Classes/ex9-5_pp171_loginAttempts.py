class User():
    def __init__(self, first_name, last_name, username, location, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.location = location
        self.login_attempts = login_attempts

    def describe_user(self):
        print("##########################")
        print("User information for: " + self.username)
        print("First name: " + self.first_name)
        print("Last name: " + self.last_name)
        print("Location: " + self.location)
        print("##########################")

    def greet_user(self):
        print("Hello, " + self.username + "!")

    def increment_login_attempts(self):
        self.login_attempts +=1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("James", "Jones", "JJ123", "Wales")

user1.describe_user()
user1.greet_user()

print(user1.login_attempts)
for i in range(10):
    user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"User {self.username}: {self.first_name} {self.last_name}, {self.location}, {self.email}")

    def greet_user(self):
        print(f"Hello, {self.username}!")

user1 = User("John", "Doe", "johndoe", "johndoe@example.com", "New York")
user1.describe_user()
user1.greet_user()


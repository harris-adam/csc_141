import Restaurant
# Restaurant class
class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name.title()} serves wonderful {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.name.title()} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, additional_served):
        self.number_served += additional_served


# User class
class User:

    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"User: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location.title()}")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


restaurant = Restaurant("The Great Taco", "Mexican")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(10)
print(f"Number served: {restaurant.number_served}")
restaurant.increment_number_served(5)
print(f"Updated number served: {restaurant.number_served}")

user = User("john", "doe", 30, "new york")
user.describe_user()
user.greet_user()
print(f"Login attempts: {user.login_attempts}")
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts after incrementing: {user.login_attempts}")
user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")

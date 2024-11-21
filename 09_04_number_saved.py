class Restaurant: 
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

restaurant = Restaurant("The Great Eatery", "Italian")
restaurant.set_number_served(20)
print(f"Number served: {restaurant.number_served}")
restaurant.increment_number_served(5)
print(f"Updated number served: {restaurant.number_served}")
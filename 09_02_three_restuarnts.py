class Restaurant:
    def init(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

restaurant1 = Restaurant("Pasta House", "Italian")
restaurant2 = Restaurant("Sushi Express", "Japanese")
restaurant3 = Restaurant("Taco Town", "Mexican")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

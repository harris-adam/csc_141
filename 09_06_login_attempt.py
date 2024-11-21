class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type="ice cream"):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("We have the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

stand = IceCreamStand("Sweet Treats")
stand.flavors = ["vanilla", "chocolate", "strawberry"]
stand.show_flavors()
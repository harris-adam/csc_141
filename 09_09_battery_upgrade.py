class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100
            print("Battery upgraded to 100 kWh.")
        else:
            print("Battery is already upgraded.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar("Tesla", "Model S", 2022)
my_tesla.battery.upgrade_battery()
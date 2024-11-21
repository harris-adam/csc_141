import json

filename = 'favorite_number.json'

try:
    with open(filename) as file:
        number = json.load(file)
    print(f"Welcome back! Your favorite number is {number}.")
except FileNotFoundError:
    number = input("What is your favorite number? ")
    with open(filename, 'w') as file:
        json.dump(number, file)
    print(f"Your favorite number {number} has been stored.")
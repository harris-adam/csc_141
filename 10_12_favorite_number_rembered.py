import json

filename = 'favorite_number.json'

try:
    with open(filename) as file:
        number = json.load(file)
    print(f"Your favorite number is {number}.")
except FileNotFoundError:
    print("No favorite number found.")
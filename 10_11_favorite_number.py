import json

filename = 'favorite_number.json'

number = input("What is your favorite number? ")
with open(filename, 'w') as file:
    json.dump(number, file)

print(f"Your favorite number {number} has been stored.")
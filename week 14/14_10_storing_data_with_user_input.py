filename = 'user_data.txt'


name = input("Enter your name: ")

with open(filename, 'w') as file:
    file.write(name)

print(f"Your name '{name}' has been written to {filename}.")
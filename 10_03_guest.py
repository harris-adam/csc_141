filename = 'guest.txt'

name = input("What is your name? ")
with open(filename, 'w') as file:
    file.write(name)

print(f"Hello, {name}. Your name has been written to {filename}.")

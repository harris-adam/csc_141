filename = 'guest_book.txt'

print("Enter 'quit' to exit.")
while True:
    name = input("What is your name? ")
    if name.lower() == 'quit':
        break

    print(f"Hello, {name}! Welcome!")
    with open(filename, 'a') as file:
        file.write(f"{name}\n")
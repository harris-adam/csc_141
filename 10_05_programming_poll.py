filename = 'programming_poll.txt'

print("Enter 'quit' to exit.")
while True:
    response = input("Why do you like programming? ")
    if response.lower() == 'quit':
        break

    with open(filename, 'a') as file:
        file.write(f"{response}\n")
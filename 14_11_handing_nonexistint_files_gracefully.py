filename = 'example.txt'


while True:
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
        break
    except FileNotFoundError:
        print(f"The file {filename} does not exist. Please check the filename and try again.")
        filename = input("Enter the filename again: ")
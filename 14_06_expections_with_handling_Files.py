filename = 'non_existent_file.txt'


try:
    with open(filename, 'r') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print(f"Sorry, the file {filename} was not found.")
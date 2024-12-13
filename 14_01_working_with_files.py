filename = 'example.txt'


try:
    with open(filename, 'r') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print(f"The file {filename} does not exist.")
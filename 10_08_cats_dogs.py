def read_file(filename):
    try:
        with open(filename) as file:
            contents = file.read()
            print(f"\nContents of {filename}:\n{contents.strip()}")
    except FileNotFoundError:
        print(f"Sorry, the file {filename} was not found.")

read_file('cats.txt')
read_file('dogs.txt')
filename = 'example.txt'


try:
    with open(filename, 'r') as file:
        contents = file.read()
        words = contents.split()  
        print(f"The file contains {len(words)} words.")
except FileNotFoundError:
    print(f"The file {filename} does not exist.")
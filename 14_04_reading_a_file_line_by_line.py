filename = 'example.txt'


try:
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())  
except FileNotFoundError:
    print(f"The file {filename} does not exist.")
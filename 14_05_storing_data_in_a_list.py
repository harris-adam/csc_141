filename = 'example.txt'


try:
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        print(line.strip())
except FileNotFoundError:
    print(f"The file {filename} does not exist.")
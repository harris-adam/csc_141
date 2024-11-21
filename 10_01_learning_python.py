filename = 'learning_python.txt'

# Reading the file as a whole
with open(filename) as file:
    content = file.read()
    print(content)

# Reading line by line
print("\n--- Reading line by line ---")
with open(filename) as file:
    for line in file:
        print(line.strip())

# Storing lines in a list and printing
print("\n--- Storing lines in a list ---")
with open(filename) as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())
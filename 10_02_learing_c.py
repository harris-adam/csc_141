filename = 'learning_python.txt'

with open(filename) as file:
    lines = file.readlines()

# Replacing "Python" with "C"
for line in lines:
    print(line.replace('Python', 'C').strip())
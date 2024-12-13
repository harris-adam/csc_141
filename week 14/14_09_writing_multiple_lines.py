filename = 'output_multiple_lines.txt'
lines_to_write = [
    "This is line one.",
    "This is line two.",
    "This is line three."
]


with open(filename, 'w') as file:
    for line in lines_to_write:
        file.write(line + '\n')  

print(f"Lines written to {filename}")
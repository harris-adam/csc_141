filename = 'output.txt'
message = "Hello, this is a test message!"


with open(filename, 'w') as file:
    file.write(message)

print(f"Message written to {filename}")
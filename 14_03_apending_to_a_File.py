filename = 'output.txt'
additional_message = "\nThis is an additional line added to the file."


with open(filename, 'a') as file:
    file.write(additional_message)

print(f"New message appended to {filename}")
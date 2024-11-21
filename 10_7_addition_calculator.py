print("Enter two numbers to add (or 'q' to quit).")

while True:
    try:
        num1 = input("Enter the first number: ")
        if num1.lower() == 'q':
            break
        num1 = int(num1)

        num2 = input("Enter the second number: ")
        if num2.lower() == 'q':
            break
        num2 = int(num2)

        print(f"The sum is: {num1 + num2}")
    except ValueError as e:
        print("Error: Please enter valid numbers.")
        with open('error_log.txt', 'a') as file:
            file.write(f"ValueError: {e}\n")
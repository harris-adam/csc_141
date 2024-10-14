prompt = "\nEnter a topping for your pizza (or 'quit' to end): "

while True:
    topping = input(prompt)
    
    if topping.lower() == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.")
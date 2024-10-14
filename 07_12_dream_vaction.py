responses = {}

while True:
    name = input("\nWhat is your name? (Enter 'quit' to end): ")
    
    if name.lower() == 'quit':
        break
    
    vacations = []
    while True:
        vacation = input(f"If you could visit one place in the world, where would you go, {name}? (Enter 'done' when finished): ")
        
        if vacation.lower() == 'done':
            break
        vacations.append(vacation)
    
    responses[name] = vacations
    
    repeat = input("Would you like to let another person respond? (yes/no): ")
    if repeat.lower() == 'no':
        break

print("\n--- Poll Results ---")
for name, vacations in responses.items():
    print(f"\n{name.title()} would like to visit the following places:")
    for vacation in vacations:
        print(f"- {vacation.title()}")
favorite_numbers = {
    'alice': [5, 12],
    'bob': [7, 22],
    'carol': [12, 42],
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are: {', '.join(map(str, numbers))}.")
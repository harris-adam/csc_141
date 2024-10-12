pet1 = {'animal': 'dog', 'owner': 'john'}
pet2 = {'animal': 'cat', 'owner': 'alice'}
pet3 = {'animal': 'rabbit', 'owner': 'bob'}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"{pet['owner'].title()} has a {pet['animal']}.")
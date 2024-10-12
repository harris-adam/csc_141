person1 = {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'city': 'New York'}
person2 = {'first_name': 'Alice', 'last_name': 'Smith', 'age': 28, 'city': 'Los Angeles'}
person3 = {'first_name': 'Bob', 'last_name': 'Johnson', 'age': 35, 'city': 'Chicago'}

people = [person1, person2, person3]

for person in people:
    print(f"Name: {person['first_name']} {person['last_name']}, Age: {person['age']}, City: {person['city']}")
favorite_places = {
    'john': ['new york', 'paris', 'tokyo'],
    'alice': ['london', 'sydney'],
    'bob': ['rome', 'amsterdam'],
}

for person, places in favorite_places.items():
    print(f"{person.title()} loves these places:")
    for place in places:
        print(f"- {place.title()}")
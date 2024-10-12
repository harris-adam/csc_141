cities = {
    'new york': {
        'country': 'usa',
        'population': '8 million',
        'fact': 'Known as the Big Apple.'
    },
    'tokyo': {
        'country': 'japan',
        'population': '37 million',
        'fact': 'The most populous city in the world.'
    },
    'paris': {
        'country': 'france',
        'population': '2 million',
        'fact': 'Famous for the Eiffel Tower.'
    }
}

for city, info in cities.items():
    print(f"{city.title()}:")
    for key, value in info.items():
        print(f"  {key.title()}: {value}") 
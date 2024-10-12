glossary = {
    'variable': 'A reserved memory location to store values.',
    'list': 'A collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.',
    'loop': 'Repeating an action multiple times.',
    'function': 'A block of code that performs a specific task.'
}

glossary['tuple'] = 'An immutable list.'
glossary['set'] = 'A collection of unique items.'

for word, definition in glossary.items():
    print(f"{word.title()}: {definition}")
from collections import OrderedDict

glossary = OrderedDict()

glossary['function'] = 'A block of code that performs a specific task.'
glossary['variable'] = 'A storage location for data.'
glossary['loop'] = 'A way to repeat actions multiple times.'

for term, definition in glossary.items():
    print(f"{term.title()}: {definition}")
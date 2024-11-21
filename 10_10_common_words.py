def count_word(filename, word):
    try:
        with open(filename) as file:
            content = file.read()
        word_count = content.lower().count(word.lower())
        print(f"The word '{word}' appears {word_count} times in {filename}.")
    except FileNotFoundError:
        print(f"Sorry, the file {filename} was not found.")

count_word('sample.txt', 'python')
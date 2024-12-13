from collections import Counter

filename = 'example.txt'


try:
    with open(filename, 'r') as file:
        words = file.read().split()  
        word_counts = Counter(words) 
        common_word, common_count = word_counts.most_common(1)[0]
        print(f"The most common word is '{common_word}', appearing {common_count} times.")
except FileNotFoundError:
    print(f"The file {filename} does not exist.")
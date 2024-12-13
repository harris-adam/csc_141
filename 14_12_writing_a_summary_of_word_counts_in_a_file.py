from collections import Counter

input_filename = 'example.txt'
output_filename = 'word_count_summary.txt'

try:
    with open(input_filename, 'r') as file:
        words = file.read().split()
        word_counts = Counter(words)
    
    with open(output_filename, 'w') as output_file:
        for word, count in word_counts.items():
            output_file.write(f"{word}: {count}\n")
    
    print(f"Word count summary has been written to {output_filename}")
except FileNotFoundError:
    print(f"The file {input_filename} does not exist.")
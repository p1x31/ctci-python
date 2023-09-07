#right
from collections import Counter

# Read the input string
s = input()

# Count the frequency of each letter in 's'
letter_counts = Counter(s)

# Initialize a dictionary with the required letters and their counts for the word 'sheriff'
required_letters = {'s': 1, 'h': 1, 'e': 1, 'r': 1, 'i': 1, 'f': 2}

# Initialize a variable to keep track of the maximum number of 'sheriff' words
max_sheriff_words = float('inf')  # Initialize as positive infinity

# Check how many 'sheriff' words can be formed
for letter, count in required_letters.items():
    if letter_counts[letter] < count:
        max_sheriff_words = 0
        break
    else:
        max_sheriff_words = min(max_sheriff_words, letter_counts[letter] // count)

# Print the maximum number of 'sheriff' words that can be formed
print(max_sheriff_words)
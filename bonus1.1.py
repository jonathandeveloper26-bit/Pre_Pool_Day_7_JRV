### Task 1.1 Vowels and Consonants
# Write a function that takes a string and prints how many vowels and how many consonants it contains.
# ✓ Ignore anything that is not a letter (spaces, digits, punctuation).
# ✓ Uppercase and lowercase are treated the same.
# count_types("Hello World!") -> 3 vowels, 7 consonants

from english_words import get_english_words_set
import random


def count_characters(string):
    vowels = ["a", "e", "i", "o", "u"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    vowel_count = 0
    consonant_count = 0
    for char in string:
        if char in vowels:
            vowel_count += 1
        if char in consonants:
            consonant_count += 1
    return vowel_count, consonant_count

random_word = random.choice(list(get_english_words_set(['web2'],lower=True)))

print(f"Random Word: {random_word}")
vowel_count, consonant_count = count_characters(random_word)
print(f"Vowel Count: {vowel_count}")
print(f"Consonant Count: {consonant_count}")

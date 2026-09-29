# Task 2.1: You have a list of words (for example, built from english_word_lower_set). Write three functions:
# 1. One that returns only the words of length n.
# 2. One that returns only the words made exclusively of letters (no digits, no -, no spaces).
# 3. One that returns a dict grouping the words by length.
# Finally, ask the user for a length and pick a random word of that length.

from english_words import get_english_words_set

def get_words_by_n(length):
    return [words for words in list(get_english_words_set(['web2'],lower=True)) if len(words) == length]

def only_letters():
    return [words for words in list(get_english_words_set(['web2'], lower=True)) if not any(char in words for char in ["-", " ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])]

def get_dict_grouping_english():
    dict_grouping = dict()
    for words in list(get_english_words_set(['web2'], lower= True)):
        if len(words) in dict_grouping:
            dict_grouping[len(words)].append(words)
        else:
            dict_grouping[len(words)] = [words]
    return dict_grouping

#print(get_dict_grouping_english()[24]) # Uncomment if you want to print this

user_length = 0
while True:
    try:
        user_length = int(input("Enter a string length: "))
        break
    except:
        print("Enter a valid string length (integer).")

print(get_words_by_n(user_length))

# print(only_letters()) # Uncomment if you want to print this
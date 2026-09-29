# Write a function that takes a word and returns a dict with the number of occurrences of each letter.
# frequency("banana") -> {"b": 1, "a": 3, "n": 2}
# Write a second function that returns the most frequent letter of a word. If several letters are tied, return
# the first one in alphabetical order

def frequency(word):
    freq = dict()
    word = word.lower()
    for char in word:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

print(frequency("Banana"))

def most_frequent_char(word):
    word = word.lower()
    most_frequent = ""
    most_frequent_count = 0
    for char in word:
        if word.count(char) > most_frequent_count:
            most_frequent_count = word.count(char)
            most_frequent = char
        if word.count(char) == most_frequent_count:
            if most_frequent < char:
                most_frequent = char
        else:
            continue
    return most_frequent

print(most_frequent_char("heeello"))


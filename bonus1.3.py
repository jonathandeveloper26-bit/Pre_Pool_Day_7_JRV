# Task 1.3: Write a function that takes two words and returns True if they are made of exactly the same letters (same letters, same number of times).
#is_anagram("listen", "silent") -> True
#is_anagram("hello", "world") -> False

def is_anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    for char in word1:
        if word1.count(char) != word2.count(char):
            return False
    return True
        

print(is_anagram(word1="Hello", word2="ohell"))

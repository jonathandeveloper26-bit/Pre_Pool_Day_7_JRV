### Task 1.2: Write a function that returns True if a word reads the same forwards and backwards, False otherwise.
# ✓ Case does not matter.
# ✓ Take inspiration from yesterday version, but use a loop instead of recursion this time.
# is_palindrome("Kayak") -> True
# is_palindrome("hangman") -> False

def is_palindrome(word):
    word = word.lower()
    is_pal = True
    for i in range(len(word)//2):
        if word[i] == word[(len(word)-i-1)]:
            continue
        else:
            return False

    return is_pal

print(is_palindrome("Kayak"))
print(is_palindrome("hangman"))
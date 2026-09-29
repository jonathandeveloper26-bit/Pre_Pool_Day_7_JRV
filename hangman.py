### Epitech Pre_Pool Day 7
# Project Title: "First Program"
# Project Goal: Hangman Game!
import random

# First Brick: Write a function that takes an integer as parameter and prints ”You lose!” if the parameter is greater than or equal to 12.
def check_attempts(atmpt):
    if atmpt >= 12: 
        print("You Lose!")
        return False
    else: 
        return True

# Second Brick: Write a snippet of code to return a random item from the set {1, 2, 3, 4, 5, 6}. Encapsulate this piece of code inside a function.

def rand_from_set():
    items = {1, 2, 3, 4, 5, 6}
    return random.choice(list(items)) # Must typecast items to turn it into an iterable

# Third Brick: Write a function that:
# ✓ takes astring as parameter;
# ✓ finds the lengthnof this string;
# ✓ prints a string made of n pairs ”_ ” (underscore followed by a space)


### For Testing Functions:

# check_attempts
print(check_attempts(13))
print(check_attempts(5))

# rand_from_set
print(rand_from_set())



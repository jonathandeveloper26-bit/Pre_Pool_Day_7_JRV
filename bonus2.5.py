### Task 2.5: Create a second mini-game: the program picks a word, shuffles its letters,
#   and the player must find the original word.
# ✓ Shuffle the letters yourself, using only what you have seen (random.shuffle is not allowed).
# ✓ The scrambled word must never be identical to the original.
# ✓ The player has a limited number of attempts.
# ✓ Show the number of attempts left after each try.

from english_words import get_english_words_set
import time
import random

def set_attempts():
    attempts = 0
    while True:
        try:
            attempts = int(input("Enter the number of attempts you would like: "))
            return attempts

        except:
            print("That is an invalid answer. Enter an integer.")

def get_random_word():
    return random.choice(list(get_english_words_set(['web2'],lower=True)))

def scramble_letters(word):
    t_seen = []
    scrambled_word = ""
    different = False
    while not different:
        for i in range(len(word)):
            t_in_seen = False
            while not t_in_seen:
                t = int(round(time.time()*1000,0) % len(word))
                if t in t_seen:
                    continue
                else:
                    t_seen.append(t)
                    scrambled_word = scrambled_word + word[t]
                    t_in_seen = True
        if scrambled_word == word:
            scrambled_word = ""
        else:
            different = True
    return scrambled_word
        
word = get_random_word()
print(word)

print(scramble_letters(word))

allowed_attempts = set_attempts()

guessed = ""
attempts = 0

while attempts < allowed_attempts:
    user_guess = input("Enter your guess: ")
    if user_guess == word:
        print("Congratulations!!! You guessed correctly.")
        break
    else:
        print("I'm sorry, your guess is incorrect.")
        attempts += 1
        print(f"You have attempted {attempts} times. You have {allowed_attempts-attempts} remaining.")
    if attempts == allowed_attempts:
        print("You've lost!")
    else:
        continue

    




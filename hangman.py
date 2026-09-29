### Epitech Pre_Pool Day 7
# Project Title: "First Program"
# Project Goal: Hangman Game!
import random
import time
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--ap", type=int, help= "Allowed Penalties")
parser.add_argument("--tb", type=bool, help= "Boolean for time")
parser.add_argument("--ts", type=int, help= "Time Limit (in seconds)")
parser.add_argument("--wl", type=int, help="Word Length")

args = parser.parse_args()


### Check User Attempts. If attempts >= 12 (by default), they lose. Otherwise, they continue.
def check_attempts(atmpt, allowed = 12):
    if atmpt >= allowed: 
        print("You Lose!")
        return False
    else: 
        return True

### Gets the Number of Allowed Penalties from the User
def get_allowed_penalties():
    allowed = 12
    while True:
        user_choice = input("Would you like to change the number of penalties allowed? (Y/N): ").lower()
        if user_choice == "quit":
            quit()
        if user_choice == "y":
            while True:
                try:
                    allowed = int(input("Enter the number of penalties you would like: "))
                    break
                except:
                    print("You have entered an invalid number. Enter an integer.")
            return allowed

        elif user_choice == "n":
            return allowed
        else:
            print(f"{user_choice} is an invalid option. Try again.")

def get_time_limit():
    time_limit_bool = False
    time_limit_s = 0
    while True:
        user_choice = input("Would you like to add a time limit? (Y/N): ").lower()
        if user_choice == "quit":
            quit()
        if user_choice == "y":
            while True:
                try:
                    time_limit_s = int(input("Enter the number of seconds you would like: "))
                    time_limit_bool = True
                    break
                except:
                    print("You have entered an invalid number. Enter an integer.")
            return time_limit_bool, time_limit_s

        elif user_choice == "n":
            return time_limit_bool, time_limit_s
        else:
            print(f"{user_choice} is an invalid option. Try again.")
    return
### Generates the '_ ' pairs to initialize the 'empty' word for the user to see
def generate_pairs(string):
    pairs = ""
    for i in range(len(string)):
        pairs += "_ "
    return pairs

### gets a random (lower-case) english word of length (chosen by user)
def get_random_word(length):
    from english_words import get_english_words_set
    return random.choice([words for words in list(get_english_words_set(['web2'],lower=True)) if len(words) == length])

### updates the '_ ' paris according to the user guess.
def update_pairs(pairs, user_guess, word):
    for i in range(len(word)):
        if user_guess == word[i]:
            pairs = pairs[:2*i] + user_guess + pairs[2*i+1:]
        else:
            continue
    return pairs

### Checks if the user has won by compairing the pairs (stripped) to the word
def check_win(pairs, word):
    stripped = pairs.replace(" ", "")
    if stripped == word:
        return True
    else:
        return False

### Gets the desired word length from the user.
def get_word_length():
    while True:
        try:
            length = int(input("Enter the length of the word you would like: "))
            break
        except:
            print("You have entered an invalid option. Please enter an integer.")
    return length

### Implements the word guess interaction.
def word_guess_interaction(guesses_words, word, penalties):
    game_finished = False
    print(f"You have guessed: {guesses_words} so far.")
    user_guess = input("Your (word) guess: ").lower()
    guesses_words.add(user_guess)
    if user_guess == word:
        print(f"Congratulations! Your guess is correct!! You won!!!")
        game_finished = True
    else:
        penalties += 5
        print(f"Your guess of '{user_guess}' is incorrect. 5 penalties have been applied. Your total penalty is {penalties}")

    return guesses_words, penalties, game_finished

### Implements the letter guess interaction.
def letter_guess_interaction(guesses_letters, word, penalties, pairs):
    user_guess = ""
    game_finished = False
    while len(user_guess) != 1:
        print(f"You have guessed {guesses_letters} so far.")
        user_guess = input("Your (letter) guess: ").lower()
        if (len(user_guess) != 1):
            print(f"You entered: {user_guess} which is an invalid guess. Please try again.\n")
            continue

        guesses_letters.add(user_guess)
        if user_guess in word:
            pairs = update_pairs(pairs, user_guess, word)
            if check_win(pairs, word):
                print(f"Congratulations! Your guess is correct!! You won!!!")
                game_finished = True
            else: 
                print("Congratulations! Your guess is correct!!")
        
        else:
            penalties += 1
            print(f"Your guess of '{user_guess}' is incorrect. 1 penalty has been applied. Your total penalty is {penalties}")
            
    return guesses_letters, penalties, game_finished, pairs

### Game Implementation

### Welcoming
print("Hello! Welcome to Hangman!")
print(f"The rules are as follows:\n - You may select the length of the word (int)\n - Each turn you may guess either a letter or a full word: \n   - if the letter exists, I will reveal all instances of that letter, but if it doesn't you are penalized 1 point.\n   - if the word exists, you win! If it doesn't, you are penalized 5 points. \n   - Once you are penalized {args.ap if args.ap else 12} times, you lose!\n")

### Initializations
penalties = 0
guess_count = 1
game_finished = False
guesses_letters = set()
guesses_words = set()

### Initialie Word and Pairs

word_length = args.wl if args.wl else get_word_length()
word = get_random_word(word_length)
pairs = generate_pairs(word)
allowed_penalties = args.ap if args.ap else get_allowed_penalties()
time_limit_bool, time_limit_s = args.tb, args.ts if args.tb and args.ts else get_time_limit()
user_time = 0
print(f"Welcome! You have chosen a word with {word_length} letters. Good luck!!\n")
if time_limit_bool:
    print("Your time starts now!!!")
    user_time = time.time()

### Game Play
print(word)
while not game_finished:
    if time_limit_bool and time.time() - user_time >= time_limit_s:
        print("Oh no! You have run out of time!!!")
        break
    
    print(pairs)
    try:
        guess_type = input(f"Guess #{guess_count}\nWould you like to guess a word(w) or a letter (l)?\n")
        if guess_type == "quit":
            game_finished = True
            break

        if guess_type.lower() == "w":
            guesses_words, penalties, game_finished = word_guess_interaction(guesses_words, word, penalties)
        elif guess_type.lower() == "l":
            guesses_letters, penalties, game_finished, pairs = letter_guess_interaction(guesses_letters, word, penalties, pairs)
        else:
            print("You entered and invalid option - enter 'w' to guess a word or 'l' to guess a letter.")
            continue
        guess_count += 1

        if not check_attempts(penalties, allowed_penalties):
            game_finished = True
            print(f"Your final result: {pairs}\nThe word: {word}.")
    except:
        print("An Error Occurred")



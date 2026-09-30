### Epitech Pre_Pool Day 7
# Project Title: "First Program"
# Project Goal: Hangman Game!

### Bonus 3.3: Wheel of Themes: This was already partially completed in hangman_bonus_2.py.
# I'm going to keep themes in the files. 
# I'm going to use "random" as choosing any of those themes
# I will display that theme
# The formula for penalties will be the length_word * 2 + len(theme_name)

import random
import time

def get_games_continue():
    valid_choice = False
    games_continue = False
    while not valid_choice:
        try:
            continue_choice = str(input("Would you like to keep playing? (Y/N) ")).lower()
            if continue_choice == "y":
                games_continue = True
                valid_choice = True      
            elif continue_choice =="n":
                games_continue = False
                valid_choice = True
            else:
                print("Enter a valid option please.")
                valid_choice = False
        except:
            print("Enter a valid option please.")
            continue
    return games_continue

def give_hint(word, pairs, penalties, guesses_letters):
    user_guess = "?"
    
    penalties += 2
    print(f"Your hint has been applied. 2 penalties have been applied. Your total penalty is {penalties}")
    for char in word:
        if not char in pairs:
            user_guess = char
            break
        else:
            continue

    return pairs, penalties, guesses_letters, user_guess

### Returns a random word from 'file_name'.txt
def get_word_from_file(file_name, length):
    words = []
    with open(file_name, "r") as f:
        for line in f:
            for w in line.split():
                words.append(w)
    return random.choice([word for word in list(words) if len(word) == length])
    
### Check User Attempts. If attempts >= 12 (by default), they lose. Otherwise, they continue.
def check_attempts(atmpt, allowed = 12):
    if atmpt >= allowed: 
        print("You Lose!")
        return False
    else: 
        return True

### Gets the time limits
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
    options = ["random", "ocean", "plants", "space", "travel", "vehicles", "custom"]
    theme = ""
    while True:
        try:
            theme = input("Do you have a theme (Random, Plants, Space, Travel, Vehicles, Custom) in mind? ").lower()
            theme = theme.replace(".txt", "")
            if theme in options:
                if theme == "random":
                    theme = random.choice(["Plants", "Space", "Travel", "Vehicles"]).lower()
                    return get_word_from_file(theme + ".txt", length), theme
                elif theme != "random" and theme != "custom":
                    return get_word_from_file(theme + ".txt", length), theme
                elif theme == "custom":
                    theme = input("Enter your file name (.txt only): ")
                    return get_word_from_file(theme + ".txt", length), theme

            else:
                print(f"You have entered {theme} which is an invalid option. Try again.")
        except:
            print("An Error has Occurred.")

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
def letter_guess_interaction(guesses_letters, word, penalties, pairs, allowed_penalties):
    user_guess = ""
    game_finished = False
    while len(user_guess) != 1:
        print(f"You have guessed {guesses_letters} so far.")
        user_guess = input("Your (letter) guess: ").lower()

        if user_guess == "?":
            if penalties + 2 >= allowed_penalties:
                print("Sorry, this option is unavailable to you. You have too many penalties.")
                continue
            else:
                pairs, penalties, guesses_letters, user_guess = give_hint(word, pairs, penalties, guesses_letters)

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

def get_allowed_penalties(word, theme):
    return 2*len(word) + len(theme)

### Game Implementation

### Welcoming
print("Hello! Welcome to Hangman!")
print(f"The rules are as follows:\n - You may select the length of the word (int)\n - Each turn you may guess either a letter or a full word: \n   - if the letter exists, I will reveal all instances of that letter, but if it doesn't you are penalized 1 point.\n   - if the word exists, you win! If it doesn't, you are penalized 5 points. \n   - Once you are penalized enough times, you lose!\n")
history = []
games_continue = True

while games_continue:
    ### Initializations
    penalties = 0
    guess_count = 1
    game_finished = False
    guesses_letters = set()
    guesses_words = set()
    
    ### Initialize Words and Pairs
    word_length = get_word_length()
    word, theme = get_random_word(word_length)
    print(f"The theme is: {theme}")
    pairs = generate_pairs(word)
    allowed_penalties = get_allowed_penalties(word, theme)
    print(f"Your allowed penalties are: {allowed_penalties}")
    time_limit_bool, time_limit_s = get_time_limit()
    user_time = 0

    game_id = word + str(round(time.time(),0))
    history.append({
        "game_id": game_id,
        "word": word,
        "won": False,
        "penalties": penalties,
    })
    

    print(f"Welcome! You have chosen a word with {word_length} letters. Good luck!!\n")
    if time_limit_bool:
        print("Your time starts now!!!")
        user_time = time.time()

    ### Game Play
    print(word)
    while not game_finished:
        if time_limit_bool and time.time() - user_time >= time_limit_s:
            print("Oh no! You have run out of time!!!")
            history[len(history)-1]["penalties"] = penalties
            game_finished = True
            continue
        
        print(pairs)
        try:
            guess_type = input(f"Guess #{guess_count}\nWould you like to guess a word(w) or a letter (l)?\n")
            if guess_type == "quit":
                game_finished = True
                history[len(history)-1]["penalties"] = penalties
                
                games_continue = False
                
                continue

            if guess_type.lower() == "w":
                guesses_words, penalties, game_finished = word_guess_interaction(guesses_words, word, penalties)
                if game_finished:
                    history[len(history)-1]["penalties"] = penalties
                    
                    games_continue = get_games_continue()
            
                    continue
            elif guess_type.lower() == "l":
                guesses_letters, penalties, game_finished, pairs = letter_guess_interaction(guesses_letters, word, penalties, pairs, allowed_penalties)
                if game_finished: 
                    history[len(history)-1]["penalties"] = penalties
                    
                    games_continue = get_games_continue()
                    
                    continue
            else:
                print("You entered and invalid option - enter 'w' to guess a word or 'l' to guess a letter.")
                continue
            guess_count += 1

            if not check_attempts(penalties, allowed_penalties):
                game_finished = True
                history[len(history)-1]["penalties"] = penalties
                print(f"Your final result: {pairs}\nThe word: {word}.")
               
                games_continue = get_games_continue()
               
                continue
        except:
            print("An Error Occurred")

print(history)



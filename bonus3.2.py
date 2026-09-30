### Epitech Pre_Pool Day 7
# Project Title: "First Program"
# Project Goal: Hangman Game!

### Bonus 3.2 - Two Player!

import random
import time
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--ap", type=int, help= "Allowed Penalties")
parser.add_argument("--tb", type=bool, help= "Boolean for time")
parser.add_argument("--ts", type=int, help= "Time Limit (in seconds)")
parser.add_argument("--wl", type=int, help="Word Length")
parser.add_argument("--f", type=str, help="File Name - including extension")

args = parser.parse_args()

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
    penalties += 4
    print(f"Your hint has been applied. 2 penalties have been applied. Your total penalty is {penalties}")
    for char in word:
        if not char in pairs:
            user_guess = char
            break
        else:
            continue

    return pairs, penalties, guesses_letters, user_guess

### Generates the '_ ' pairs to initialize the 'empty' word for the user to see
def generate_pairs(string):
    pairs = ""
    for i in range(len(string)):
        pairs += "_ "
    return pairs

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

### Implements the word guess interaction.
def word_guess_interaction(guesses_words, word, penalties):
    game_finished = False
    game_won = False
    print(f"You have guessed: {guesses_words} so far.")
    user_guess = input("Your (word) guess: ").lower()
    guesses_words.add(user_guess)
    if user_guess == word:
        print(f"Congratulations! Your guess is correct!! You found the word!!")
        game_won = True
        game_finished = True
    else:
        penalties += 5
        print(f"Your guess of '{user_guess}' is incorrect. 5 penalties have been applied. Your total penalty is {penalties}")

    return guesses_words, penalties, game_finished, game_won

### Implements the letter guess interaction.
def letter_guess_interaction(guesses_letters, word, penalties, pairs):
    user_guess = ""
    game_finished = False
    game_won = False
    while len(user_guess) != 1:
        print(f"You have guessed {guesses_letters} so far.")
        user_guess = input("Your (letter) guess: ").lower()

        if user_guess == "?":
            pairs, penalties, guesses_letters, user_guess = give_hint(word, pairs, penalties, guesses_letters)

        if (len(user_guess) != 1):
            print(f"You entered: {user_guess} which is an invalid guess. Please try again.\n")
            continue

        guesses_letters.add(user_guess)
        if user_guess in word:
            pairs = update_pairs(pairs, user_guess, word)
            if check_win(pairs, word):
                print(f"Congratulations! Your guess is correct!! You found the word!!")
                game_finished = True
                game_won = True
            else: 
                print("Congratulations! Your guess is correct!!")
        
        else:
            penalties += 1
            print(f"Your guess of '{user_guess}' is incorrect. 1 penalty has been applied. Your total penalty is {penalties}")
            
    return guesses_letters, penalties, game_finished, pairs, game_won

def validate_secret(word):
    
    if word.isalpha() and len(word) >=3:
        print("\n"*100)
        return True
    else:
        return False

def end_game_print(history):

    print("Game Over! Let's see who won!!")
    print(f"Player 1's Score: {p1_score}")
    print(f"Player 2's Score: {p2_score}")
    if p1_score > p2_score:
        print("Congratulations Player 1!")
    elif p1_score < p2_score: 
        print("Congratulations Player 2!")
    else:
        print("You tied!")

def get_word_from_player():
    word = ""
    valid = False
    while not valid:
        word = input("Enter the secret word: ").lower()
        valid = validate_secret(word)
        if not valid: 
            print("Enter a word with at least three letters and no numbers")
        else: 
            continue
    return word

### Game Implementation

### Welcoming
print("Hello! Welcome to Hangman - 2 Player Mode!")
print(f"The rules are as follows:\n - You may select the length of the word (int)\n - Each turn you may guess either a letter or a full word: \n   - if the letter exists, I will reveal all instances of that letter, but if it doesn't you are penalized 1 point.\n   - if the word exists, you win! If it doesn't, you are penalized 5 points. \n   - Once you are penalized {args.ap if args.ap else 12} times, you lose!\n")
history = {
    "Player 1": [],
    "Player 2": [],
}
p1_score = 0
p1_penalty = 0
p2_score = 0
p2_penalty = 0
games_continue = True

while games_continue:
    player = ""
    chooser = ""
    if (len(history["Player 1"])+ len(history["Player 2"])) % 2 == 0:
        player = "Player 1"
        chooser = "Player 2"
    else:
        player = "Player 2"
        chooser = "Player 1"

    print("Player: " + player)

    if len(history["Player 2"]) > 2:
        end_game_print(history)
        break
        
    ### Initializations
    penalties = 0
    guess_count = 1
    game_finished = False
    guesses_letters = set()
    guesses_words = set()

    ### Initialize Word and Pairs
    word = get_word_from_player()
    pairs = generate_pairs(word)

    game_id = word + str(round(time.time(),0))
    history[player].append({
        "game_id": game_id,
        "word": word,
        "won": False,
        "penalties": penalties,
    })
    
    print(f"Welcome {player}! {chooser} has chosen a word with {len(word)} letters. Good luck!!\n")
    
    ### Game Play
    while not game_finished:
        print(pairs)
        try:
            guess_type = input(f"Guess #{guess_count}\nWould you like to guess a word(w) or a letter (l)?\n")
            if guess_type == "quit":
                game_finished = True
                history[player][len(history[player])-1]["penalties"] = penalties
                history[player][len(history[player])-1]["won"] = False
                games_continue = False
                continue

            if guess_type.lower() == "w":
                guesses_words, penalties, game_finished, game_won = word_guess_interaction(guesses_words, word, penalties)
                if game_finished:
                    history[player][len(history[player])-1]["penalties"] = penalties
                    history[player][len(history[player])-1]["won"] = game_won
                    #games_continue = get_games_continue()
                    continue
            elif guess_type.lower() == "l":
                guesses_letters, penalties, game_finished, pairs, game_won = letter_guess_interaction(guesses_letters, word, penalties, pairs)
                if game_finished: 
                    history[player][len(history[player])-1]["penalties"] = penalties
                    history[player][len(history[player])-1]["won"] = game_won
                    #games_continue = get_games_continue()
                    continue
            else:
                print("You entered and invalid option - enter 'w' to guess a word or 'l' to guess a letter.")
                continue
            guess_count += 1

        except:
            print("An Error Occurred")

for key in history:
    for i in range(len(history[key])):
        if key == "Player 1":
            p1_score += history[key][i]["penalties"]
        if key == "Player 2":
            p2_score += history[key][i]["penalties"]

if p1_score < p2_score:
    print({f"Congratulations Player 1. You finished with {p1_score} penalties - and Player 2 finished with {p2_score} penalties. You won!!!!"})
elif p1_score > p2_score:
    print({f"Congratulations Player 2. You finished with {p2_score} penalties - and Player 1 finished with {p1_score} penalties. You won!!!!"})
else:
    print(f"Congratulations to both! You both finished with {p1_score}. You tied!!")

print(history)



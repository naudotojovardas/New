# Implement the hangman game using a TDD approach.
# Step 1: Set Up the Hangman Project
# Your hangman game will select a word, handle user input, and display all output using a text-based user interface. You need code to handle each of these tasks.
# However, you’ll do everything using built-in and standard-library tools. You don’t need to install anything else.
# Step 2: Select a Word to Guess
# The first step in playing hangman is to select the target word. When a human player selects a word for hangman, they pick one word from their own vocabulary.
# For the computer to select a word, it needs to have a vocabulary from which to select. Of course, its vocabulary doesn’t need to be as large as a human’s.
# Step 3: Get and Validate the Player’s Input
# Now, you need a way to get the player’s guesses at the command line. After all, a game isn’t much of a game if there isn’t some way for the player to influence the outcome.
# In your hangman game, you have to get the player’s input and make sure that it’s valid. Remember when you created your list of words?
# All the words were in lowercase, so you should turn the player’s guesses into lowercase letters as well.
# Additionally, the player shouldn’t be able to guess the same letter twice. It’d also be good to avoid numbers, special characters, and complete words as well.
# Step 4: Display the Guessed Letters and Word
# Once you’ve selected the target word in a real-life game of hangman, you need to write an underscore, or blank, for each letter in the word.
# These blanks tell the players how many letters are in the target word. 
# As players make guesses, you fill in the blanks with the correct letters. You should also keep track of incorrect letters, which you write to the side.
# Step 5: Draw the Hanged Man
# Of course, there’s no hangman game without the actual hanged man, is there?
# You could simply print out the number of guesses the player has taken. But if you want to make the game look like hangman, then showing the hanged man is a good idea.
# Implement a function draw_hanged_man that, depending on the integer passed, will show different ASCII pictures
# >>> draw_hanged_man(0)
#   -----
#   |   |
#       |
#       |
#       |
#       |
#       |
#       |
#       |
#       |
# -------
# >>> draw_hanged_man(6)
#   -----
#   |   |
#   O   |
#  ---  |
# / | \ |
#   |   |
#  ---  |
# /   \ |
# |   | |
#       |
# -------
# Step 6: Figure Out When the Game Is Over
# Games normally end due to a condition set up by the player’s input. Perhaps the player has finally reached the goal, or they failed some task and lost the game.
# Your hangman game ends when one of two events happens:
# The player makes six incorrect guesses.
# The player guesses the word correctly.
# Both of these outcomes stem from the player’s input. So, it makes sense to check for them in the game loop, which is where you gather, validate,
# and process all player input. Encapsulating these checks into a function is a good idea as well.
# Step 7: Run the Game Loop
# Up to this point, you’ve assembled the functions and code that cover most of the important parts of your hangman game. Those parts include the following:
# Selecting a random word to guess
# Gathering and processing the player’s input
# Showing the word with unguessed letters hidden
# Showing the hanged man drawing
# Tracking the letters guessed and guesses taken
# Checking if the game is over

import time
import random


def get_word():
    words = ["hangman", "chairs", "backpack", "bodywash", "clothing", "computer", "python", "program",
            "glasses", "sweatshirt", "sweatpants", "mattress", "friends", "clocks", "biology", "algebra",
            "suitcase", "knives", "ninjas", "shampoo", "conditioner", "perfume", "sewing", "friends", "family", "pizza"]
    return random.choice(words)


def get_guess():
    guess = input("Guess a letter: ")
    return guess.lower()


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legsg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    input('Guess a letter: ')

    while not guessed and tries > 0:
        print(word_completion)
        guess = get_guess()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))       

    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
        time.sleep(1)
        print("Goodbye!")
        time.sleep(1)


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
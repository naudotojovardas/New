# # Adjust your solution to first lesson's exercises using parametrization.


import time
import random
import pytest

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


@pytest.mark.parametrize("word", ["hangman", "chairs", "backpack", "bodywash", "clothing", "computer", "python", "program", "glasses",
                                   "sweatshirt", "sweatpants", "mattress", "friends", "clocks", "biology", "algebra", "suitcase", "knives",
                                   "ninjas", "shampoo", "conditioner", "perfume", "sewing", "friends", "family", "pizza"])

def test_get_word(word):
    assert word in ["hangman", "chairs", "backpack", "bodywash", "clothing", "computer", "python", "program", "glasses",
                    "sweatshirt", "sweatpants", "mattress", "friends", "clocks", "biology", "algebra", "suitcase", "knives",
                    "ninjas", "shampoo", "conditioner", "perfume", "sewing", "friends", "family", "pizza"]
    



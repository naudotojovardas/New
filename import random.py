import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Initialize a variable to keep track of the number of guesses
num_guesses = 0

# Start the guessing game
while True:
    # Get the user's guess
    guess = int(input("Guess the number between 1 and 10: "))
    
    # Increment the number of guesses
    num_guesses += 1
    
    # Check if the guess is correct
    if guess == random_number:
        print(f"Congratulations! You guessed the number in {num_guesses} attempts.")
        break
    elif guess < random_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

import random

Diffuculty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if Diffuculty == 'easy':
    attempts = 10
elif Diffuculty == 'hard':
    attempts = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1,100)
print(f"Pssst, the correct answer is {number}")

def check_answer(guess, number, attempts):
    """Checks answer against guess. Returns the number of attempts remaining."""
    if guess > number:
        print("Too high.")
        return attempts - 1
    elif guess < number:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {number}.")

def set_difficulty():
    """Sets the difficulty of the game."""
    if Diffuculty == 'easy':
        return 10
    else:
        return 5
    
attempts = set_difficulty()

guess = 0
while guess != number:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts = check_answer(guess, number, attempts)
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        break
    elif guess != number:
        print("Guess again.")


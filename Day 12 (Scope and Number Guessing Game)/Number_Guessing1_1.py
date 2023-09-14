from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_lEVEL_TURNS = 5

# make function to set difficulty
def  set_difficulty():
    level = input("Do you want 'easy' mode (10 turns) or 'hard' mode (5 turns)? ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_lEVEL_TURNS




#Make a function to check if the guess is correct. 
def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns number of turns remaining"""
    if guess > answer:
        print('Sorry, your guess is too high. Try again.')
        return turns -1
    elif guess < answer:
        print('Sorry, your guess is too low. Try again.')
        return turns -1
    else:
        print(f"Congratulations, you got it right! The correct answer was {answer}.")


def game():
    print('Welcome to the guessing game')
    print("I'm thinking of a number between 1 and 100.")
    #choosing a number between 1 and 100
    answer = random.randint(1,100)
    print(f'pss, the ansswer is {answer}')

    #Repeat the functionalit until they get it wrong
    guess = 0
    turns = set_difficulty()
    while guess != answer:
        print(f'You have {turns} attempts left to guess the number.')

        #Let user guess a number

        guess = int(input('Make a guess: '))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print('Sorry, you are out of guesses, you lost.')
            return False

    # Function to check users gues against acutal answer.

game()



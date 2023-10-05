# Include an ASCII art logo.
from art import logo

# Allow the player to submit a guess for a number between 1 and 100.
import random

def guess():
    return int(input('What number do you think I am thinking of? '))

# Check user's guess against the actual answer.
def check_guess(user, answer, lives):
    if user > answer:
        print('Sorry, your guess is too high. Try again.')
    elif user < answer:
        print('Sorry, your guess is too low. Try again.')
    else:
        print(f"Congratulations, you got it right! The correct answer was {answer}.")
        return True
    return False

def set_difficulty():
    difficulty = input("Do you want 'easy' mode (10 turns) or 'hard' mode (5 turns)? ").lower()
    if difficulty == 'easy':
        return 10
    elif difficulty == 'hard':
        return 5
    else:
        print("Invalid input. Defaulting to 'easy' mode (10 turns).")
        return 10

def play_game():
    print(logo)
    answer = random.randint(1, 100)
    print(f'Psst, the answer is {answer}')
    lives = set_difficulty()
    game_over = False
    
    while not game_over and lives > 0:
        user = guess()
        game_over = check_guess(user, answer, lives)
        lives -= 1

    if not game_over:
        print(f'Sorry, you ran out of lives. The correct answer was {answer}')

if __name__ == "__main__":
    game_running = True

    while game_running:
        play_game()
        play_again = input('Do you want to play again? (y/n): ').lower()
        if play_again != 'y':
            game_running = False

    print('Goodbye!')

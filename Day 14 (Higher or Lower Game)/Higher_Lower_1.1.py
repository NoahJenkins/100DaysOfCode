
import random
from art import logo
from art import vs
from game_data import data
import os

def clear():
    # Clear the terminal screen for Windows
    if os.name == 'nt':
        os.system('cls')
    # Clear the terminal screen for Unix/Linux/MacOS
    else:
        os.system('clear')

def run_game():
    score = 0
    game_running = True

    while game_running:
        print(logo)
        selected_subject_A = random.choice(data)
        choice_A = selected_subject_A['follower_count']
        print(f"Compare A: {selected_subject_A['name']}, a {selected_subject_A['description']} from {selected_subject_A['country']} with {choice_A} followers.")
        print(vs)
        selected_subject_B = random.choice(data)
        choice_B = selected_subject_B['follower_count']
        print(f"Compare B: {selected_subject_B['name']}, a {selected_subject_B['description']} from {selected_subject_B['country']} with {choice_B} followers.")

        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        if choice_A > choice_B and user_choice == 'a':
            score += 1
            print(f'That is correct! Your score is {score}')
        elif choice_A < choice_B and user_choice == 'b':
            score += 1
            print(f'That is correct! Your score is {score}')
        else:
            print(f'That is incorrect! Your final score is {score}')
            game_running = False


    continue_game = input("Do you want to continue? Type 'y' or 'n': ").lower()
    if continue_game != 'y':
        game_running = True
    else:
        print("Game Over")
        print(f"Your final score is {score}")

run_game()


    
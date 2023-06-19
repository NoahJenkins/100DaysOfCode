import os
import random
from art import logo, vs
from game_data import data

def clear():
    # Clear the terminal screen for Windows
    if os.name == 'nt':
        os.system('cls')
    # Clear the terminal screen for Unix/Linux/MacOS
    else:
        os.system('clear')

def turn_start(selected_subject_A, selected_subject_B):
    choice_A = selected_subject_A['follower_count']
    print(f"Compare A: {selected_subject_A['name']}, a {selected_subject_A['description']} from {selected_subject_A['country']} with {choice_A} followers.")
    print(vs)
    choice_B = selected_subject_B['follower_count']
    print(f"Compare B: {selected_subject_B['name']}, a {selected_subject_B['description']} from {selected_subject_B['country']} with {choice_B} followers.")
    return choice_A, choice_B

def run_game():
    score = 0
    game_running = True
    selected_subject_B = random.choice(data)

    while game_running:
        selected_subject_A = selected_subject_B
        selected_subject_B = random.choice(data)
        choice_A, choice_B = turn_start(selected_subject_A, selected_subject_B)

        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if choice_A > choice_B:
            correct_choice = 'a'
        else:
            correct_choice = 'b'

        if user_choice == correct_choice:
            score += 1
            print("That is correct!")
            clear()
        else:
            print("That is incorrect!")
            game_running = False

        print(f"Your score is {score}\n")

    print("Game Over")
    print(f"Your final score is {score}")

    continue_game = input("Do you want to continue? Type 'y' or 'n': ").lower()
    if continue_game == 'n':
        clear()
        return

    run_game()

run_game()

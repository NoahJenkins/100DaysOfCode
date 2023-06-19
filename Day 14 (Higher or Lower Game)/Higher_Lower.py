#Higher or Lower Game
# To Do List:
#   1. Import Random
#   2. Import game_data
#   3. Import art
#   4. Set up While Loop (game running)
#   5. Create Logic to ask for 2 sets of values from data. 
#   6. Create logic to compare both sets of data to see which is higher. 
#   7. Create logic to ask for user input selecting which is higher. 
#   8. Create logic to dermine if user wins or loses. 
#   9. create logic to keep track of score. 
#   10. Ending game logic (print score)


import random
from art import logo
from art import vs
from game_data import data

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
            print("That is correct!")
        elif choice_A < choice_B and user_choice == 'b':
            score += 1
            print("That is correct!")
        else:
            print("That is incorrect!")
            game_running = False

        print(f"Your score is {score}")
        print()

        continue_game = input("Do you want to continue? Type 'y' or 'n': ").lower()
        if continue_game != 'y':
            game_running = False

    print("Game Over")
    print(f"Your final score is {score}")

run_game()


    
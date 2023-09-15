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
from art import logo, vs
from game_data import data

def run_game():
    score = 0
    game_running = True
    selected_subject_B = random.choice(data)

    while game_running:
        print(logo)
        selected_subject_A = selected_subject_B
        choice_A = selected_subject_A['follower_count']
        print(f"Compare A: {selected_subject_A['name']}, a {selected_subject_A['description']} from {selected_subject_A['country']} with {choice_A} followers.")
        print(vs)
        selected_subject_B = random.choice(data)
        choice_B = selected_subject_B['follower_count']
        print(f"Compare B: {selected_subject_B['name']}, a {selected_subject_B['description']} from {selected_subject_B['country']} with {choice_B} followers.")

        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if choice_A > choice_B:
            correct_choice = 'a'
        else:
            correct_choice = 'b'

        if user_choice == correct_choice:
            score += 1
            print("That is correct!")
        else:
            print("That is incorrect!")
            game_running = False

        print(f"Your score is {score}\n")

    print("Game Over")
    print(f"Your final score is {score}")

    continue_game = input("Do you want to continue? Type 'y' or 'n': ").lower()
    if continue_game == 'y':
        run_game()

run_game()



    
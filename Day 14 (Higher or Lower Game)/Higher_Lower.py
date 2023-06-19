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

game_running == True


def run_game():
    score = 0
    print(logo)
    selected_subject_A = random.choice(data)
    Chocie_A = selected_subject['follower_count']
    Print(f'Compare A')
    print(vs)
    selected_subject_B = random.choice(data)
    Chocie_B = selected_subject['follower_count']
    Print(f'Compare B')
    user = input('Who has more followers? Type "A" or "B":').lower()
    if Choice_A > Choice_B and user == 'a':
        score =+ 1
        print("That is Correct!")
        print(f'Your score is {score}')
    elif Choice_A < Choice_B and user == 'b':
        score =+ 1
        print("That is Correct!")
        print(f'Your score is {score}')
    else:
        print("That is Incorrect!")
        print(f'Your score is {score}')
        game_running = False
        print("Game Over")
        print(f'Your score is {score}')
        continue_game = input("Do you want to continue? Type 'y' or 'n': ").lower()
        if continue_game == 'y':
            game_running = True
        else:
            game_running = False
            print("Game Over")
            print(f'Your score is {score}')

run_game()


    
import random
import os
from art import logo
from art import vs
from game_data import data


def clear():
    """This function will cleae the terminal. Please note that you must 'import os' for this to work."""
    # Clear the terminal screen for Windows
    if os.name == 'nt':
        os.system('cls')
    # Clear the terminal screen for Unix/Linux/MacOS
    else:
        os.system('clear')

def grab_data():
    random_subject = random.choice(data)
    name = random_subject['name']
    follower = random_subject['follower_count']
    description = random_subject['description']
    country = random_subject['country']
    return name, follower, description, country

subject_A = grab_data()
subject_B = grab_data()

score = 0


game_running = True

while game_running:
    print(logo)

    print(f'The current score is {score}')
    print(f'Compare A: {subject_A[0]}, a {subject_A[2]}, from {subject_A[3]}')
    print(subject_A[1])

    print(vs)

    print(f'Compare B: {subject_B[0]}, a {subject_B[2]}, from {subject_B[3]}')
    print(subject_B[1])

    if subject_A[1] > subject_B[1]:
        answer = 'a'
    else:
        answer = 'b'

    question = input('Who do you think has a higher follower count? A or B: ').lower()

    
    if answer == question:
        score += 1
        if subject_B[1] > subject_A[1]:
            subject_A = subject_B
        subject_B = grab_data()
        if subject_A[0] == subject_B[0]:
            subject_B = grab_data()
        
        clear()
        
    else:
        game_running = False
       

print(f'Game Over, the final score is {score}')






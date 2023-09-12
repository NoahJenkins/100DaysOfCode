import random
from art import logo

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

user_cards = []
computer_cards = []

def deal_card_user():
    user_cards.append(random.choice(cards)) 
def deal_card_computer():
    computer_cards.append(random.choice(cards))

user_hand = sum(user_cards)
computer_hand = sum(computer_cards)


def round():
    user_choice = input(f'Your hand is current at {user_hand}, do you want to draw another card? "yes" or "no": ').lower
    if user_choice == 'yes':
        deal_card_user()
    elif computer_hand > 17:
        deal_card_computer()


start_game = [1,2]

for number in start_game:
    deal_card_user()
    deal_card_computer

game_running = True

def check_score():
    if user_hand > 21:
        print(f'You busted, sorry. Your hand is {user_hand - 21} too high.')
        game_running == False
    if computer_hand > 21:
        print("The computer busted, looks like it's your lucky day. You Win!")
        game_running == False

def check_winner():
    if user_hand > computer_hand and user_hand <= 21:
        print('Congragulations, you win!')
        game_running == False
    if computer_hand > user_hand and computer_hand <= 21:
        print('Sorry, you lose.')
        game_running == False
    if computer_hand == user_hand and computer_hand <= 21:
        print("It's a draw! What are the odds?")
        game_running == False

while game_running:
    round()
    check_score()

# if game_running == False:
#     play_again = input('Do you want to play again? "yes" or "no': ).lower
#     if play_again == 'yes':







    
    
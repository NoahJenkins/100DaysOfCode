import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_hand = []
npc_hand = []

user_count = 0
npc_count = 0

def deal_card():
    return random.choice(cards)

def calculate_score(hand):
    score = sum(hand)
    if score == 21 and len(hand) == 2:
        return 0
    if 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def compare(user_score, npc_score):
    if user_score == npc_score:
        return "Draw"
    elif npc_score == 0:
        return "You lose, the opponent has Blackjack."
    elif user_score == 0:
        return "You Win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose."
    elif npc_score > 21:
        return "The Opponent went over. You win!"
    elif user_score > npc_score:
        return "You win!"
    else:
        return "You lose!"
    
def play_game():
    user_hand.append(deal_card())
    user_hand.append(deal_card())
    npc_hand.append(deal_card())
    npc_hand.append(deal_card())
    game_running = True

    while game_running:
        user_count = calculate_score(user_hand)
        npc_count = calculate_score(npc_hand)
        print(f"Your cards: {user_hand}, current score: {user_count}")
        print(f"Computer's first card: {npc_hand[0]}")

        if user_count == 0 or npc_count == 0 or user_count > 21:
            game_running = False
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_hand.append(deal_card())
            else:
                game_running = False

    while npc_count != 0 and npc_count < 17:
        npc_hand.append(deal_card())
        npc_count = calculate_score(npc_hand)

    print(f"Your final hand: {user_hand}, final score: {user_count}")
    print(f"Computer's final hand: {npc_hand}, final score: {npc_count}")
    print(compare(user_count, npc_count))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    user_hand = []
    npc_hand = []
    play_game()

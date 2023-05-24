from replit import clear
from art import logo

print(logo)

players = {}

def silent_auction():
  player_name = input("What is the player's name? ")
  player_bid = input("What is the player's bidding amount? $")
  players[player_name] = player_bid

live_auction = True

while live_auction:
  silent_auction()
  choice = input("Does anyone else want to bid? Yes or No: ").lower()
  if choice == 'yes':
    live_auction = True
    clear()
  else:
    live_auction = False

if players:
  winner = max(map(int, players.values()))
  result_dict = {key: value for key, value in players.items() if int(value) == winner}
  print(result_dict)
else:
  print("No players or bids entered.")

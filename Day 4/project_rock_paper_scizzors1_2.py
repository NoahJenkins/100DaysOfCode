rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
#Write your code below this line 👇
import random

number = input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors? ")
print('You chose:')
player = int(number)
print(game_images[player])


#0 = rock, 1 = Paper, 2 = scissorsizzor

player = int(number)

NPC = random.randint(0,2)
print("Computer Chose:")
print(game_images[NPC])


win = "Congrats, you win!"
loss = "Sorry, you lose."
if player == NPC:
  print("Amazing, it's a Draw! What are the odds?")
elif player == 0 and NPC == 2:
  print(win)
elif NPC == 0 and player ==2:
  print(loss)
elif player > NPC:
  print(win)
elif NPC > player:
  print(loss)
else:
  print("Sorry, that is an invalid choice. You loose")
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

#Write your code below this line 👇
import random

number = input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors? ")

#0 = rock, 1 = Paper, 2 = scissorsizzor

player = int(number)

NPC = random.randint(0,2)

win = "Congrats, you win!"

if player == NPC:
  print("Amazing, it's a Draw! What are the odds?")
elif player == 0 and NPC == 2:
  print("Player chose:" + rock + "NPC chose:" + scissors + win)
elif player == 1 and NPC == 0:
  print("Player chose:" + paper + "NPC chose:" + rock + win)
elif player == 2 and NPC == 1:
  print("Player chose:" + scissors + "NPC chose:" + paper + win)
else:
  print("Sorry, you loose")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input("Do you want to go 'right' or 'left'? ")
choice1L = choice1.lower()

if choice1L == "left":
  choice2 = input("You have arrived at a lake. Do you 'swim' through it, or go 'wait' to see what happens? ")
  choice2L = choice2.lower()
  if choice2L == "wait":
    choice3 = input("You have made your way to 3 doors. A 'red', 'yellow', and 'blue' door stand before you. Which door do you enter? ")
    choice3L = choice3.lower()
    if choice3L == 'yellow':
      print("Congratulations, you win!")
    elif choice3L == 'red':
      print('You have been burned by fire. Game Over.')
    elif choice3L == 'blue':
      print("You have been eaten by a beast. Game Over.")
    else:
      print("By not choosing an option, you have chosen death. Game Over.")
    
  else:
    print("You have been eaten by a very hungry trout. Game over.")

else:
  print("Ahhhhh, you fell into a hole. Game Over.")
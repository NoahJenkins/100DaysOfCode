from Coffee_Data import resources
from Coffee_Data import MENU
import os

# *****FUNCTIONS/METHODS*****

def clear():
    """This function will cleae the terminal. Please note that you must 'import os' for this to work."""
    # Clear the terminal screen for Windows
    if os.name == 'nt':
        os.system('cls')
    # Clear the terminal screen for Unix/Linux/MacOS
    else:
        os.system('clear')

def report():
    """This function will show to current resources in the coffee machine."""
    for key, value in resources.items():
        print(f"{key}: {value}")

def show_menu():
    """This function will ask the user to deside their drink selection, it can also be used
    to turn off the machine or pull a report with the secret inputs"""
    return str(input("What would you like? (espresso ($1.50) /latte ($2.50) /cappuccino ($3.0)): ")).lower()
    
def drink_selection(user_choice):
    """This function will take the user choice, and assign the recourse required to make it and 
    the cost to purchase it. It will also pass along the user secred code for the secret functions"""
    if user_choice == "report":
        return 'report'
    elif user_choice == 'espresso':
        drink =  MENU["espresso"]
        return drink
    elif user_choice == 'latte':
        drink = MENU["latte"]
        return drink
    elif user_choice == 'cappuccino':
        drink = MENU["cappuccino"]
        return drink
    elif user_choice == 'off':
        return 'off'
    else:
        print("I'm sorry, that is not a valid selection, please try again: ")
        user_choice = show_menu()
        return drink_selection(user_choice)
    
def check_resources(drink):
    """This function will check if there are enouch recourses in the machine to
    make the selected drink."""
    if resources["water"] < drink["ingredients"]['water']:
        print("Sorry, there is not enough water.")
        return False
    elif resources["milk"] < drink["ingredients"]['milk']:
        print("Sorry, there is not enough milk.")
        return False
    elif resources["coffee"] < drink["ingredients"]['coffee']:
        print("Sorry, there is not enough coffee.")
        return False
    else:
        return True
    
def process_coins():
    """This function will will take the users payment, and calculate it's total value."""
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickels?: "))
    pennies = float(input("How many pennies?: "))
    return (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)
       
def check_transaction(drink, total_coins):
    """This function will will take the users payment, and calculate if it is enouch
    to purchase their selected drink. It will return the change if it is not enouch,
    and will return the correct change if they overpayed."""
    if total_coins < drink["cost"]:
        print("Sorry, that's not enough money. Pyament refunded.")
        return False
    elif total_coins > drink["cost"]:
        change = round(total_coins - drink["cost"], 2)
        print(f"Here is ${change} in change.")
        return True
    else :
        print('That is the perfect ammount, thank you!')
        return True

def barista(drink, user_choice):
    """This function will will efffectively make the users drink, it will take
    the current amount of recourses and subtract the required ammount to make
    the users selected drink, then update the recourses dictionary to the new vaule
    after the drink has been made."""
    new_water = (resources["water"] - drink["ingredients"]['water'])
    new_milk = (resources["milk"] - drink["ingredients"]['milk'])
    new_coffee = (resources["coffee"] - drink["ingredients"]['coffee'])
    print(f'Here is your {user_choice}, please enjoy!')
    return {
    "water": new_water,
    "milk": new_milk,
    "coffee": new_coffee,
}

# *****Production Code *****

cafe_on = True
while cafe_on:
    user_choice = show_menu()
    if user_choice == 'off':
        cafe_on = False
    elif user_choice == 'report':
        report()
    else:
        drink = drink_selection(user_choice)
        print(drink["cost"])
        check_resources(drink)
        total_coins = process_coins()
        payment = check_transaction(drink, total_coins)
        resources = barista(drink, user_choice)

clear()
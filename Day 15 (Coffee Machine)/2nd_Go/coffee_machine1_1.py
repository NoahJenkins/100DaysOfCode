from Coffee_Data import coins
from Coffee_Data import resources
from Coffee_Data import MENU

# coins = {
#     "quarters": 0.25,
#     "dimes": 0.10,
#     "nickles": 0.05,
#     "pennies": 0.01,
# }

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }


# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#Create a function to check current recourses

# *****GLOBAL VARIABLES*****
user_choice = ""
drink = ''
cafe_running = True

# *****FUNCTIONS/METHODS*****


def report():
    for key, value in resources.items():
        print(f"{key}: {value}")


def show_menu():
    return input("What would you like? (espresso ($1.50) /latte ($2.50) /cappuccino ($3.0)): ").lower()
    

def drink_selection(user_choice):
    if user_choice == "report":
        report()
        user_choice = show_menu()
        return drink_selection(user_choice)
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
        cafe_running = False
        return
    else:
        print("I'm sorry, that is not a valid selection, please try again: ")
        user_choice = show_menu()
        return drink_selection(user_choice)
    
def check_resources(drink):
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
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickels?: "))
    pennies = float(input("How many pennies?: "))
    # return (quarters * coins["quarters"]) + (dimes * coins["dimes"]) + (nickels * coins["nickels"]) + (pennies * coins["pennies"])
    return (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)


        
def check_transaction(drink, total_coins):
    if total_coins < drink["cost"]:
        print("Sorry, that's not enough money. Pyament refunded.")
        return False
    elif total_coins > drink["cost"]:
        change = round(total_coins - drink["cost"], 2)
        print(f"Here is ${change} in change.")
        return True
    else :
        return True


print(coins)
user_choice = show_menu()
print(user_choice)
drink = drink_selection(user_choice)
print(drink)
print(drink["cost"])
check_resources(drink)
total_coins = process_coins()
payment = check_transaction(drink, total_coins)
#make drink




# while cafe_running:
#     user_choice = show_menu()
# print(user_choice)
# drink = drink_selection(user_choice)
# print(drink)
# if drink["ingredients"]['water'] < resources['water'] or drink["ingredients"]['coffee'] < resources['coffee'] or drink["ingredients"]['milk'] < resources('milk'):
#     print(f"I'm sorry, we do not have enouch ingredients for {user_choice}, please try a different selection.")
    
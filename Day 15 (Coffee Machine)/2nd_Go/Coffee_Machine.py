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
    else:
        print("I'm sorry, that is not a valid selection, please try again: ")
        user_choice = show_menu()
        return drink_selection(user_choice)
        

user_choice = show_menu()
print(user_choice)
drink = drink_selection(user_choice)
print(drink)

# espresso_ingredients = MENU["espresso"]["ingredients"]

# print(drink["ingredients"]['water'])

def check_resource(drink, user_choice):
    required_water = drink["ingredients"]['water']
    required_coffee = drink["ingredients"]['coffee']
    required_milk = drink["ingredients"]['milk']

    if required_water < resources['water'] or required_coffee < resources['coffee'] or required_milk < resources('milk'):
        print(f"I'm sorry, we do not have enouch ingredients for {user_choice}, please try a different selection.")
        return
    else:
        print(f'Awesome choice! The {user_choice} cost {drink["cost"]}')
        return drink["cost"]

cost_drink = check_resource(drink, user_choice)
print(check_resource)

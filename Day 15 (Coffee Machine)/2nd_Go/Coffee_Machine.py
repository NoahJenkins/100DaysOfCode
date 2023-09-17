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

def check_resources():
    for key, value in resources.items():
        print(f"{key}: {value}")


def show_menue():
    user_choice = input("What would you like? (espresso ($1.50) /latte ($2.50) /cappuccino ($3.0)): ").lower()
    return user_choice

def report():
    if user_choice == "report":
        check_resources()
    elif user_choice == 'expresso':
        drink =  MENU["expresso"]
        return drink
    elif user_choice == 'latte':
        drink == MENU["latte"]
        return drink
    elif user_choice == 'cappaccino':
        drink == MENU["cappuccino"]
    else:
        print("I'm sorry, that is not a valid selection, please try again: /n")
        show_menue()
        report()

report()
print(drink)

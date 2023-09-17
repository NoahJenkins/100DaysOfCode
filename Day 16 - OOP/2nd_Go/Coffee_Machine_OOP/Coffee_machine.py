from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os
def clear():
    """This function will cleae the terminal. Please note that you must 'import os' for this to work."""
    # Clear the terminal screen for Windows
    if os.name == 'nt':
        os.system('cls')
    # Clear the terminal screen for Unix/Linux/MacOS
    else:
        os.system('clear')


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_running = True

while machine_running:
    options = menu.get_items()
    user_choice = input(f"What drink would you like? ({options}): ")
    if user_choice == "off":
        machine_running = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink) 
clear()
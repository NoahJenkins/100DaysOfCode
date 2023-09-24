#Steve Jobs OOP Quote: "Object-oriented programming teaches you to think about the world in terms of objects that interact with one another. "

#Coffee Machine OOP

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
 
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_running = True

while machine_running:
    options = menu.get_items()
    choice = input(f"What drink would you like? ({options}): ")
    if choice == "off":
        machine_running = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink) 

clear()



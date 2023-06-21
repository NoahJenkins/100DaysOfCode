# #Program Requirements:
# 1. Print a report of all coffee machine resources
# 2. Check resources sufficient to make drink order
# 3. Process coins
# 4. Check transaction successful
# 5. Make coffee and deduct resources

from Coffee_Data import MENU, resources, coins

def check_resources(user_choice):
    if resources["water"] < MENU[user_choice]["ingredients"]["water"]:
        print("Sorry, there is not enough water.")
        return False
    elif resources["milk"] < MENU[user_choice]["ingredients"]["milk"]:
        print("Sorry, there is not enough milk.")
        return False
    elif resources["coffee"] < MENU[user_choice]["ingredients"]["coffee"]:
        print("Sorry, there is not enough coffee.")
        return False
    else:
        return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total_coins = (quarters * coins["quarters"]) + (dimes * coins["dimes"]) + (nickels * coins["nickels"]) + (pennies * coins["pennies"])
    return total_coins

def check_transaction(user_choice, total_coins):
    if total_coins < MENU[user_choice]["cost"]:
        print("Sorry, that's not enough money. Pyament refunded.")
        return False
    elif total_coins > MENU[user_choice]["cost"]:
        change = round(total_coins - MENU[user_choice]["cost"], 2)
        print(f"Here is ${change} in change.")
        global coins
        coins["quarters"] = 0.25
        coins["dimes"] = 0.10
        coins["nickels"] = 0.05
        coins["pennies"] = 0.01
        return True
    

def make_coffee(user_choice):
    resources["water"] -= MENU[user_choice]["ingredients"]["water"]
    resources["milk"] -= MENU[user_choice]["ingredients"]["milk"]
    resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
    print(f"Here is your {user_choice}. Enjoy!")

cafe_on = True
while cafe_on:
    user_choice = input("What would you like? ($1.50 espresso/ $2.50 latte/ $3.00 cappuccino): ").lower()
    if user_choice == "off":
        cafe_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${coins}")
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        if check_resources(user_choice):
            total_coins = process_coins()
            if check_transaction(user_choice, total_coins):
                make_coffee(user_choice)
    else: 
        print("Please enter a valid option.")






   

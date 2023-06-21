# #Program Requirements:
# 1. Print a report of all coffee machine resources
# 2. Check resources sufficient to make drink order
# 3. Process coins
# 4. Check transaction successful
# 5. Make coffee and deduct resources

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = 0  # Initialize coins variable with 0

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

cafe_on = True
while cafe_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        cafe_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${coins}")
    elif user_choice in ["espresso", "latte", "cappuccino"]:
        if check_resources(user_choice):
            total_coins = process_coins()
            if total_coins < MENU[user_choice]["cost"]:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                change = total_coins - MENU[user_choice]["cost"]
                print(f"Here is ${change:.2f} in change.")
                print(f"Here is your {user_choice} ☕️. Enjoy!")
                resources["water"] -= MENU[user_choice]["ingredients"]["water"]
                resources["milk"] -= MENU[user_choice]["ingredients"]["milk"]
                resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
                coins += MENU[user_choice]["cost"]
    else:
        print("Invalid input. Please try again.")




   

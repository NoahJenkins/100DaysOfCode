# #Program Requirements:
# 1. Print a report of all coffee machine resources
# 2. Check resources sufficient to make drink order
# 3. Process coins
# 4. Check transaction successful
# 5. Make coffee and deduct resources

from Coffee_Data import MENU, resources

cafe_on = True
while cafe_on == True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        cafe_on = False
    elif user_choice == "report":
        print(f"Water: {Coffee_Data.resources['water']}ml")
        print(f"Milk: {Coffee_Data.resources['milk']}ml")
        print(f"Coffee: {Coffee_Data.resources['coffee']}g")
        print(f"Money: ${Coffee_Data.money}")
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        if Coffee_Data.check_resources(user_choice) == True:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total = Coffee_Data.process_coins(quarters, dimes, nickles, pennies)
            if total >= Coffee_Data.MENU[user_choice]["cost"]:
                change = round(total - Coffee_Data.MENU[user_choice]["cost"], 2)
                print(f"Here is ${change} in change.")
                Coffee_Data.make_coffee(user_choice)
            else:
                print("Sorry, that's not enough money. Money refunded.")
        else:
            print("Sorry, there is not enough resources.")
    else:
        print("Invalid input. Please try again.")


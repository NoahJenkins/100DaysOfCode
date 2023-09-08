names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random

victim = random.choice(names)

print(f"{victim} is going to pay today!")

# or
#num_items = len(names)
#random_choice = random.randint(0, num_items - 1)
#person_who_will_pay = names[random_choice]
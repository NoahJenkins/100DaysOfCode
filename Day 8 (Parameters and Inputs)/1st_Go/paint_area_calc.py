# Exercise: Paint Area Calculator


#Write your code below this line 👇

import math
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5


number_of_cans = test_h * test_w / coverage
rounded_number_of_cans = math.ceil(number_of_cans)
print(f"You'll need {rounded_number_of_cans} cans of paint.")







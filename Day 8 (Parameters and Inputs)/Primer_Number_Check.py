#Write your code below this line 👇

import math

def check_prime(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# Write your code above this line 👆

# Do NOT change any of the code below👇
while 1==1:
    n = int(input("Check this number: "))
    check_prime(number=n)
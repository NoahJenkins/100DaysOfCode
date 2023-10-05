#Write your code below this line 👇

import math

def check_prime(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            #Not a prime
            is_prime = False
    if is_prime == True:
        print(f'{number} is a prime number')
    else:
         print(f'{number} is not a prime number.')

    


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
check_prime(number=n)
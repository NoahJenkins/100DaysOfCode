x = int(input("Type in whole number. "))

y = x % 2

if y == 1:
  print("Your number is odd.")
else:
  print("Your number is even/")

# Modulo is the % sign. It divides the number and returns the remainder.
# If the remainder is 0, then the number is even. If the remainder is 1, then the number is odd.
# This is because even numbers are divisible by 2, and odd numbers are not.
# The modulo operator is useful for determining if a number is even or odd.
# It is also useful for determining if a number is divisible by another number.
# For example, if you want to know if a number is divisible by 3, you can use the modulo operator to determine if the remainder is 0.
# If the remainder is 0, then the number is divisible by 3.
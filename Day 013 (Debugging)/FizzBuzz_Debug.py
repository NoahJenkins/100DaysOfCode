# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])


#FIX: The first if statment was an or, it should have been an and. The second and third if statements should have been elif statements. The else statement should have been an elif statement.
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print([number])
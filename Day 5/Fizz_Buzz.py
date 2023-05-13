for number in range(1,101,):
    if number % 5 == 0 and number % 3 == 0:
      print("Fizz Buzz")
    if number % 5 == 0:
      print("Buzz")
    if number % 3 == 0:
      print("Fizz ")
    else:
      print(number)

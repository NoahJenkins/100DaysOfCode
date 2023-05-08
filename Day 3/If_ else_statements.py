

  #what are comparison operators?
    # > greater than
    # < less than
    # >= greater than or equal to
    # <= less than or equal to
    # == equal to
    # != not equal to


#Nesting if statements and elif statements in python
# elif is short for else if
# elif is used when you have more than 2 conditions
# if you have more than 2 conditions, you can use elif
# example:
# if condition1:
#   do A
# elif condition2:
#   do B
# elif condition3:
#   do C
# else:
#   do D
# if condition1 is true, then do A
# if condition1 is false, then check condition2
# if condition2 is true, then do B
# if condition2 is false, then check condition3
# if condition3 is true, then do C
# if condition3 is false, then do D
# if none of the conditions are true, then do D


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")

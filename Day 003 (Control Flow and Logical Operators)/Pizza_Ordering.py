print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


sub_price = 0
if size == "L":
  sub_price += 25
  if add_pepperoni == "Y":
    sub_price += 3
elif size == "M":
    sub_price += 20
    if add_pepperoni == "Y":
      sub_price += 3
elif size == "S":
  sub_price += 15
  if add_pepperoni == "Y":
    sub_price += 2

if extra_cheese == "Y":
  sub_price += 1


print(f"Your total is ${sub_price}.")
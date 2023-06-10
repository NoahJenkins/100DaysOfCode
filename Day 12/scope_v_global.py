#NameSpaces: Global vs Local
#Global variables are the one that are defined and declared outside a function and we need to use them inside a function.
#If a variable with same name is defined inside the scope of function as well then it will print the value given inside the function only and not the global value.
enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
#Output:
# enemies inside function: 2
# enemies outside function: 1

#If we want to use the global variable inside a function where we have defined a local variable with same name, we can use the global keyword.
enemies = 1

def increase_enemies():
    global enemies
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
#Output:
# enemies inside function: 2
# enemies outside function: 2



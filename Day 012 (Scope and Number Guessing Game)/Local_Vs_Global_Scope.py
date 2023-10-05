################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")
#   enemies inside function: 2

increase_enemies()
print(f"enemies outside function: {enemies}")
# enemies outside function: 2

#Local Scope

# def drink_potion():
#   potion_strenth = 2
#   print(potion_strenth)

# drink_potion()
# print(potion_strenth)
#Notice how the potion strength is not defined in the line above, this is becuase it is
#only defined in the method drink_potion, and cannot be called outside of it. 

# anything you define is in  a namespece. A variable defined in a method has a local namespace. 

#Modifying Global Scope
enemies = "Skeleton"

def increase_enemies():
  enemies = "zombies"
  print(f"enemies inside function: {enemies}")
#   enemies inside function: zombies

increase_enemies()
print(f"enemies outside function: {enemies}")
#   enemies outside function: skeleton

enemies = 1

def increase_enemies():
  global enemies
  #the global functiont takes the variable into the method, and allows it to be modified. 
  enemies += 1
  print(f"enemies inside function: {enemies}")
#   enemies inside function: 2

increase_enemies()
print(f"enemies outside function: {enemies}")
#   enemies outside function: 2

#Using return:

enemies = 1

def increase_enemies():
  return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

#Global COnstants:

PI = 3.114159
#The naming convention for a Global cosntnce is to you all caps, this does not affect the code,
#but is common practice. 



#Block Scope
#Variables declared inside the block are not available outside of the block:
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]
print(new_enemy)
#Output:
# NameError: name 'new_enemy' is not defined
#
#Modifying Global Scope
#If we want to modify a global variable inside a function, we can use the global keyword.
enemies = 1
def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")
increase_enemies()
print(f"enemies outside function: {enemies}")
#Output:
# enemies inside function: 2
# enemies outside function: 2

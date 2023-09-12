#There is no Block scope:

game_level = 3
enemies = ['Skeleton', "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

# if else, and lopps (for/while) statements do not put a fence around a variable, 
# and it can be called in what ever namescape (by default global) it is in. 

import prettytable

table = prettytable.PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"]) 
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

# Output:
# +---------------+----------+
# | Pokemon Name  | Type     |
# +---------------+----------+
# | Pikachu       | Electric |
# | Squirtle      | Water    |
# | Charmander    | Fire     |
# +---------------+----------+

#Note that prettytable is not currently supported in Python 3.11.4, I used Python 3.9.13 to run this code.


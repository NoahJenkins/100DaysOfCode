
import prettytable

# Creates a table object, this is a class of the prettytable package.
table = prettytable.PrettyTable()

# Adds columns to the table object, this is a method of the table object.
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"]) 
table.add_column("Type", ["Electric", "Water", "Fire"])

# Aligns the text to the left of the column, this is an attribute of the table object.
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


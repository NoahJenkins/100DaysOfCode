#PyPi stands for Python Package index. 
#Look at documentation for instructions on install.
# Here is the command to install PrettyTable:
# python -m pip install -U prettytable

from prettytable import PrettyTable
table = PrettyTable()

table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Pokemon Type', ['Eletric,', 'Water', 'Fire'])
print(table)

# the above (add column) changes are examples of methods. 

#The code above is an example of a method, it is changing the text allignment from center to left
table.align = 'l'
print(table)
#
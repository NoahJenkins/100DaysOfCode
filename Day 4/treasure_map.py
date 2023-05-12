
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


row = int(position[1]) - 1   
column = int(position[0]) - 1
map[row][column] = "X"

#The code converts the input into row and column indices by subtracting 1 from each digit to account for zero-based indexing in Python.

print(f"{row1}\n{row2}\n{row3}")

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

#horizontal = int(position[0])
#vertical = int(position[1])

#map[vertical - 1][horizontal - 1] = "X"
#if input is 23, then 2 is the vertical and 3 is the horizontal

column = int(position[1]) - 1   
row = int(position[0]) - 1
map[column][row] = "X"

#The code converts the input into row and column indices by subtracting 1 from each digit to account for zero-based indexing in Python.

print(f"{row1}\n{row2}\n{row3}")

#why is the X ouputted when the map ie printed again? 

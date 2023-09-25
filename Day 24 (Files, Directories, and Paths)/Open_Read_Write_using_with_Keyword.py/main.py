#The below is to show you the current directory level.
# import os
# cwd = os.getcwd()
# files = os.listdir(cwd)
# print(cwd, files)


# path = "C:\\Code\\100DaysOfCode\\Day 24 (Files, Directories, and Paths)\\Open_Read_Write_using_with_Keyword.py\\my_file.txt"
# file = open(path)

path = "Day 24 (Files, Directories, and Paths)\\Open_Read_Write_using_with_Keyword.py\\my_file.txt"
# file = open(path)

# contents = file.read()
# print(contents)
# file.close()


# Using the with keyword will close the file after it has been used. 
with open(path, mode = "a") as file:
    file.write('\nNew text')

# modes:
# w = write
# r=read
# a=append

#This code will create a new file. 
with open("new_file.txt", mode = "w") as file:
    file.write('New text in new file. ')
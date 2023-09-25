#The below is to show you the current directory level.
# import os
# cwd = os.getcwd()
# files = os.listdir(cwd)
# print(cwd, files)


# path = "C:\\Code\\100DaysOfCode\\Day 24 (Files, Directories, and Paths)\\Open_Read_Write_using_with_Keyword.py\\my_file.txt"
# file = open(path)

path = "Day 24 (Files, Directories, and Paths)\\Open_Read_Write_using_with_Keyword.py\\my_file.txt"
file = open(path)

contents = file.read()
print(contents)
file.close()
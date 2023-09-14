############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   #Had to change the range to 21, ince range does not include the last number. 
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# #Had to update the range below to 0-5, since list position starts at 0, meaning 6 was out of range. 
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# #updated if statment to include = so 1980, and 1994 are captured.
# if year >= 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
#   #added new elif statment to capture values < 1980. 
# elif year <1980:
#   print('You are just old.')

# # Fix the Errors
# #added int so captured input is an int and not a string. 
# age = int(input("How old are you?"))
# #reversed the < sign so that ages below 17 are told when they can drive.
# if age < 18:
#   #had to indent line below so it fits in "if" block. Also converted to f string. 
#   print(f"You can drive at age {age}.")
#   #added else so numbers greater than or equal to 18 have an output.
# else:
#   print("You can drive. Don't text and drive.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# #the below line previosly had ==, instead of =, this prevent the variable from equalling the user input. 
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(pages)
# print(word_per_page)
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     #had to indent the code below so it falls under the for loop, allowig each item to be appended to the new list.
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])
# #Exception Handling

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up.")

#BMI Calcluator

# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("The hight you iputed is way to high.")

# bmi = weight / height ** 2
# print(bmi)

#Challenge 1:
# fruits = eval(input())
# 🚨 Do not change the code above

# TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#         print(fruit + " pie")
#     except IndexError:
#         print("Index out of range. Please provide a valid index.")

# # Example usage:
# make_pie(2)  # Replace 2 with the desired index

#Challenge 2:
# eval() function will create a list of dictionaries using the input
# facebook_posts = eval(input())

# total_likes = 0
# # TODO: Catch the KeyError exception
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass

# print(total_likes)


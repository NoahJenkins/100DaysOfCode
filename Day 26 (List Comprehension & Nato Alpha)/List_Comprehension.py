#List Copmprehension

# numbers = [1,2,3]
# #new_list =[new_item for item in list]
# new_number = [n+1 for n in numbers]
# print(new_number)

# name = "Noah"
# name_list = [letter for letter in name]
# print(name_list)

# number_range = range(1,5)
# new_number_range = [num*2 for num in number_range]
# print(new_number_range)

#Conditional List Comprehension
# new_list = [new_item for item in list if test]

names = ['Alex', 'Beth', "Caroline", 'Dave', "Eleanor", 'Freddie']
short_names = [name for name in names if len(name) < 4]
print(short_names)


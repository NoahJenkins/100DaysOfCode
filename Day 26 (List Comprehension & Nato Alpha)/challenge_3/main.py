import pandas

file_1 = pandas.read_csv('file1.txt', header=None, names=['Numbers'])
list_1 = file_1['Numbers'].to_list()
print(list_1)

file_2 = pandas.read_csv('file2.txt', header=None, names=['Numbers'])
list_2 = file_2['Numbers'].to_list()
print(list_2)

same_value = [num for num in list_1 if num in list_2]
print(same_value)

#################################################################################

with open('file1.txt') as file1:
    file_1_data = file1.readlines()

with open('file2.txt') as file2:
    file_2_data = file2.readlines()

result = [int(num) for num in file_1_data if num in file_2_data]
print(result)
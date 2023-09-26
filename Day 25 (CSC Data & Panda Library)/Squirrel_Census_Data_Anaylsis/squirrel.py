import pandas

#primary fur color
gray_color = "Gray"
cinnamon_color = "Cinnamon"
black_color = "Black"

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')



data_dict = data.to_dict()

primary_fur = data['Primary Fur Color'].to_list()


#gray count
gray_data = data[data['Primary Fur Color'] == gray_color]
gray_count = len(gray_data)
print(f'The number of gray squirrels is {gray_count}.')

cinnamon_data = data[data['Primary Fur Color'] == cinnamon_color]
cinnamon_count = len(cinnamon_data)
print(f'The number of cinnamon squirrels is {cinnamon_count}.')

black_data = data[data['Primary Fur Color'] == black_color]
black_count = len(black_data)
print(f'The number of black squirrels is {black_count}.')
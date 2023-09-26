#CSV is short for comma seperated values

# with open('weather_data.csv') as weather_file:
#     weather = weather_file.readlines()

# print(weather)

# import csv
# temperature = []

# with open('weather_data.csv') as weather_file:
#     data = csv.reader(weather_file)
#     print(data) #a reader object has been made
#     next(data) #skipps the first row
#     for row in data:
#         print(row)
#         temperature.append(int(row[1]))
#     print(temperature)


#Using Panda library
import pandas

data = pandas.read_csv('weather_data.csv')
print(data['temp'])
#Much easier using pandas!
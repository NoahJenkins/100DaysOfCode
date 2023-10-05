# #CSV is short for comma seperated values

# # with open('weather_data.csv') as weather_file:
# #     weather = weather_file.readlines()

# # print(weather)

# # import csv
# # temperature = []

# # with open('weather_data.csv') as weather_file:
# #     data = csv.reader(weather_file)
# #     print(data) #a reader object has been made
# #     next(data) #skipps the first row
# #     for row in data:
# #         print(row)
# #         temperature.append(int(row[1]))
# #     print(temperature)


# #Using Panda library
import pandas

# data = pandas.read_csv('weather_data.csv')
# # print(type(data)) #prints panda dataframe, object
# # print(data['temp'])
# # Much easier using pandas!
# #Each collum is a series, or like a vertical list

# #You can convert data frams to different files (such as SQL, XML, or even python dictionaries)
# # data_dict = data.to_dict()
# # print(data_dict)

# # temp_data = data['temp'].to_list()

# # print(temp_data)

# # #Calculate the Average
# # average = sum(temp_data) / len(temp_data)
# # print(average)

# #or

# # print((data['temp'].mean()))

# #Find Max of temp:

# # print((data["temp"].max()))

# #How How to get data drom the row.
# # print(data[data.day == 'Monday']) #Row is printed

# #Row of data where temp was max. 
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_f = (monday.temp * 1.8) + 32

# print(monday_f)

#Create a Data frame from scrath
data_dict = {
"students": ['Amy', "james,", 'Noah'],
"scores": [76, 56, 89]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv('new_data.csv')

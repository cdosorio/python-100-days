# with open("weather_data.csv") as file:
#     data = file.readlines()

# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

import pandas

#data = pandas.read_csv("weather_data.csv")
#print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

#temp_list = data["temp"].to_list()
#print(len(temp_list))

# get data of a serie (case sensitive)
# print(data["temp"].mean())
# print(data.temp.max())

# get row by filter
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# create a dataframe
# data_dict = {
#     "students" : ["Amy", "jame", "angela"],
#     "scores": [10,20,30]
# }
# data = pandas.DataFrame(data_dict)

# #dataframe to CSV
# data.to_csv("new_data.csv")

# group and count
data = pandas.read_csv("Squirrel_Data.csv")
df_colors = data.groupby(['Primary Fur Color']).size().reset_index(name='counts')
print(df_colors)
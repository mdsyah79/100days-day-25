
# with open("weather_data.csv") as file:
#     data = file.readlines()

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
#
# average_temp = data["temp"].mean()
# print(average_temp)
#
# max_temp = data.temp.max()
# print(max_temp)

# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp_F = monday.temp * 9/5 +32
# print(monday_temp_F)

# Create DF from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
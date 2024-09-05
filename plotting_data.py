# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: lab 11.13
# Date: 08 11 2023

#plotting_data.py
#imports
import matplotlib.pyplot as plt
import numpy as np
import math

with open("WeatherDataCLL.csv", "r") as w:
    days = w.readlines()
    #do this so it doesnt have \n at the end
    days = [days[x].replace('\n', "") for x in range(len(days))]
    #do this to make them all a list in a big list
    days = [days[x].split(",") for x in range(len(days))]
    #make sure it doesnt include the first words
    days = days[1:]

##line
#wind
y = []
#max
y2 = []
count = 0
counts = []
for i in days:
    if i[1] != "" and i[5] != "":
        count += 1
        counts.append(count)
        y.append(int(i[5]))
        y2.append(float(i[1]))


fig, ax1 = plt.subplots()
ax1.set_ylabel('Maximum Temperature, F')
ax1.plot(counts, y, label="Max Temp", color="RED")
ax2 = ax1.twinx()
ax2.set_ylabel("Average Wind Speed, mph")
ax2.set_xlabel('date')
ax2.plot(counts,y2, label="Avg Winds", color="BLUE")
fig.legend(loc="lower left", bbox_to_anchor=(0.13, 0.10))
fig.suptitle("Maximum Temperature and Average Wind Speed")

plt.tight_layout()
plt.show()

##histogram
xs = []
for i in days: 
    if i[1] != "":
        xs.append(float(i[1]))

plt.hist(xs, bins=29,color='green', edgecolor='black')
plt.xlabel('Average Wind Speed, mph')
plt.ylabel("Number of Days")
plt.title("Histogram of Average Wind Speed")
plt.tight_layout()
plt.show()

##scatter
x = []
y = []
for i in days:
    if i != "" and i[3] != "":
        x.append(float(i[3]))
        y.append(float(i[2]))
plt.scatter(x,y, color='black', s=22 )
plt.xlabel('Average Relative Humidity (%)')
plt.ylabel('Precipitation (in)')
plt.title('Percipitation vs Average Relative Humidity')
plt.tight_layout()
plt.show()

##bar chart
month = {1 : [], 2 : [], 3 : [], 4 : [], 5 : [], 6 : [], 7 : [], 8 : [],
           9: [], 10 : [], 11 : [], 12 : []}

for i in days:
    date = i[0]
    date = date.split("/")
    if i[4] != "":
        month[int(date[0])].append(int(i[4]))


months = [key for key in month]
values = []

def average(lst): 
    return sum(lst) / len(lst) 

for i in months:
    values.append(average(month[i]))

plt.bar(months, values, color='y')


#lines
#max
month = {1 : [], 2 : [], 3 : [], 4 : [], 5 : [], 6 : [], 7 : [], 8 : [],
           9: [], 10 : [], 11 : [], 12 : []}

for i in days:
    date = i[0]
    date = date.split("/")
    if i[5] != "":
        month[int(date[0])].append(int(i[5]))

valuesmax = []

for i in months:
    valuesmax.append(max(month[i]))

#min
month = {1 : [], 2 : [], 3 : [], 4 : [], 5 : [], 6 : [], 7 : [], 8 : [],
           9: [], 10 : [], 11 : [], 12 : []}

for i in days:
    date = i[0]
    date = date.split("/")
    if i[5] != "":
        month[int(date[0])].append(int(i[6]))

valuesmin = []

for i in months:
    valuesmin.append(min(month[i]))

plt.plot(months, valuesmax, label='High T', color='red')
plt.plot(months, valuesmin, label='Low T', color='blue')
plt.xlabel('Month')
plt.ylabel('Average Temperature, F')
plt.title('Temperature by Month')
plt.legend()
plt.tight_layout()
plt.show()

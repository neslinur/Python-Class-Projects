# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: lab 11.13
# Date: 08 11 2023


months = {"January" : 1, "February" : 2, "March" : 3, "April" : 4, "May" : 5, "June" : 6, 
          "July" : 7, "August" : 8, "September" : 9, "October" : 10, "November" : 11, "December" : 12}

with open("WeatherDataCLL.csv", "r") as w:
    days = w.readlines()
    #do this so it doesnt have \n at the end
    days = [days[x].replace('\n', "") for x in range(len(days))]
    #do this to make them all a list in a big list
    days = [days[x].split(",") for x in range(len(days))]
    #make sure it doesnt include the first words
    days = days[1:]


    max_list = []
    #now we have to go through each day and make a new list for all the max and then check which one is max from all of them
    for day in days:
        try:
            max_list.append(float(day[5]))
        except:
            pass
    
    maxi = max(max_list)

    #do the same for min
    min_list = []
    for day in days:
        try:
            min_list.append(float(day[6]))
        except:
            pass
    
    mini = min(min_list)

    #print max and min
    print(f"10-year maximum temperature: {maxi:.0f} F")
    print(f"10-year minimum temperature: {mini:.0f} F") 

    print("")
    #now we get the month and year
    fmonth = input("Please enter a month: ")
    #change into the value
    month = 0
    if fmonth in months:
        month = months[fmonth]

    year = input("Please enter a year: ")

    #check through the days and make a new list with the ones they want
    new_days = []
    for day in days:
        #split date of day
        split_day = day[0].split("/")
        if int(split_day[0]) == month and split_day[2] == year:
            new_days.append(day)

    print()
    print(f"For {fmonth} {year}:")
    #now we move on to average of daily temp
    #do what you did w max/min w average daily temp 
    daily_temps_list = []
    for day in new_days:
        try:
            daily_temps_list.append(float(day[4]))
        except:
            pass
    
    #calculate and print mean avg daily temp
    avg_daily_temps = sum(daily_temps_list)/len(daily_temps_list)
    print(f"Mean average daily temperature: {avg_daily_temps:.1f} F")

    #repeat with humidity

    humidity_list = []
    for day in new_days:
        try:
            humidity_list.append(float(day[3]))
        except:
            pass
    
    #calculate and print 
    avg_humidity = sum(humidity_list)/len(humidity_list)
    print(f"Mean relative humidity: {avg_humidity:.1f}%")

    #repeat with daily wind

    wind_list = []
    for day in new_days:
        try:
            wind_list.append(float(day[1]))
        except:
            pass
    
    #calculate and print
    avg_wind = sum(wind_list)/len(wind_list)
    print(f"Mean daily wind speed: {avg_wind:.2f} mph")

    #now we do perticipation
    rain = 0
    for day in new_days:
        if float(day[2]) > 0:
            rain += 1
    
    #calculate and print 
    avg_rain = rain/len(new_days) * 100
    print(f"Percentage of days with precipitation: {avg_rain:.1f}%")

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: 5.4 LAB
# Date: 18 09 2023
from math import *

#x = excess temperature
#y = surface heat flux

#x0 = x of start point
#y0 = y of start point
#x1 = x of second point
#y1 = y of second point

#m = slope between two points 

x = float(input("Enter the excess temperature: "))
y = 0

x0 = 0
y0 = 0
x1 = 0
y1 = 0

m = 0

#We check which area the x is in and go off of that
if x >= 1.3 and x <= 5:
    #If x >= 1.3 and x <= 5
    #Assign x0, x1, y0, y1 to points (1.3,1000) and (5,7000)
    #Find slope with these points
    #Find heat flux with the slope and these points and the input given
    #Print the statement
    x0 = 1.3
    y0 = 1000
    x1 = 5
    y1 = 7000
    m = log10(y1/y0)/log10(x1/x0)
    y = y0 * ((x/x0) ** m)
    print(f"The surface heat flux is approximately {y:.0f} W/m^2")
#We don’t include 5 in the next statement because we already included it in past if statement
elif x > 5 and x <= 30:
    x0 = 5
    y0 = 7000
    x1 = 30
    y1 = 1.5 * (10 ** 6)
    m = log10(y1/y0)/log10(x1/x0)
    y = y0 * ((x/x0) ** m)
    print(f"The surface heat flux is approximately {y:.0f} W/m^2")
elif x > 30 and x <= 120:
    x0 = 30
    y0 = 1.5 * (10 ** 6)
    x1 = 120
    y1 = 2.5 * (10 ** 4)
    m = log10(y1/y0)/log10(x1/x0)
    y = y0 * ((x/x0) ** m)
    print(f"The surface heat flux is approximately {y:.0f} W/m^2")
elif x > 120 and x <= 1200:
    x0 = 120
    y0 = 2.5 * (10 ** 4)
    x1 = 1200
    y1 = 1.5 * (10 ** 6)
    m = log10(y1/y0)/log10(x1/x0)
    y = y0 * ((x/x0) ** m)
    print(f"The surface heat flux is approximately {y:.0f} W/m^2")
#Make an elif statement at the end if x is less than 1.3 or greater than 1200 and say that surface flux is not available
elif x > 1200 or x < 1.3:
    print("Surface heat flux is not available")
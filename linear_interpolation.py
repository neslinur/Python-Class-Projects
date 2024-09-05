# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Neslinur Kaya
# Claudia Herrera
# Jasmine Gonzales
# Soley Mendoza
# Section: 403/503
# Assignment: 2.8 LAB
# Date: 28 08 2023
#
#

from math import *
#x will be time and y will be position 
x1 = 10
#adding 45 to 10 is 55
x2 = 55

y1 = 2027
y2 = 23027
# find equation for distance between 10 and 55 minutes
#find slope first = (y2 - y1)/(x2 - x1)
slope = (y2 - y1) / (x2 - x1)

#the equation will be: y = (slope)(x - x1) + y1
x = 25
distance = (slope) * (x - x1) + y1
print("Part 1:")
print("For t = 25 minutes, the position p =", distance, "kilometers")

# Part 2:
#find circumference since it orbits
circum = 2 * pi * 6745
x4 = 300
exterdistance = (slope) * (x4 - x1) + y1
#use modular division as it resets every time it hits houston in the orbit
exterdistance %= circum
print("Part 2:")
print("For t = 300 minutes, the position p =", exterdistance, "kilometers")
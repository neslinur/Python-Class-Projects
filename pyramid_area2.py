# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Neslinur Kaya, Soley Mendoza, Jasmine Gonzales, Neslinur Kaya
# Section: 503 403
# Assignment: 6.12
# Date: 25 09 2023

side = float(input('Enter the side length in meters: '))
layers = int(input('Enter the number of layers: '))

from math import *
triangle_area = ((3**0.5)/4) * ((side*layers)**2)
square_area = (side * side) * (sum(range(1,layers+1)) * 3)

#we use sum instead of loop
#for i in range(1, layers+1):
#  square_area += (side * side) * (i * 3)


area = square_area + triangle_area
print(f"You need {area:.2f} m^2 of gold foil to cover the pyramid")


# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Neslinur Kaya, Jasmine Gonzales, Soley Mendoza, Claudia Herrera
# Section: 403/503
# Assignment: 4.18
# Date: 08 09 2023
#

from math import *
t1= float(input("Enter time 1: "))
x1=float(input("Enter the x position of the object at time 1: "))
y1=float(input("Enter the y position of the object at time 1: "))
z1=float(input("Enter the z position of the object at time 1: "))

t2= float(input("Enter time 2: "))
x2= float(input("Enter the x position of the object at time 2: "))
y2= float(input("Enter the y position of the object at time 2: "))
z2= float(input("Enter the z position of the object at time 2: "))

#we are making functions for each so we don't have to repeat
def x_interpolation(time):
  result = ((x2 - x1)/(t2 - t1)) * (time - t1) + x1
  return result

def y_interpolation(time): 
  result = ((y2 - y1)/(t2 - t1)) * (time - t1) + y1
  return result

def z_interpolation(time):
  result = ((z2 - z1)/(t2 - t1)) * (time - t1) + z1
  return result

time_split = ((t2 - t1)/ 4)
tt = t1


print()
#1
print(f'At time {tt:.2f} seconds the object is at ({x_interpolation(tt):.3f},{y_interpolation(tt):.3f},{z_interpolation(tt):.3f})')

#1.25
tt += time_split
print(f'At time {tt:.2f} seconds the object is at ({x_interpolation(tt):.3f},{y_interpolation(tt):.3f},{z_interpolation(tt):.3f})')

#1.5
tt += time_split
print(f'At time {tt:.2f} seconds the object is at ({x_interpolation(tt):.3f},{y_interpolation(tt):.3f},{z_interpolation(tt):.3f})')

#1.75
tt += time_split
print(f'At time {tt:.2f} seconds the object is at ({x_interpolation(tt):.3f},{y_interpolation(tt):.3f},{z_interpolation(tt):.3f})') 

#2
tt += time_split
print(f'At time {tt:.2f} seconds the object is at ({x_interpolation(tt):.3f},{y_interpolation(tt):.3f},{z_interpolation(tt):.3f})')
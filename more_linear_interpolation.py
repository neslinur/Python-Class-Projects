# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: 2.10 LAB
# Date: 28 08 2023
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:07:51 2023

@author: l3tbt
"""

#these are used to plug into the formulas for the rest of the equations we need to solve
t1 = 12
x1 = 8
y1 = 6
z1 = 7

t2 = 85
x2 = -5
y2 = 30 
z2 = 9

#we will use these formulas to find the answers when we are given the time:
#x = ((x2 - x1)/(t2 - t1))(t - t1) + x1
#y = ((y2 - y1)/(t2 - t1))(t - t1) + y1
#z = ((z2 - z1)/(t2 - t1))(t - t1) + z1
time1 = 30.0
time1_x = ((x2 - x1)/(t2 - t1)) * (time1 - t1) + x1
time1_y = ((y2 - y1)/(t2 - t1)) * (time1 - t1) + y1
time1_z = ((z2 - z1)/(t2 - t1)) * (time1 - t1) + z1
print("At time", time1, "seconds:")
print("x1 =", time1_x, "m")
print("y1 =", time1_y, "m")
print("z1 =", time1_z, "m")

print("-----------------------")

#you divide 30 seconds by 4 to find out that you need 7.5 intervals to get 5 points
time2 = 37.5
time2_x = ((x2 - x1)/(t2 - t1)) * (time2 - t1) + x1
time2_y = ((y2 - y1)/(t2 - t1)) * (time2 - t1) + y1
time2_z = ((z2 - z1)/(t2 - t1)) * (time2 - t1) + z1
print("At time", time2, "seconds:")
print("x2 =", time2_x, "m")
print("y2 =", time2_y, "m")
print("z2 =", time2_z, "m")

print("-----------------------")

time3 = 45.0
time3_x = ((x2 - x1)/(t2 - t1)) * (time3 - t1) + x1
time3_y = ((y2 - y1)/(t2 - t1)) * (time3 - t1) + y1
time3_z = ((z2 - z1)/(t2 - t1)) * (time3 - t1) + z1
print("At time", time3, "seconds:")
print("x3 =", time3_x, "m")
print("y3 =", time3_y, "m")
print("z3 =", time3_z, "m")

print("-----------------------")

time4 = 52.5
time4_x = ((x2 - x1)/(t2 - t1)) * (time4 - t1) + x1
time4_y = ((y2 - y1)/(t2 - t1)) * (time4 - t1) + y1
time4_z = ((z2 - z1)/(t2 - t1)) * (time4 - t1) + z1
print("At time", time4, "seconds:")
print("x4 =", time4_x, "m")
print("y4 =", time4_y, "m")
print("z4 =", time4_z, "m")

print("-----------------------")

time5 = 60.0
time5_x = ((x2 - x1)/(t2 - t1)) * (time5 - t1) + x1
time5_y = ((y2 - y1)/(t2 - t1)) * (time5 - t1) + y1
time5_z = ((z2 - z1)/(t2 - t1)) * (time5 - t1) + z1
print("At time", time5, "seconds:")
print("x5 =", time5_x, "m")
print("y5 =", time5_y, "m")
print("z5 =", time5_z, "m")




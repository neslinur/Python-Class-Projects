# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: 2.11 LAB
# Date: 21 08 2023
# -*- coding: utf-8 -*-

#x = 1
#y = 10
#z = 0
#x = y
#x += 1
#y += x
#y *= x
#z += x
#z += y
#print(z)

#I have to manipulate the given equations to get the required answers:
#1, 27, 102, 1000000000000, 8675

#1
z = 0
x = 1
y = 10
z += x
print(z)

#27
z = 0
x = 1
y = 10
x += 1
y *= x
x += 1
x += 1
x += 1
x += 1
x += 1
y += x
z += y
print(z)

#102
y = 10
x = y
z = 0
y *= x
x = 1
x += 1
y += x
z += y
print(z)

#1000000000000
y = 10
x = 1
z = 0
#keep using x and y to make more 0s
x = y
y *= x
x = y
y *= x
x = y
y *= x
y *= x
z += y
print(z)

#8675
y = 10
x = 1
z = 0
#make y thousand
x = y
y *= x
y *= x
#make x 8
x = 1
x += 1
x += 1
x += 1
x += 1
x += 1
x += 1
x += 1
#make y 8000
y *= x
#make z y
z += y
#make y 100
y = 10
x = y
y *= x
#make x 6
x = 1
x += 1
x += 1
x += 1
x += 1
x += 1
#make y 600
y *= x
#add y to z
z += y
#make y 70
y = 10
x = 1
x += 1
x += 1
x += 1
x += 1
x += 1
x += 1
y *= x
z += y
#make x 5
x = 1
x += 1
x += 1
x += 1
x += 1
z += x
print(z)
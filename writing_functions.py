# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: 3.18 LAB
# Date: 30 08 2023
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 14:53:41 2023

@author: l3tbt
"""

from math import *

#area of equilateral triangle
#area of square
#area of regular pentagon
#area of regular dodecagon (12)



#creating functions with side parameter
def area_triangle(side):
    area = (sqrt(3)/4) * pow(side,2)
    return area

def area_square(side):
    area = side * side
    return area

def area_pent(side):
    area = (1/4) * sqrt(5 * (5 + (2 * sqrt(5)))) * pow(side,2)
    return area

def area_dod(side):
    area = 3 * pow(side,2) * (2 + sqrt(3))
    return area

side = float(input("Please enter the side length: "))
print(f"A triangle with side {side:.2f} has area {area_triangle(side):.3f}")
print(f"A square with side {side:.2f} has area {area_square(side):.3f}")
print(f"A pentagon with side {side:.2f} has area {area_pent(side):.3f}")
print(f"A dodecagon with side {side:.2f} has area {area_dod(side):.3f}")
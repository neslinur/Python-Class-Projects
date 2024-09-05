# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: 1.13 LAB
# Date: 21 08 2023
from math import *
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 14:04:07 2023

@author: l3tbt
"""

print("This shows the evaluation of sin(x-1)/(x-1) evaluated close to x=1")
print("My guess is 1")
#we add a 0 to the x between the 1s
print(sin(1.1-1)/(1.1-1))
print(sin(1.01-1)/(1.01-1))
print(sin(1.001-1)/(1.001-1))
print(sin(1.0001-1)/(1.0001-1))
print(sin(1.00001-1)/(1.00001-1))
print(sin(1.000001-1)/(1.000001-1))
print(sin(1.0000001-1)/(1.0000001-1))
print(sin(1.00000001-1)/(1.00000001-1))
#it ends with a 1.0
print("")
print("My guess was good")

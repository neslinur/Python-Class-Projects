# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: 4.19 LAB
# Date: 10 09 2023
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 14:32:23 2023

@author: l3tbt
"""
from math import *

A = float(input("Please enter the coefficient A: "))
B = float(input("Please enter the coefficient B: "))
C = float(input("Please enter the coefficient C: "))

#(-b +- sqrt(b^2 - 4ac))/2a

if A == 0 and B == 0 and C != 0:
    print('You entered an invalid combination of coefficients!')
#could be two real roots or two idential or two complex
elif A != 0:
    if ((B ** 2) - (4 * A * C)) < 0:
        if (-abs(B) % (2 * A)) == 0 and (sqrt(abs((B ** 2) - (4 * A * C)))) % (2 * A) == 0:
            lex1 = -abs(B) / (2 * A)
            lex2 = (sqrt(abs((B ** 2) - 4 * A * C)) / (2 * A))
            root1 = f'{lex1} + {lex2}i'
            root2 = f'{lex1} - {lex2}i'
            print(f'The roots are x = {root1} and x = {root2}')
    else:
        root1 = (-abs(B) + sqrt((B ** 2) - (4 * A * C)))/2*A
        root2 = (-abs(B) - sqrt((B ** 2) - (4 * A * C)))/2*A
        if root1 > root2:
            print(f'The roots are x = {root1} and x = {root2}')
        elif root2 > root1:
            print(f'The roots are x = {root2} and x = {root1}')
        elif root2 == root1:
            print(f'The root is x = {root1}')
#could be one root
elif A == 0 and B != 0 and C != 0:
    if C > 0:
        root1 = -abs(C)/B
    elif C < 0:
        root1 = abs(C)/B
    print(f"The root is x = {root1}")
    
    
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: 4.18 LAB
# Date: 10 09 2023
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 13:48:08 2023

@author: l3tbt
"""
#10 gadgets a day
#after 10 days (starting at 11 days), one more gadget per day
#day 50 it reaches full speed (starts producing same amount everyday)
#day 101 it stops producing completely

day = float(input("Please enter a positive value for day: "))

#lets make sure this number is valid
if day < 0:
    print("You entered an invalid number!")
else:
    if day < 11:
        gadgets = day * 10
    elif day >= 11 and day <= 50:
        gadgets = 100
        gadgets += ((11 + day) * (day - 10))/2
    elif day > 50 and day <= 100:
        gadgets = 100
        gadgets += ((11 + 50) * (50 - 10))/2
        gadgets += (day - 50) * 50
    elif day >= 101:
        gadgets = 100
        gadgets += ((11 + 50) * (50 - 10))/2
        gadgets += (100 - 50) * 50

print(f"The sum total number of gadgets produced on day {day:.0f} is {gadgets:.0f}")
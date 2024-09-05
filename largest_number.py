# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: 4.16 LAB
# Date: 08 09 2023# -*- coding: utf-8 -*-

first = float(input("Enter number 1: "))
second = float(input("Enter number 2: "))
third = float(input("Enter number 3: "))
#im creating a largest variable to keep track of it
largest = first

#this makes sure that even if its equal it will print largest
if second > largest:
    largest = second
if third > largest:
    largest = third
    
print(f"The largest number is {largest}")
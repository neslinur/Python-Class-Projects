# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: 3.17 LAB
# Date: 30 08 2023
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 14:00:37 2023

@author: l3tbt
"""
from math import *

print("This program calculates the applied force given mass and acceleration")
#all inputs are string so we have to convert it
mass = float(input("Please enter the mass (kg): "))
acc = float(input("Please enter the acceleration (m/s^2): "))
force = mass * acc
print(f"Force is {force:.1f} N")

#We need to be specific to the reqirements so we add a line between
print("")

print("This program calculates the wavelength given distance and angle")
dist = float(input("Please enter the distance (nm): "))
angle = float(input("Please enter the angle (degrees): "))
angleradians = angle * pi / 180
wave = 2 * (dist * sin(angleradians))
#we make sure it only shows 4 decimal points
print(f"Wavelength is {wave:.4f} nm")

print("")

#im going to start using code from my using variables
print("This program calculates how much Radon-222 is left given time and initial amount")
days = float(input("Please enter the time (days): "))
initial_g = float(input("Please enter the initial amount (g): "))
half_days = 3.8 
radon = initial_g * (2 ** (-days/half_days))
print(f"Radon-222 left is {radon:.2f} g")

print("")

print("This program calculates the pressure given moles, volume, and temperature")
moles = float(input("Please enter the number of moles: "))
volume = float(input("Please enter the volume (m^3): "))
temperature_k = float(input("Please enter the temperature (K): "))
gas_constant = 8.314
pressure = ((moles * temperature_k * gas_constant)/volume)/1000
print(f"Pressure is {pressure:.0f} kPa")


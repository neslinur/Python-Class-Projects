# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: 1.12 LAB
# Date: 21 08 2023
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 14:03:58 2023

@author: l3tbt
"""
from math import *

#Calculate force applied with mass 27 kg
#and acceleration 1.5 m/s^2 (F=ma)
print("Force is", (27 * 1.5), "N")

#Calculate the wavelength of x-rays w distance of 0.025 nm, 
#scattering angle of 35 degrees, and first order diffraction 
#convert degree to radian to make it easier
angleradians = 35 * pi / 180
print("Wavelength is",(2 * (0.025 * sin(angleradians))), "nm")

#Calculate how much Radon-222 is left after 5 days of radioactive decay
#initial amount of 27 g and a half-life of 3.8 days
#27 * 2 ** -5/3.8
print("Radon-222 left is", 27 * (2 ** (-5/3.8)),"g")

#Calculate the pressure of 5 moles of an ideal gas 
#with a volume of 0.27 m^3, and temperature of 415 K
#Use a value of 8.314 m^3Pa/K·mol for the gas constant
#We use the formula and after getting the answer in pascals, we convert
#it into kilopascals to get the desired answer
print("Pressure is",((5 * 415 * 8.314)/0.27)/1000, "kPa")

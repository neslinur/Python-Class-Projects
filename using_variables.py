# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: 2.9 LAB
# Date: 21 08 2023
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 14:03:58 2023

@author: l3tbt
"""
from math import *

#Calculate force applied with mass 27 kg
#and acceleration 1.5 m/s^2 (F=ma)
mass_kg = 27
acceleration = 1.5
print("Force is", (mass_kg * acceleration), "N")

#Calculate the wavelength of x-rays w distance of 0.025 nm, 
#scattering angle of 35 degrees, and first order diffraction 
#convert degree to radian to make it easier
diffraction = 1
dist_nm = 0.025
angle_degrees = 35
angle_radians = angle_degrees * pi / 180
print("Wavelength is",(2 * (dist_nm * sin(angle_radians)))/diffraction, "nm")

#Calculate how much Radon-222 is left after 5 days of radioactive decay
#initial amount of 27 g and a half-life of 3.8 days
#27 * 2 ** -5/3.8
days = 5
initial_g = 27
half_days = 3.8 
print("Radon-222 left is", initial_g * (2 ** (-days/half_days)),"g")

#Calculate the pressure of 5 moles of an ideal gas 
#with a volume of 0.27 m^3, and temperature of 415 K
#Use a value of 8.314 m^3Pa/K·mol for the gas constant
#We use the formula and after getting the answer in pascals, we convert
#it into kilopascals to get the desired answer
moles = 5
volume = 0.27
gas_constant = 8.314
temperature_k = 415
print("Pressure is",((moles * temperature_k * gas_constant)/volume)/1000, "kPa")

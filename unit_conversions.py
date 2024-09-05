# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Neslinur Kaya
# Claudia Herrera
# Jasmine Gonzales
# Soley Mendoza
# Section: 503/403
# Assignment: 3.15 LAB
# Date: 06 09 2023

from math import *

#Please enter the quantity to be converted: 867.5309
#867.53 pounds force is equivalent to 3858.97 Newtons
#867.53 meters is equivalent to 2846.23 feet
#867.53 atmospheres is equivalent to 87902.57 kilopascals
#867.53 watts is equivalent to 2960.14 BTU per hour
#867.53 liters per second is equivalent to 13750.65 US gallons per minute
#867.53 degrees Celsius is equivalent to 1593.56 degrees Fahrenheit

#Pounds (force) to Newtons (Claudia)
#Meters to feet- jasmine
#Atmospheres to kilopascals (kPa) - Neslinur
#Watts to BTU per hour - Neslinur
#Liters per second to US gallons per minute (Claudia)
#Degrees Celsius to degrees Fahrenheit - (soley)

quant = float(input("Please enter the quantity to be converted: "))

#claudia
def pounds_to_force(quant):
  newtons= quant * 4.44822
  return newtons
print(f"{quant:.2f} pounds force is equivalent to {pounds_to_force(quant):.2f} Newtons")

#jasmine
def met_to_feet(quant):
  feet = quant * 3.2808399
  return feet
print(f"{quant:.2f} meters is equivalent to {met_to_feet(quant):.2f} feet")

#nesli
def atmo_to_kpa(quant):
  kpa = quant * 101.325
  return kpa
print(f"{quant:.2f} atmospheres is equivalent to {atmo_to_kpa(quant):.2f} kilopascals")

def watt_to_btu(quant):
  btu = quant * 3.4121416331
  return btu
print(f"{quant:.2f} watts is equivalent to {watt_to_btu(quant):.2f} BTU per hour")

#claudia
def lit_to_gall(quant):
  gall= quant * 15.850323141489
  return gall
print(f"{quant:.2f} liters per second is equivalent to {lit_to_gall(quant):.2f} US gallons per minute")

#soley
def cel_to_fah(quant):
  Fahrenheit = quant * 1.8 + 32
  return Fahrenheit
print(f"{quant:.2f} degrees Celsius is equivalent to {cel_to_fah(quant):.2f} degrees Fahrenheit")

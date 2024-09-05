# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Neslinur Kaya, 
# Jasmine Gonzales,
# Claudia Herrera 
# Section: 403/503
# Assignment: 12 Lab
# Date: 11 14 2023

# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

import numpy as np
import matplotlib as plt

#3x4
A = np.arange(12).reshape(3, 4)
print(f"A = {A}")
print("")

#4x2
B = np.arange(8).reshape(4, 2)
print(f"B = {B}")
print("")

#2x3
C = np.arange(6).reshape(2, 3)
print(f"C = {C}")
print("")

#did matrix multiplication
D= np.dot(A,B).dot(C)

print(f"D = {D}")
print("")

DT = np.transpose(D)

print(f"D^T = {DT}")
print("")

E= (np.sqrt(D))/2
print(f"E = {E}")
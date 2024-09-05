# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Neslinur Kaya, Jasmine Gonzales, Claudia Herrera, Soley Mendoza
# Section: 403/503
# Assignment: 4.15 Lab
# Date: 11 09 2023

############ Part A ############

a = input("Enter True or False for a: ")
if a == 'T' or a == 't' or a == 'True':
  a = True
elif a == 'F' or a == 'f' or a == 'False':
  a = False
  
b = input("Enter True or False for b: ")
if b == 'T' or b == 't' or b == 'True':
  b = True
elif b == 'F' or b == 'f' or b == 'False':
  b = False

c = input("Enter True or False for c: ")
if c == 'T' or c == 't' or c == 'True':
  c = True
elif c == 'F' or c == 'f' or c == 'False':
  c = False

############ Part B ############

#a and b and c
adbdc = a and b and c
#a or b or c
arbrc = a or b or c

############ Part C ############
xor = (a or b) and (not(a and b) or (not a and not b))
odd = (a and b and c) or (a and not b and not c) or (b and not a and not c) or (c and not a and not b)

print(f"a and b and c: {adbdc}")
print(f"a or b or c: {arbrc}")
print(f"XOR: {xor}")
print(f"Odd number: {odd}")

############ Part D ############


complex1 = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
complex2 = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))


simple1 = not b or (not a and b and not c)
simple2 = a or not b and c
print(f"Complex 1: {complex1}")
print(f"Complex 2: {complex2}")
print(f"Simple 1: {simple1}")
print(f"Simple 2: {simple2}")

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Neslinur Kaya, Jasmine Gonzales, Soley Mendoza, Claudia Herrera
# Section: 403/503
# Assignment: 4.14
# Date: 08 09 2023

#dont print 0 and for 1 dont print coefficient
from math import *
quadratic = ""

CoeA= float(input("Please enter the coefficient A: "))
CoeB= float(input("Please enter the coefficient B: "))
CoeC= float(input("Please enter the coefficient C: "))

quadratic = ''

#coefficient a 
if CoeA != 0:
  if CoeA < 0:
    quadratic += '- '
  if abs(CoeA) == 1:
    quadratic += 'x^2 '
  if abs(CoeA) != 1:
    quadratic += f'{abs(CoeA):.0f}x^2 '
  if CoeB > 0 and CoeB != 0:
    quadratic += '+ '

#coefficient b
if CoeB != 0:
  if CoeB < 0:
    quadratic += '- '
  if abs(CoeB) == 1:
    quadratic += 'x '
  if abs(CoeB) != 1:
    quadratic += f'{abs(CoeB):.0f}x '
  if CoeC > 0 and CoeC != 0:
    quadratic += '+ '

#coefficient c
if CoeC != 0:
  if CoeC < 0:
    quadratic += f'- {abs(CoeC):.0f} '
  if CoeC > 0:
    quadratic += f'{abs(CoeC):.0f} '

print(f'The quadratic equation is {quadratic}= 0')
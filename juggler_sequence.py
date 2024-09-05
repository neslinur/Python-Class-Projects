# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: 6.14 LAB-
# Date: 22 09 2023
from math import *

n = int(input("Enter a positive integer: "))
iter = 0

#put this at the beginning so it doesn't repeatedly print
print(f"The Juggler sequence starting at {n} is: ")
while n != 1:
    print(f'{n}', end=', ')
    if n % 2 == 0:
        n = floor(sqrt(n))
    else:
        n = floor(pow(n, 3/2))
    iter += 1
        
#I put this at the end to include 1
print(n)

if iter != 1:
    print(f"It took {iter} iterations to reach 1")
else:
    print(f"It took {iter} iteration to reach 1") 

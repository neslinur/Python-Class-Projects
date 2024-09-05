# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Neslinur Kaya, Jasmine Gonzales, Soley Mendoza, Claudia Herrera
# Section: 503/403
# Assignment: Lab 10.13
# Date:  01 11 2023

from time import time
import math 
#The function should take in as a parameter a positive integer and #return a list of four (4) numbers that when squared add up to the #positive integer of interest. 

def list_nums(num):
  a = 0
  #checks that the squared of each number leading up to number doesnt go past it
  while (a**2 <= num):
    b = a
    while (b**2 <= num):
      c = b
      while (c**2 <= num):
        d = c
        while (d**2 <= num):
          #goes through them all and makes sure they equal the number
          if ((a**2)+(b**2)+(c**2)+(d**2) == num):
            return [a,b,c,d]
          d += 1
        c += 1
      b += 1
    a += 1

def count_sets(num):
  #same code but instead of returning we just count it and keep going
  count = 0
  a = 0
  while (a**2 <= num):
    b = a
    while (b**2 <= num):
      c = b
      while (c**2 <= num):
        d = c
        while (d**2 <= num):
          if ((a**2)+(b**2)+(c**2)+(d**2) == num):
            #add to count instead of returning
            count += 1
          d += 1
        c += 1
      b += 1
    a += 1
  return count



# how to measure how long your function takes to run:
#t1 = time() # get start time
#print(list_nums(9)) # run function
#t2 = time() # get end time
#print(f"This took {t2-t1} seconds") # print result
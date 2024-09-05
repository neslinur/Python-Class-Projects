# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: 9.16 lab
# Date: 27 10 2023
from math import *

#####PARTA#####
def parta(sphere_r, hole_r):
    return ((4/3) * pi * (((sphere_r ** 2) - (hole_r ** 2)) ** (3/2)))
   
#####PARTB#####
def partb(n):
    oddlist = []
    newlist = []
    for i in range(1, n, 2):
        oddlist.append(i)
    for i in range(len(oddlist)):
        for j in range(len(oddlist)):
            if sum(oddlist[i:j+1]) == n:
                newlist.append(oddlist[i:j+1])

     
    if newlist == []:
        return False
    else:
        newlist = newlist[0]  
    return newlist 

  
    
#####PART C#####

def partc(char,name,comp,email):
   lengths = [len(name),len(comp),len(email)]
   longest = max(lengths) +6
   all = [name,comp,email]
   
   #im just using multiplication to make it easier for me
   result = char * longest
   
   for element in all:
       result += '\n' + char 
       result += ((longest - len(element)) // 2 - 1) * " "
       result += element
       
       if longest % 2 == 0 and len(element) % 2 != 0:
           result += ((longest - len(element)) // 2) * " " 
       else:
           result += ((longest - len(element)) // 2 - 1) * " " 
       result += char
   
   result += '\n' + char * longest
   return result


#####PART D#####
def partd(nums):
    minim = min(nums)
    maxim = max(nums)
    med = 0
    nums = sorted(nums)
    length = len(nums)
    index = (length - 1) // 2
   
    if (length % 2):
        med = nums[index]
    else:
        med = (nums[index] + nums[index + 1])/2.0   
    return minim, med, maxim

#####PARTE#####

def parte(times,distances):
    velocity = []
    for i in range(len(times)-1):
        speed = (distances[i+1]-distances[i])/(times[i+1]-times[i])
        velocity.append(speed)
    return velocity



#####PARTF#####
def partf(nums):
    result = -1
    for i in range(len(nums)):
        for num in nums[:i]:
            if num + nums[i] == 2027:
                result = num*nums[i]
                break
        for num in nums[i+1:]:
            if num + nums[i] == 2027:
                result = num*nums[i]
                break
    if result < 0:
        result = False
    return result

#print(partf([1,2,3,4,27,7,8]))
                
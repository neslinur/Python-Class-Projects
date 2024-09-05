# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: 6.14 LAB
# Date: 21 09 2023



#we make it a function so we can use it
def doublefactorial(ans):
    sum = 1
    for i in range(ans, 0, -2):
        sum *= i
    return sum

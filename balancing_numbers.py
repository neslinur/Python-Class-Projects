# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: 6.14 LAB
# Date: 22 09 2023

n = int(input("Enter a value for n: "))
sum_1 = 0
sum_2 = 0
iter = 0

for i in range(n):
    sum_1 += i
    
#im creating a hold variable so it doesn't mess up the initial input
hold = n
while sum_2 < sum_1:
    if sum_1 != sum_2:
        hold += 1
        sum_2 += hold
        iter += 1
    
if sum_1 == sum_2:
    print(f'{n} is a balancing number with r={iter}')
else:
    print(f'{n} is not a balancing number')

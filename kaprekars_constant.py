# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: 7.25 LAB
# Date: 02 10 2023

#if word starts w consonant, move consonant to end and add 'ay'
#if word starts w vowel, add 'yay' (y also counts as a vowel)

num = input("Enter a four-digit integer: ")
nums = list(map(int, num))
#there is a lot of changing from list to ints
#also use sort to sort them from descending and ascending order
iter = 0
s = str(num)
for a in range(8):
    i = len(nums)
    while i < 4:
        nums[0:0] += [0]
        i+= 1
    first = sorted(nums, reverse=True)
    first = int("".join(map(str, first)))
    second = sorted(nums)
    second = int("".join(map(str, second)))
    sum = first - second
    nums = list(map(int, str(sum)))
    iter += 1
    s += f' > {sum}'
    if sum == 6174:
        break 
else:
    s = f'{num} > 0'
    iter = 1
    
print(s)
print(f"{num} reaches {sum} via Kaprekar's routine in {iter} iterations")


    

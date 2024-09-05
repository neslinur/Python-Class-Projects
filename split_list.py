# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: 7.26 LAB
# Date: 30 09 2023
nums = input("Enter numbers: ")
nums_list = nums.split()
nums_list = list(map(int,nums_list))
sum = 0
sum2 = 0

for i in range(len(nums_list)):
    #add up numbers to the left of i
    #add up numbers to the right of i
    sum = 0
    sum2 = 0
    for num in nums_list[:i]:
        sum += num
    for num in nums_list[i:]:
        sum2 += num
    if sum == sum2:
        left = nums_list[:i]
        right = nums_list[i:]
        print(f'Left: {left}')
        print(f'Right: {right}')
        print(f"Both sum to {sum}") 
        break
else:
    print("Cannot split evenly")

import numpy as np
import matplotlib.pyplot as plt
# x = np.linspace(-2, 2, 25)
# y1 = x
# y2 = x ** 2
# plt.plot(x, y1, 'g', linewidth = 3)
# plt.plot(x, y2, 'k', marker = 'o', markerfacecolor = 'b')
# plt.axis([-2, 2, -2, 4])
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Plots for 2 polynomials')
# plt.legend(['straight', 'curved'], loc = 'lower left')
# plt.show()

# #40)
# #writing a function
# def Armstrong_number(a, b):
#   result = []
#   for i in range(a, b + 1):
#     split_num = list(str(i))
#     sum = 0
#     for j in split_num:
#       sum += int(j) ** len(split_num)
#     if sum == i:
#       result.append(i)
#   return result

# n = input("Enter an integer: ")

# while True:
  
#     while True:
#         try:
#             n = int(n)
#             break
#         except:
#             n = input("Bad input! Try again: ")

#     if n < 0:
#       n = input("Need a positive number: ")
#     else:
#       break

# n2 = input("Enter another integer: ")

# while True:
  
#     while True:
#         try:
#             n2 = int(n2)
#             break
#         except:
#             n2 = input("Bad input! Try again: ")

#     if n2 < 0:
#       n2 = input("Need a positive number: ")
#     else:
#       break

# print(f"Armstrong numbers: {Armstrong_number(n , n2)}")

# #41)
# def perfectnumber(a):
#    sum = 0
#    for i in range(1, a):
#       if a % i == 0:
#         sum += i
#    if sum == a:
#       return True
#    return False
   
# n = input("Enter an integer: ")

# while True:
#    while True:
#       try:
#          n = int(n)
#          break
#       except:
#          n = input("Bad input! Try again: ")
    
#    if n < 0:
#         n = input("Need a positive integer: ")
#    else:
#         break

# if perfectnumber(n):
#    print(f"{n} is a perfect number")
# else:
#    print(f"{n} is not a perfect number")

# #42)
# with open("item_cost.dat", 'r') as c:
#     everything = c.readlines()

# maxcost = 0
# maxname = ''
# for i in range(1, len(everything)): # skip header line
#     line = everything[i].split(',') # split on commas
#     if float(line[1]) > maxcost: # compare current value to max
#         maxcost = float(line[1]) # update max if current value is bigger
#         maxname = line[0] # don't forget to grab the name
# print(f'The most expensive item is {maxname} and costs ${maxcost:.2f}')

# #43)
# with open("grades.txt", "w") as g:
#     grades = g.write("Name\tScore\n")
#     leng = int(input("Enter the number of students: "))
#     avg = []
#     for i in range(leng):
#         grade = input("Enter the next name and score: ")
#         grade = grade.split(" ")
#         avg.append(float(grade[1]))
#         grades = g.write(f"{grade[0]}\t{float(grade[1])}\n")

# avg = sum(avg) / len(avg)
# print(f"The average grade for this quiz is {avg}")

def change(a):
    a = 2
    print(a, end="")

a = 6
change(a)
print(a,end="")


    
    
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: 12.14 LAB
# Date: 13 11 2023
import numpy as np
import matplotlib.pyplot as plt

#start with a 2d point

point = np.array([[1],
                  [0]])
#make matrix
matrix = np.array([[1.02, 0.095],
                   [-0.095, 1.02]])

x = [point[0][0]]
y = [point[1][0]]



for i in range(250):
    #assign point each time
    point = np.dot(matrix, point)
    x.append(point[0][0])
    y.append(point[1][0])

#points
plt.scatter(x,y)
#names
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Spiral")
#show
plt.show()



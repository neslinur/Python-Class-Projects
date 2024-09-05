# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Neslinur Kaya, 
# Jasmine Gonzales,
# Claudia Herrera 
# Section: 403/503
# Assignment: 12 Lab
# Date: 11 15 2023

# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material


import numpy as np
import matplotlib.pyplot as plt

######PART 1#######
#parabola

#domain
x = np.linspace(-2.0, 2.0, 100)

#plug in f values to equation 
y1 = (1 / (4 * 2)) * x**2  
y2 = (1 / (4 * 6)) * x**2  

#size of axises
plt.figure(figsize=(10, 6))

plt.plot(x, y1, label='f=2', color='red', linewidth=2.0)#change line wdith
plt.plot(x, y2, label='f=6', color='blue', linewidth=6.0)

plt.title('Parabola plots with varying focal lengths')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


######PART 2#####
#cubic polynomial

#domain
x = np.linspace(-4.0, 4.0, 25)
y_cubic = 2 * x**3 + 3 * x**2 - 11 * x - 6 #equation

plt.figure(figsize=(8, 5))

plt.scatter(x, y_cubic, label='Cubic Polynomial', color='yellow', marker="*", s=100, edgecolors="black", linewidths=1)

plt.title('Plot of cubic polynomial')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()


######PART 3######
#sin/cos using subplots

#domain
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(12, 4))

#cos plot
ax1.plot(x, y_cos, label='cos(x)', color='maroon')
ax1.set_xlabel('x')
ax1.set_ylabel('y=cos(x)')
ax1.legend()
ax1.grid(True)

#sinplot
ax2.plot(x, y_sin, label='sin(x)', color='grey')
ax2.set_ylabel('y=sin(x)')
ax2.legend()
ax2.grid(True)



fig.suptitle('Plot of cos(x) and sin(x)')
plt.tight_layout()
plt.show()

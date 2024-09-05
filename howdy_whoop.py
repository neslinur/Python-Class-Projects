# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: 6.13 LAB
# Date: 21 09 2023



first = int(input("Enter an integer: "))
sec = int(input("Enter another integer: "))

for i in range(1,101):
    #we do this first so it doesn't run the others before this one
    if i % first == 0 and i % sec == 0:
        print("Howdy Whoop")
    elif i % first == 0:
        print("Howdy")
    elif i % sec == 0:
        print("Whoop")
    else:
        print(i)


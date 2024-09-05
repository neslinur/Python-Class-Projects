# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: 7.26 LAB
# Date: 30 09 2023

words = input("Enter some text: ")
word_list = words.split()

con = {
       "a" : "4",
       "e" : "3",
       "o" : "0",
       "s" : "5",
       "t" : "7"
       }

new_str = ""
for word in word_list:
    for char in word:
        if char in "aeost":
            new_str += con[char]
        else:
            new_str += char
    new_str += " "

#a > 4, e > 3, o > 0, s > 5, t > 7
         
print(f'In leet speak, "{words}" is: {new_str}')
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: 7.25 LAB
# Date: 30 09 2023

#if word starts w consonant, move consonant to end and add 'ay'
#if word starts w vowel, add 'yay' (y also counts as a vowel)

words = input("Enter word(s) to convert to Pig Latin: ")

word_list = words.split()

#don't assign the object directly or it will change them both, assign the range
hold_list = word_list[:]

for i in range(len(hold_list)):
    if hold_list[i][0] in 'yaeiou':
        hold_list[i] += 'yay'
    elif hold_list[i][1] not in 'yaeiou' and hold_list[i][2] in 'yaeiou':
        hold_list[i] = hold_list[i][2:] + hold_list[i][0:2] + 'ay'
    else:
        hold_list[i] = hold_list[i][1:] + hold_list[i][0] + 'ay'
        
s = ''

for word in hold_list:
    s += word + " "
print(f'In Pig Latin, "{words}" is: {s}')
            

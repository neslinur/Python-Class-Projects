# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Neslinur Kaya
# Jasmine Gonzales
# Soley Mendoza
# Claudia Herrera
# Section: 403/503
# Assignment: Lab 8
# Date: 18 10 2023

#If 12 determine am/pm
if type == "12":
  if int(time[:-3]) < 12 or int(time[:-3]) == 24: 
  #add to string
    time += "AM"
  elif int(time[:-3]) >= 12:
    time += "PM"
    
#If not permitted, try again
if character not in 'abcdeghkmnopqrsuvwxyz@$&*=':
  loop = True
  while loop:
    character = input("Character not permitted! Try again: ")
    if character in 'abcdeghkmnopqrsuvwxyz@$&*=':
      loop = False
      
#Loop 
#Loop through value and change to character
output = ''

for l in range(5):
  output += '\n'
  for a in range(len(time)):
    if time[a] in convert:
      for i in convert[time[a]][l]:
        if i not in " PAM:" and character != "":
          output += character
        else:
          output += i
    if a != len(time)-1:
      output += " "


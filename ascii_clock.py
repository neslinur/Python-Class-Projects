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

#######ASCII Clock#######

#Get input

#Get time
time = input("Enter the time: ")

#Get clock type
type = input("Choose the clock type (12 or 24): ")

#If 24 no am/pm
#If 12 determine am/pm
if type == "12":
  if int(time[:-3]) < 12 or int(time[:-3]) == 24: 
  #add to string
    time += "AM"
  elif int(time[:-3]) >= 12:
    time += "PM"
#If type is 12 and time is past 12, convert to standard time 
if type == '12' and int(time[:-5]) > 12:
  time = str(int(time[:-5]) - 12) + time[-5:]
elif type == '12' and int(time[:-5]) == 0:
  time = '12' + time[-5:]
#make into list
time = list(time)

#Get character 
character = input("Enter your preferred character: ")
#If not permitted, try again
if character not in 'abcdeghkmnopqrsuvwxyz@$&*=':
  loop = True
  while loop:
    character = input("Character not permitted! Try again: ")
    if character in 'abcdeghkmnopqrsuvwxyz@$&*=':
      loop = False
#######Process data######

#Dictionary 
#Create dict for each num and letter (key), make list convert to drawing (value)
convert = {'0' : [['0','0','0'],
                  ['0',' ','0'],
                  ['0',' ','0'],
                  ['0',' ','0'],
                  ['0','0','0']],
           '1' : [[' ','1',' '],
                  ['1','1',' '],
                  [' ','1',' '],
                  [' ','1',' '],
                  ['1','1','1']],
           '2' : [['2','2','2'],
                  [' ',' ','2'],
                  ['2','2','2'],
                  ['2',' ',' '],
                  ['2','2','2']],
           '3' : [['3','3','3'],
                  [' ',' ','3'],
                  ['3','3','3'],
                  [' ',' ','3'],
                  ['3','3','3']],
           '4' : [['4',' ','4'],
                  ['4',' ','4'],
                  ['4','4','4'],
                  [' ',' ','4'],
                  [' ',' ','4']],
           '5' : [['5','5','5'],
                  ['5',' ',' '],
                  ['5','5','5'],
                  [' ',' ','5'],
                  ['5','5','5']],
           '6' : [['6','6','6'],
                  ['6',' ',' '],
                  ['6','6','6'],
                  ['6',' ','6'],
                  ['6','6','6']],
           '7' : [['7','7','7'],
                  [' ',' ','7'],
                  [' ',' ','7'],
                  [' ',' ','7'],
                  [' ',' ','7']],
           '8' : [['8','8','8'],
                  ['8',' ','8'],
                  ['8','8','8'],
                  ['8',' ','8'],
                  ['8','8','8']],
           '9' : [['9','9','9'],
                  ['9',' ','9'],
                  ['9','9','9'],
                  [' ',' ','9'],
                  ['9','9','9']],
           ':' : [[' '],
                  [':'],
                  [' '],    
                  [':'],
                  [' ']],
           'A' : [[' ','A',' '],
                  ['A',' ','A'],
                  ['A','A','A'],
                  ['A',' ','A'],
                  ['A',' ','A']],
           'M' : [['M',' ',' ',' ','M',],
                  ['M','M',' ','M','M',],
                  ['M',' ','M',' ','M'],
                  ['M',' ',' ',' ','M'],
                  ['M',' ',' ',' ','M']],
           'P' : [['P','P','P',],
                  ['P',' ','P',],
                  ['P','P','P',],
                  ['P',' ',' ',],
                  ['P',' ',' ']],
}
  
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

#Combine together for result
print(output)
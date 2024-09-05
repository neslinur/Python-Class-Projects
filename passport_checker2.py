# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Neslinur Kaya
# Jasmine Gonzales
# Claudia Herrera
# Soley Mendoza
# Section: 403/503
# Assignment: Team Lab 11 
# Date: 06 11 2023
#

# ask for file name
file_name = input("Enter the name of the file: ")
#"scanned_passports.txt"

def v(diction: dict):
  if not 1920 <= int(diction['byr']) <= 2007:
      return False
  if not 2013 <= int(diction['iyr']) <= 2023:
      return False
  if not 2023 <= int(diction['eyr']) <= 2033: 
      return False
  if diction['hgt'] != -1 and diction['hgt'][-2:] == 'in':
      if not 59 <= int(diction['hgt'][:-2]) <= 76:
          return False
  elif diction['hgt'] != -1 and diction['hgt'][-2:] == 'cm':
      if not 150 <= int(diction['hgt'][:-2]) <= 193:
          return False
  else:
      return False
  if diction['hcl'] != -1 and diction['hcl'][0] == '#':
      for i in diction['hcl'][1:]:
          if not i in '0123456789abcdef':
              return False
  else: 
      return False
  if diction['pid'] != -1 and len(diction['pid']) != 9 or not 0 <= int(diction['pid']) <= 999999999:
      return False
  if not 100 <= int(diction['cid']) <= 999:
      return False
  return True

#open file as reading and make that assigned to "f" and with so you dont have to close it later
with open(file_name, 'r') as f: 
  #put the whole thing in lines first so we can split it based on the big space between passports instead of splitting it into just regular lines 
  lines = f.read()
  #here we split them into specific passports because the seperation is two new lines
  lines = lines.split("\n\n")
  #now we create a new file for the valid passports which we will write inside with only the valid passports
  valid = open("valid_passports2.txt", "w")
  #this count is for the amount of valid passports to later print it
  count = 0
  #start by going through each passport in the list of lines
  for port in lines:
    #we replace the \n inside the passports with space so they can be only what we need
    passport = port.replace("\n", " ")
    #we need to split the individual passport into a list too so we can get the starting three letters and chek them
    splitpassport = passport.split(' ')
    #this counter is for counting the amount of specifications a passport has and we reset it everytime it completes a passport
    dict = {'byr':-1, 'iyr':-1, 'eyr':-1, 'hgt':-1, 'hcl':-1, 'pid':-1, 'cid':-1}
    
    #we go through the specific passport
    for i in splitpassport:
      dict[i.split(':')[0]] = i.split(':')[1]
    if v(dict):
      #if it does qualify, we add 1 to the valid passport counter
      count+=1
      #we also write to the new text file we created
      valid.write(port + '\n')
      valid.write("\n")

#dont forget to close the valid text file since we didnt use "with"
valid.close()
#print it
print(f"There are {count} valid passports")

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
# Write a program named passport_checker.py that takes as input from the user a filename (like scanned_passports.txt), reads the file, counts the number of valid passports, then writes the valid passport scans to a new file named valid_passports.txt. Format your program’s output using the
# example shown below. Format your new file using the same format as the input file; write the data for each passport exactly as shown in the input file with one blank line between valid passports


# ask for file name
file_name = input("Enter the name of the file: ")
#"scanned_passports.txt"

#open file as reading and make that assigned to "f" and with so you dont have to close it later
with open(file_name, 'r') as f: 
  #put the whole thing in lines first so we can split it based on the big space between passports instead of splitting it into just regular lines 
  lines = f.read()
  #here we split them into specific passports because the seperation is two new lines
  lines = lines.split("\n\n")
  #now we create a new file for the valid passports which we will write inside with only the valid passports
  valid = open("valid_passports.txt", "w")
  #this count is for the amount of valid passports to later print it
  count = 0
  #start by going through each passport in the list of lines
  for port in lines:
    #we replace the \n inside the passports with space so they can be only what we need
    passport = port.replace("\n", " ")
    #we need to split the individual passport into a list too so we can get the starting three letters and chek them
    splitpassport = passport.split(' ')
    #this counter is for counting the amount of specifications a passport has and we reset it everytime it completes a passport
    counter = 0
    # we go through the specific passport
    for i in splitpassport:
      #we check if the three letters in the beginning equal any of the specifications except eye color because that doesnt matter
      if i[:3] == 'byr' or i[:3] == 'iyr' or i[:3] == 'eyr' or i[:3] == "hgt" or i[:3] == "hcl" or i[:3] == "pid" or i[:3] == 'cid':
        #when it does equal one of these, we add it to the specifications counter
        counter+=1
    #the minimum you need of these is 7 so we check if the amount qualifies
    if counter >= 7:
      #if it does qualify, we add 1 to the valid passport counter
      count+=1
      #we also write to the new text file we created
      valid.write(port + '\n')
      valid.write("\n")

#dont forget to close the valid text file since we didnt use "with"
valid.close()
#print it
print(f"There are {count} valid passports")

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: lab 11.12
# Date: 08 11 2023

paint = input("Enter the filename: ")
character = input("Enter a character: ")

txt_name = paint[:-3] + "txt"
painting = open(txt_name, "w")
with open(paint, "r") as p:
    #separate into lines
    paint_lines = p.readlines()

    #get rid of the \n
    paint_lines = [paint_lines[x].replace('\n', "") for x in range(len(paint_lines))]

    #go through each line
    for line in paint_lines:
        #for each line split it with the commas
        split_line = line.split(",")
        #go through the split one
        for i in range(len(split_line)):
            #check for the position and add to text based on the position
            if i % 2 == 0:
                painting.write(" " * int(split_line[i]))
            else:
                painting.write(character * int(split_line[i]))
        painting.write("\n")
    
    
painting.close
print(f"{txt_name} created!")
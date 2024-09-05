# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: lab 11.11
# Date: 07 11 2023

file_name = input("Enter the name of the file: ")


with open(file_name, "r") as f:
    barcodes = f.readlines()
    for b in range(len(barcodes)):
        if barcodes[b][-1:] == '\n':
            barcodes[b] = barcodes[b][:-1]
    count = 0
    v = open("valid_barcodes.txt","w")
    for barcode in barcodes:

  

        #take barcode and make into list
        barcode = list(map(int,barcode))

        #split first 12 into two groups
        first = []
        second = []
        for f in range(0,len(barcode)-1,2):
            first.append(barcode[f])
        for f in range(1,len(barcode)-1,2):
            second.append(barcode[f])

        #take sum of first and second (mult by 3) and add them
        first_sum = sum(first)
        second_sum = sum(second) * 3
        s = first_sum + second_sum


        #subtract last digit from 10
        ldigit = 10 - int(str(s)[-1])

        #compare with last digit of barcode
        if ldigit == barcode[-1]:
            count += 1
            word = "".join("".join(map(str,barcode)))
            v.write(word)
            v.write('\n')

v.close()
print(f"There are {count} valid barcodes")

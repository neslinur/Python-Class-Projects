# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Neslinur Kaya, Jasmine Gonzales, Soley Mendoza, Claudia Herrera
# Section: 403/503
# Assignment: 4.13
# Date: 08 09 2023

#input will be how much paid and how much cost
#output change and list how many of each type of coin
#change is always less than $1

#Example output (using inputs 1, 0.73):
#How much did you pay? 1
#How much did it cost? 0.73
#You received $0.27 in change. That is...
#1 quarter
#2 pennies

paid = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))
diff = paid - cost

quarter = 0
dime = 0
nickel = 0
penny = 0


print(f"You received ${diff:.2f} in change. That is...")
#quarter -> dime -> nickel -> penny
diff = round(diff,2)

if diff >= .25:
  quarter = int(diff / .25)
  diff -=  .25* quarter
  diff = round(diff, 2)

if diff >= .10:
  dime = int(diff/ .10)
  diff -= dime * .10
  diff = round(diff, 2)

if diff >= .05:
  nickel = int(diff/ .05)
  diff -= nickel * .05
  diff = round(diff, 2)


if diff >= .01:
  penny = int(diff/ .01)
  diff -= penny * .01
  diff = round(diff, 2)

if quarter == 1:
  print(f'{quarter} quarter')
elif quarter > 1:
  print(f'{quarter} quarters')

if dime == 1:
  print(f'{dime} dime')
elif dime > 1:
  print(f'{dime} dimes')

if nickel == 1:
  print(f'{nickel} nickel')
elif nickel > 1:
  print(f'{nickel} nickels')

if penny == 1:
  print(f'{penny} penny')
elif penny > 1:
  print(f'{penny} pennies')

  
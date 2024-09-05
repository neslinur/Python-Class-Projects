# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Neslinur Kaya
# Claudia Herrera
# Jasmine Gonzales
# Soley Mendoza
# Section: 403/503
# Assignment: Lab 7 Team
# Date: 04 10 2023
#

#lets get  down to business 
import time

print("Please use the positions on the top and right to determine where you would like to move with the row(right) first and the column(top) second.")
#this makes it print one at a time
time.sleep(1)
print("This is our board:")
#first we're supposed to make sure we can make our board readable and display the positions to the viewer
time.sleep(1)
print('1 2 3 4 5 6 7 8 9')
print('. . . . . . . . . 1')
print('. . . . . . . . . 2')
print('. . . . . . . . . 3')
print('. . . . . . . . . 4')
print('. . . . . . . . . 5')
print('. . . . . . . . . 6')
print('. . . . . . . . . 7')
print('. . . . . . . . . 8')
print('. . . . . . . . . 9')

time.sleep(1)
print("Black moves first and then alternate")

time.sleep(1)
move = ""
count = 0
#this is the actual board that we make moves on
board =  [ 
['.', '.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],
['.', '.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],
['.', '.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],
['.', '.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],
['.', '.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],
['.', '.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],
['.', '.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],
['.', '.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],
['.', '.' , '.' , '.' , '.' , '.' , '.' , '.' , '.'],
]
  
#we're making the code with loops and with if statements
while move != 'stop':
  #this will display the board before every move
  for i in board:
    for j in i:
      print(j, end=" ")
    print()
  #this will ask them where they want to move, taking in a two digit number
  move = input("Where would you like to move? ")
  #we use break because otherwise it will run the list(map(int, ans)) with the input stop and that causes an error
  if move == 'stop':
    break
  #if the move is not a number
  if move.isdigit() == False:
    print("You entered an invalid entry, try again")
    continue
  ans = list(move)
  ans = list(map(int, ans))
  #if the move is off the board
  if len(ans) > 2 or ans[0] < 1 or ans[1] < 1:
    print("Your move is off the board, try again")
    continue
    #we do subtract one because our positions dont align with the index
  elif board[ans[0]-1][ans[1]-1] == '.':
    if count % 2 == 0:
      board[ans[0]-1][ans[1]-1] = '●'
    else:
      board[ans[0]-1][ans[1]-1] = 'o'
  #we do else incase the position isnt empty
  else:
    print("There is already a stone in this position, try another one")
    continue
  #we add a count because we are using this to do modulus and determine which stone it is in play
  count += 1
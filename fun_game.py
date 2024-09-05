# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Neslinur Kaya, Jasmine Gonzales, Claudia Herrera
# Section: 403/503
# Assignment: Lab 13
# Date: 01 12 2023
#
#
#

import turtle
import time
import numpy as np
import sys
turtle.setworldcoordinates(-300, -300, 300, 300)

#####TEEKO#####

#Board
board = np.array([["", "", "", "", ""],
                  ["", "", "", "", ""],
                  ["", "", "", "", ""],
                  ["", "", "", "", ""],
                  ["", "", "", "", ""]])

def rows_cols():
  # Set up the turtle
  my_turtle = turtle.Turtle()
  my_turtle.speed(0)  # Fastest drawing speed
  # Display x and y values on the sides
  r = 0
  c = 0
  for i in range(-300, 301, 150):
      my_turtle.penup()
      my_turtle.goto(i, 360)
      my_turtle.pendown()
      my_turtle.write(str(c), align="center", font=("Arial", 8, "normal"))
      c += 1

  for i in range(300, -301, -150):
      my_turtle.penup()
      my_turtle.goto(-360, i)
      my_turtle.pendown()
      my_turtle.write(str(r), align="center", font=("Arial", 8, "normal"))
      r += 1
  my_turtle.hideturtle()
rows_cols()

# Draw the outer square
def outer_square():
  my_turtle = turtle.Turtle()
  my_turtle.speed(0) 
  my_turtle.pensize(3)
  my_turtle.penup()
  my_turtle.goto(-300, 300)
  for i in range(4):
    my_turtle.pendown()
    my_turtle.forward(600)
    my_turtle.right(90)
  my_turtle.hideturtle()

# # Draw the inside
def inner_squares():
  my_turtle = turtle.Turtle()
  my_turtle.speed(0)  
  my_turtle.pensize(3)

  for y in range(-300, 301, 150):
    my_turtle.penup()
    my_turtle.goto(-300, y)
    my_turtle.pendown()
    my_turtle.forward(600)
  my_turtle.left(90)
  for x in range(-300, 301, 150):
    my_turtle.penup()
    my_turtle.goto(x, -300)
    my_turtle.pendown()
    my_turtle.forward(600)
  my_turtle.hideturtle

  for i in range(-300, 301, 150):
    my_turtle.penup()
    my_turtle.goto(-300,i)
    my_turtle.pendown()
    my_turtle.goto(i,-300)
    my_turtle.penup()
    my_turtle.goto(i,300)
    my_turtle.pendown()
    my_turtle.goto(300,i)
  for i in range(300, -301, -150):
    my_turtle.penup()
    my_turtle.goto(300,-i)
    my_turtle.pendown()
    my_turtle.goto(i,-300)
    my_turtle.penup()
    my_turtle.goto(-300,i)
    my_turtle.pendown()
    my_turtle.goto(-i,300)
  my_turtle.hideturtle()

def circles():
    my_turtle = turtle.Turtle()
    my_turtle.speed(0)  # Set the drawing speed (1 is slowest, 10 is fastest)

    for x in range(-300,301, 150):
        for y in range(-300,301,150):
            my_turtle.penup()
            my_turtle.goto(x,y-50)
            my_turtle.pendown()
            my_turtle.color("black", "white")  
            my_turtle.begin_fill()
            my_turtle.circle(50)
            my_turtle.end_fill()



    my_turtle.hideturtle()

def points(a,b,p):
   r = {0 : 300, 1 : 150, 2: 0, 3 : -150, 4 : -300}
   c = {0 : -300, 1 : -150, 2: 0, 3 : 150, 4 : 300}
   my_turtle = turtle.Turtle()
   my_turtle.speed(0)

   my_turtle.penup()
   my_turtle.goto(c[b], r[a]-50)
   my_turtle.pendown()
   my_turtle.color("black", p)  
   my_turtle.begin_fill()
   my_turtle.circle(50)
   my_turtle.end_fill()
   my_turtle.hideturtle()

def empty(a,b):
   r = {0 : 300, 1 : 150, 2: 0, 3 : -150, 4 : -300}
   c = {0 : -300, 1 : -150, 2: 0, 3 : 150, 4 : 300}
   my_turtle = turtle.Turtle()
   my_turtle.speed(0)

   my_turtle.penup()
   my_turtle.goto(c[b], r[a]-50)
   my_turtle.pendown()
   my_turtle.color("black", "white")  
   my_turtle.begin_fill()
   my_turtle.circle(50)
   my_turtle.end_fill()
   my_turtle.hideturtle()
outer_square()    
inner_squares()
circles()



#Rules

#Instructions
def instructions():
    print("Welcome to Teeko.")
    print("")
    time.sleep(1.5)
    print("Black moves first. Move piece to any spot on the board. Red moves next to any unoccupied spot. ")
    print("")
    time.sleep(1.5)
    print("The object of the game is for either player to win by having all four of their markers in a straight line or on a square of four adjacent spaces. (Adjacency is horizontal, vertical, or diagonal, but does not wrap around the edges of the board.) ")
    print("")
    time.sleep(1.5)
    print("You have 4 pieces each. After all 8 pieces are on the board, you can move a piece to an empty adjacent spot until there is a winner or you choose to quit. ")
    print("")
    time.sleep(1.5)
    print("To quit early, type 'q' at any time.")
    time.sleep(1.5)
    print("If you want to see the instructions again, type 'i' at any time.")
    time.sleep(1.5)
instructions()


#Moves

#function to ask for position from each player and then check if valid 
def get_input(player):
  '''To get the position the players want to go if valid
  parameters: player = the player that is going to make a move
  returns: row and column of position'''
  print("")
  row = input(f"Player {player}, choose row 0 to 4: ")
  if row == "q":
    sys.exit()
  if row == "i":
    instructions()
    get_input(player)
  time.sleep(1.5)
  while True:
    try: 
        row = int(row)
        break
    except:
        if row == "q":
            sys.exit()
        if row == "i":
            instructions()
            get_input(player)
        row = input("That's not a valid number! Try again! ")
  time.sleep(1.5)
  column = input(f"Player {player}, choose column 0 to 4: ")
  if column == "q":
    sys.exit()
  if column == "i":
    instructions()
    get_input(player)
  while True:
    try: 
        column = int(column)
        break
    except:
        if column == "q":
            sys.exit()
        column = input("That's not a valid number. Try again! ")
  time.sleep(1.5)
  if 0 <= row <= 4 and 0 <= column <= 4:
    if board[row][column] == "": 
      return row, column
    else:
      print("That space is already taken. Try again! ")
      time.sleep(1.5)
      get_input(player)
  else:
      print("Not within the range given. Try Again! ")
      time.sleep(1.5)
      get_input(player)

def moving(player):
  '''To get the position the players want to change if valid
  parameters: player = the player that is going to make a change
  returns: row and column of changing piece'''  
  my_dict = {"Black" : "B", "Red" : "R"}
  print("")
  row = input(f"Player {player}, choose the row in which the piece you'd like to move is in: ")
  if row == "q":
    sys.exit()
  if row == "i":
    instructions()
    moving(player)
  time.sleep(1.5)
  while True:
    try: 
        row = int(row)
        break
    except:
        if row == "q":
            sys.exit()
        if row == "i":
            instructions()
            moving(player)
        row = input("That's not a valid number! Try again! ")
  time.sleep(1.5)
  column = input(f"Player {player}, choose the column in which the piece you'd like to move is in: ")
  if column == "q":
    sys.exit()
  if column == "i":
    instructions()
    moving(player)
  while True:
    try: 
        column = int(column)
        break
    except:
        if column == "q":
            sys.exit()
        if column == "i":
            instructions()
            moving(player)
        column = input("That's not a valid number. Try again! ")
  time.sleep(1.5)
  row = int(row)
  column = int(column)
  if 0 <= row <= 4 and 0 <= column <= 4:
    if board[row][column] == my_dict[player]: 
      return row, column
    else:
      print("That is not your piece. Try again! ")
      time.sleep(1.5)
      moving(player)
  else:
      print("Not within the range given. Try Again! ")
      time.sleep(1.5)
      moving(player)

#Check for 4 in a row (vert/hori/diag/square)
def win(player):
    '''To check if anyone has won based on diagnols/square/horizontal/vertical
    parameters: player = the player that is going to make a move
    returns: True or False if there is a winner or not'''
    my_dict = {"Black" : "B", "Red" : "R"}
    piece = my_dict[player]
    # Check horizontal locations for win
    for r in range(5):
        if (board[r,0] == piece and board[r,1] == piece and board[r,2] == piece and board[r,3] == piece) or (board[r,1] == piece and board[r,2] == piece and board[r,3] == piece and board[r,4] == piece):
                return True

    # Check vertical locations for win
    for c in range(5):
        if (board[0,c] == piece and board[1,c] == piece and board[2,c] == piece and board[3,c] == piece) or (board[1,c] == piece and board[2,c] == piece and board[3,c] == piece and board[4,c] == piece):
                return True

    # Check positively sloped diaganols
    for r in range(2):
        for c in range(2):
            if board[r,c] == piece and board[r+1,c+1] == piece and board[r+2,c+2] == piece and board[r+3,c+3] == piece:
                return True
    if board[1,1] == piece and board[2,2] == piece and board[3, 3] == piece and board[4,4] == piece:
       return True

    # Check negatively sloped diaganols
    for r in range(2):
        for c in range(3, 5):
            if board[r][c] == piece and board[r+1][c-1] == piece and board[r+2][c-2] == piece and board[r+3][c-3] == piece:
                return True
    if board[1,3] == piece and board[2,2] == piece and board[3, 1] == piece and board[4,0] == piece:
       return True

    #Check square
    for r in range(4):
       for c in range(4):
        if board[r,c] == piece and board[r,c+1] == piece and board[r+1,c] == piece and board[r+1,c+1] == piece:
           return True

#applying them

bmoves = 0
rmoves = 0
moves = 0
notwon = True

my_file = open("TeekoKeepTrack.txt", "w")
my_file.write("Lets keep track of our intense game!\n")
while notwon:

    if bmoves >= 4 and rmoves >= 4:
       if moves % 2 == 0:
            rowm , colm = moving("Black")
            empty(rowm, colm)
            board[rowm, colm] = ""
            row, column = get_input("Black")
            board[row, column] = "B"
            my_file.write(f"Black moved their piece at {rowm}, {colm} to {row}, {column}!\n")
            points(row, column, "black")
            bmoves += 1
            moves += 1
            print(board)
            if win("Black"):
                print("Black won!")
                my_file.write("Black won!\n")
                sys.exit()

       else:
            rowm , colm = moving("Red")
            empty(rowm, colm)
            board[rowm, colm] = ""
            row, column = get_input("Red")
            board[row, column] = "R"
            my_file.write(f"Red moved their piece at {rowm}, {colm} to {row}, {column}!\n")
            points(row, column, "red")
            rmoves += 1
            moves += 1
            if win("Red"):
                print("Red won!")
                sys.exit()
    else:
        if moves % 2 == 0:
            row , column = get_input("Black")
            board[row, column] = "B"
            my_file.write(f"Black put a piece down at {row}, {column}!\n")
            points(row, column, "black")
            bmoves += 1
            moves += 1
            if win("Black"):
                print("Black won!")
                sys.exit()


        else:
            row , column = get_input("Red")
            board[row, column] = "R"
            my_file.write(f"Red put a piece down at {row}, {column}!\n")
            points(row, column, "red")
            rmoves += 1
            moves += 1
            if win("Red"):
                print("Red won!")
                sys.exit()

# end it
my_file.close()
turtle.mainloop()
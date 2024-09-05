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

# #need a grid

# def draw_grid():
#   # Set up the turtle
#   my_turtle = turtle.Turtle()
#   my_turtle.speed(0)  # Fastest drawing speed
#   # Draw horizontal grid lines
#   for y in range(-300, 301, 50):
#       my_turtle.penup()
#       my_turtle.goto(-300, y)
#       my_turtle.pendown()
#       my_turtle.forward(600)

#   # Draw vertical grid lines
#   my_turtle.left(90)
#   for x in range(-300, 301, 50):
#       my_turtle.penup()
#       my_turtle.goto(x, -300)
#       my_turtle.pendown()
#       my_turtle.forward(600)

#   # Display x and y values on the sides
#   for i in range(-300, 301, 50):
#       my_turtle.penup()
#       my_turtle.goto(i, -320)
#       my_turtle.pendown()
#       my_turtle.write(str(i), align="center", font=("Arial", 8, "normal"))

#       my_turtle.penup()
#       my_turtle.goto(-320, i)
#       my_turtle.pendown()
#       my_turtle.write(str(i), align="center", font=("Arial", 8, "normal"))
#     # Hide the turtle
#   my_turtle.hideturtle()
# draw_grid()

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
    print(i)
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
   c = {0 : -300, 1 : -150, 2: 0, 3 : 150, 4 : 200}
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

outer_square()    
inner_squares()
circles()



#Rules

#Instructions
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
  time.sleep(1.5)
  try: 
    row = int(row)
  except:
    row = input("That's not a valid number!")
  time.sleep(1.5)
  column = input(f"Player {player}, choose column 0 to 4: ")
  if column == "q":
    sys.exit()
  try: 
    column = int(column)
  except:
    column = input("That's not a valid number! ")
  time.sleep(1.5)
  row = int(row)
  column = int(column)
  if 0 <= row <= 4 and 0 <= column <= 4:
    if board[row][column] == "": 
      return row, column
    else:
      print("That space is already taken. Try again! ")
      time.sleep(1.5)
      return get_input(player)
  else:
      print("Not within the range given. Try Again! ")
      time.sleep(1.5)
      return get_input(player)
      


#applying them

bmoves = 0
rmoves = 0
moves = 0
while bmoves != 4 and rmoves != 4:
  if moves % 2 == 0:
    row , column = get_input("Black")
    board[row, column] = "B"
    points(row, column, "black")
    bmoves += 1
    moves += 1
    print(board)
  else:
    row , column = get_input("Red")
    board[row, column] = "R"
    points(row, column, "red")
    rmoves += 1
    moves += 1
    print(board)


print(moves)
print(rmoves)
print(bmoves)
#Check for 4 in a row (vert/hori/diag/square)






#to do this ill make a function that will check after every move


# Keep the window open
turtle.mainloop()
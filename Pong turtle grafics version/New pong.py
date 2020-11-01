from turtle import Turtle,Screen
from time import sleep
from random import randint

# Screen setup
window = Screen() # Creating the Screen object where turtle are drawn on
window.setup(900,620) # Initialising window's size
window.bgcolor("black") # Stting black as the background color
window.title("THE PONG GAME 1vs1") # Renaming window 

# Borders setup
border = Turtle() # Creating the turtle to draw the boarders

border.speed(0) # Turtle initialisation
border.hideturtle()
border.color("white")

border.penup() # Drawing of the main square
border.pensize(10)
border.goto(-400,300)
border.pendown()
for l in range(2):
    border.forward(800)
    border.right(90)
    border.forward(600)
    border.right(90)

border.penup() # Drawing of the middle line
border.goto(0,300)
border.pendown()
border.goto(0,-300)

# Score pen
sc_pen = Turtle() # Turtle initialisation
sc_pen.speed(0)
sc_pen.hideturtle()
sc_pen.color("red")
sc_pen.penup()

sc_pen.goto(0,250) # Setting the possition where it will write the score
sc_pen.pendown()

# Score Setup
pl1_score = 0
pl2_score = 0
sc_pen.write("Player 2: 0     Player 1:  0",align="center",font=("carrier",30,"normal")) # Writes the score in the screen which start at 0-0

# Player1 object
player1 = Turtle() # Turtle initialisation
player1.speed(0)
player1.shape("square")
player1.shapesize(1,5)
player1.penup()
player1.color("white")
player1.right(90)
player1.goto(350,0)


# Player2 object
player2 = Turtle() # Turtle initialisation
player2.speed(0)
player2.shape("square")
player2.shapesize(1,5)
player2.penup()
player2.color("white")
player2.right(90)
player2.goto(-350,0)

# Ball
ball=Turtle() # Turtle initialisation
ball.speed(0)
ball.penup()
ball.shape("circle")
ball.color("blue")
ball.shapesize(1.2,1.2)

# Movement Functions
def forward1(): 
    ''' Player1 moves upwards '''
    if player1.ycor() + 30 < + 220: # Doesn't letting the player to go out of the borders
        player1.forward(-30)

def back1():
    ''' Player1 moves downwards '''
    if player1.ycor() - 30 > -220: # Doesn't letting the player to go out of the borders
        player1.forward(30)

def forward2():
    ''' Player2 moves upwards '''
    if player2.ycor() + 30 < + 220: # Doesn't letting the player to go out of the borders
        player2.forward(-30)
def back2():
    ''' Player2 moves downwards '''
    if player2.ycor() - 30 > - 220: # Doesn't letting the player to go out of the borders
        player2.forward(30)

#This set of functionts help for the change of direction and keep it random but logical 
def left_to_right():
    a=randint(3,8)
    return a
def right_to_left():
    a=randint(-8,-3)
    return a
def up_to_down():
    a=randint(-8,-3)
    return a
def down_to_up():
    a=randint(3,8)
    return a
    
# Ball direction start
dirx = 3
diry = 3

while True:
    #Players movement
    window.update()
    window.listen()
    window.onkey(forward2,"w") # Calls the forward2 when w is pressed
    window.onkey(back2,"s") # Calls the back2 when s is pressed
    window.onkey(forward1,"Up") # Calls the forward1 when up arrow is pressed
    window.onkey(back1,"Down") # Calls the back1 when down arrow is pressed

    ball.goto(ball.xcor()+dirx,ball.ycor()+diry) # Ball movement it adds the dirx and diry to its current possition

    #Borders-Ball colision
    if ball.ycor() > 270 or ball.ycor() < -270:
        diry = left_to_right() if diry < 0 else right_to_left()
    #Players-ball colision
    if ball.distance(player1) < 60 or ball.distance(player2) < 60:
        dirx = down_to_up() if dirx < 0 else up_to_down()

    #Score
    if ball.xcor()<-370: # Adds a goal to the player1 and resets the game for the next point
        ball.goto(0,0)
        pl1_score += 1
        sc_pen.clear() # Update the score in the screen 
        sc_pen.write("Player 2: {}     Player 1:  {}".format(pl2_score,pl1_score),align="center",font=("carrier",30,"normal"))
        sleep(0.5) # small delay
        if pl1_score == 7: # Checks if that goal made the player win
            sc_pen.penup()
            sc_pen.goto(200,0)
            sc_pen.pendown()
            sc_pen.write("Winner",align="center",font=("carrier",30,"normal"))
            sc_pen.penup()
            sc_pen.goto(-200,0)
            sc_pen.pendown()
            sc_pen.write("Loser",align="center",font=("carrier",30,"normal"))
            ball.hideturtle()
            sleep(2)
            break # Ends the game

    if ball.xcor()>370: # Adds a goal to the player2 and resets the game for the next point
        ball.goto(0,0)
        pl2_score+=1
        sc_pen.clear() # Update the score in the screen
        sc_pen.write("Player 2: {}     Player 1:  {}".format(pl2_score,pl1_score),align="center",font=("carrier",30,"normal"))    
        sleep(0.5)
        if pl2_score==7: # Checks if that goal made the player win
            sc_pen.penup()
            sc_pen.goto(200,0)
            sc_pen.pendown()
            sc_pen.write("Loser",align="center",font=("carrier",30,"normal"))
            sc_pen.penup()
            sc_pen.goto(-200,0)
            sc_pen.pendown()
            sc_pen.write("Winner",align="center",font=("carrier",30,"normal"))
            ball.hideturtle()
            sleep(2)
            break # Ends the game

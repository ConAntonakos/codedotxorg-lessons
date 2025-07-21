import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.colormode(255)
screen.bgcolor("black")

# Ball variables
ball_size = 10.0
ball_speed = 5

# Paddle variables
paddle_speed = 30
paddle_width = 60.0
paddle_thickness = paddle_width / 10.0

# Boundary variables
box_size = 400.0
boundary = box_size / 2.0

#Drawing the box
box_drawer = turtle.Turtle()
box_drawer.penup()
box_drawer.speed(0)
box_drawer.goto(-box_size / 2.0, -box_size / 2.0)
box_drawer.pendown()
box_drawer.color("red")
for i in range(4):
	box_drawer.forward(box_size)
	box_drawer.left(90)
box_drawer.ht()

################################################################
############################ Paddle ############################
################################################################

#Making the paddle
paddle = turtle.Turtle()
paddle.color("aquamarine")
paddle.shape("square")
paddle.shapesize(paddle_thickness/20.0, paddle_width / 20.0)

'''
TODO: Paddle starting position
5m

Move the paddle so that it starts at the coordinates (0, -boundary + 20)
'''



'''
TODO: Move paddle with arrow keys
5m

1) If the user presses the right arrow key, the paddle moves to the right
by paddle_speed but only if the right edge of the paddle is less than boundary.

2) If the user presses the left arrow key, the paddle moves to the left
by paddle_speed but only if the left edge of the paddle is within the boundary.

Hint: paddle.xcor() will give you the x coordinate of the middle of the paddle.
How can you use this value and paddle_width to get the x coordinates of the 
left and right edges of the paddle?

When you create a Turtle shape, its position (.xcor(), .ycor()) is always the center point of the shape, not the left or right edge.
So when you check if your paddle is about to move off screen, you have to calculate:

Where is the left edge?
Where is the right edge?

Because paddle_width is the whole width, and you need only half of it to reach the left or right edge from the middle.
'''


################################################################
############################ Bricks ############################
################################################################

# Brick variables
num_bricks = 10
gap_size = 10.0
brick_width = (box_size - (num_bricks + 1)*gap_size) / num_bricks
brick_thickness = brick_width / 2.0

'''
TODO: Write make_brick_row function
5-10m

Write the function called make_brick_row that takes in a color and y coordinate.
This function will create one row of bricks, save each brick in a list and
return the list of bricks.

  - Use num_bricks for the number of bricks per row.
  - The color is a string that will tell you the color that you should make that 
	row of bricks.
  - The y coordinate will be the y coordinate of all the bricks in this row.
  - When you make your turtle bricks, you can change the speed of 
  	the brick turtle to 0 so that the bricks are drawn more quickly.
  - Use shape to make each brick a square and use shapesize to change 
  	the size of each brick to (brick_thickness/20.0, brick_width/20.0)

Hint: The x coordinate of the first brick should be 
-box_size/2.0 + gap_size + brick_width/2.0. 
From there, the x coordinate of the second brick will be the 
x coordinate of the previous brick plus brick_width plus gap_size

1.Takes in a color (string) and a y coordinate (number).
2.Makes num_bricks Turtle squares in that color, all at the same y.
3.Spreads them left to right with equal gaps.
4.Returns a list of those Turtle brick objects so you can manage them later (collision, hide, check win).

-box_size/2 → puts you at the far left edge of the play area.
+ gap_size → small margin so brick isnt stuck to wall.
+ brick_width/2 → because .xcor() is center of brick, so we shift by half the width to line up left edge cleanly.
.shape("square") → base shape.
.shapesize() → stretches that square to a rectangle.
.penup() → don’t draw lines when moving the brick.
.goto(xBrick, y) → places the brick at the right x & the same y for the row.

Shifts the x for the next brick.
Why add width + gap? So each brick sits next to the last brick, with a gap in between.
'''
def make_brick_row(color, y):
	row = []
	return row


y_brick = (box_size / 2.0) - gap_size - (brick_thickness / 2.0)
row1 = make_brick_row("red", y_brick)
row2 = make_brick_row("green", y_brick - ((brick_thickness) + gap_size))
row3 = make_brick_row("blue", y_brick - 2*((brick_thickness) + gap_size))
row4 = make_brick_row("yellow", y_brick - 3*((brick_thickness) + gap_size))

################################################################
############################ Ball ##############################
################################################################

#Making the ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("hot pink")
ball.shape("circle")
ball.penup()
ball.goto(0, paddle.ycor() + (paddle_thickness / 2.0) + ball_size)

# Set the angle of the ball
heading = random.randint(10,170)
ball.setheading(heading)

'''
TODO: Bounce wall
15m

Create a function called bounce_wall that bounces the ball whenever it hits
the boundary.
	- If the ball is at a corner (in other words, its x coordinate 
		and y coordinate are both past the boundaries) then the ball 
		should bounce back in exactly the opposite direction it came from.

One way to do this is to change the angle of the ball if it is past 
the boundary. If you use this approach, use the function heading to get the 
current angle of the ball and the function setheading to change 
the angle of the ball.
	- If the ball is past the left or right boundary, change the angle to be 
		180 minus the current angle
	- If the ball is past the top of the boundary, change the angle to be 
		360 minus the current angle

Example use of heading and setheading:
	turtle_angle = name_of_turtle.heading()

	name_of_turtle.setheading(new_angle)
'''

#Checks for wall collision and changes direction
def bounce_wall():
	pass 

'''
TODO: Bounce paddle
30m

Create a function called bounce_paddle that bounces the ball off the paddle.

To check if the ball is touching the paddle,
you have to check that all the following are true:

	1) the ball is heading downwards
	2) the y coordinate of the ball minus the ball size is less 
		than the y coordinate of the top edge of the paddle
	3) the x coordinate of the ball plus the ball size is greater 
		than the x coordinate of the left edge of the paddle
	4) the x coordinate of the ball minus the ball size is less than 
		the x coordinate of right edge of the paddle

If all the above conditions are True, then change the angle of the ball 
to 360 minus the current angle.

Hint: Think about how to use paddle_width to calculate the edges of the paddle
'''

#Checks for paddle collision and changes direction
def bounce_paddle():
	pass

'''
TODO: Bounce brick row
20m

Create a function called bounce_brick_row that accepts a 
list of bricks as an argument.

This function should check whether the ball is touching each brick in the list.
If the ball is touching the brick and the brick is visible, then make sure 
to hide the brick and bounce the ball (just like in bounce_paddle).

To check if a brick is visible, use the isvisible() function on each brick. 
The isvisible function returns True if the brick is still visible.
To hide a turtle you can use the function ht.
	
	Examples:
		name_of_turtle.ht()
		name_of_turtle.isvisible()

Hint: To check if the ball is touching each brick, think about how you did 
this for the paddle. Remember that in the case of bricks, you'll have to check
whether the ball is within all 4 edges of the brick and it doesn't matter 
in what direction the ball is moving.
'''
def bounce_brick_row(row):
	pass

def bounce_bricks():
	bounce_brick_row(row1)
	bounce_brick_row(row2)
	bounce_brick_row(row3)
	bounce_brick_row(row4)


################################################################
####################### Gameplay ###############################
################################################################

'''
TODO: Write bricks_gone_row function
5-10m

Create a function called bricks_gone_row that accepts a list of bricks
as an argument and returns True if all the bricks in that list are not visible.
The function returns False if there is still at least one brick that is visible.

To check if a brick is visible, use the isvisible() function on each brick.
The isvisible function returns True if the brick is still visible.
'''
def bricks_gone_row(row):
	return False

'''
TODO: Write bricks_gone function
5-10m

Create a function called bricks_gone that calls brick_gone_row 4 times:
once on each row (row1, row2, row3, row4).
If all 4 brick rows are gone, then return True. Otherwise return False.
'''
def bricks_gone():
	return False

def startGame():
	lose = False

	#Make the ball move continuously
	while True:
		ball.forward(ball_speed)
		'''
		TODO: Player loses

		If the ball is below the bottom boundary, then hide the ball turtle,
		set the lose variable to True and break from this while loop.
		'''
		


		bounce_wall()
		bounce_paddle()
		bounce_bricks()
		'''
		TODO: Call bricks_gone function

		Call the bricks_gone function and if it returns True then break from
		this while loop
		'''
	

	
	'''
	TODO: Create writer turtle for game over
	
	Create a turtle that writes either "You lose!" or "You win!"
	depending on the value of the variable lose.

	You can use the function write for the turtle to write text.
	Example:
		name_of_turtle.write("Text to write on screen")

	You'll want to change the color of the turtle to something other than black
	so that you can see the text.

	If you'd like, you can use the function ht to hide the turtle.
	'''
	

screen.onkey(startGame, "space")
screen.listen()

# Closes the game window when you click the screen
screen.exitonclick()
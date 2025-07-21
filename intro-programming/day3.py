import random
import turtle
t = turtle.Turtle()
# t.pencolor("pink")
# t.pensize(10)
screen = turtle.Screen()

# num = random.randint(1, 10)
# print("My random integer is " + str(num))

# num = random.randint(150, 300)
# print("My random int is " + str(num))
# t.forward(num)

######.goto() — move to a new spot
#Use .goto(x, y) to place your Turtle exactly on the screen.
#Great for jumping between shapes or starting a new drawing.
# t.forward(50)
# t.penup()          # lift the pen so it won't draw a line
# t.goto(100, 50)    # jump to x=100, y=50
# t.pendown()        # put the pen back down
# t.forward(50)      # draw forward from the new spot

######.goto() + random
# Randomly scatter shapes all over your screen.
# Same idea you’ll use for game objects (e.g., ball spawns).
# x = random.randint(-200, 200)
# y = random.randint(-200, 200)
# print("My x is " + str(x))
# print("My y is " + str(y))
# t.penup()
# t.goto(x, y)
# t.pendown()
# t.forward(100)

######.setheading() — turn to an exact angle
# .right() and .left() turn relative to where you’re facing now.
# .setheading() snaps you to an absolute direction (0–360 degrees).
# t.setheading(90)  # face north (up)
# t.forward(100)
# t.setheading(180) # face west (left)
# t.forward(50)
# t.setheading(0)   # face east (right)
# t.forward(50)

#####
# This makes your Turtle move in totally random directions.
# Good for games, random patterns, or fun surprises.
# angle = random.randint(0, 360)  # pick random angle
# print("My angle num is " + str(angle))
# t.setheading(angle)
# t.forward(100)

# number_string = "123"
# number = "123"
# print(number_string == number)

# age = int(input("What is your age?"))
# print(type(age))

# if age >= 18:
#     print("You can vote")
# else:
#     print("You are too to vote")

# score =60

# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# else:
#     print("C or below")

# num = random.randint(1, 100)

# print(num)

# if num > 50:
#     print("Going far")
#     t.forward(200)
# else:
#     print("Staying close")
#     t.forward(50)

num = random.randint(0, 100)
x = random.randint(-200, 200)
y = random.randint(-200, 200)
angle = 270
pensize = 10

t.forward(50)

if num < 100:
    t.pensize(pensize)
    t.pencolor("pink")
    t.setheading(angle)
    t.forward(100)
elif num > 100:
    t.pensize(pensize*2)
    t.pencolor("blue")
    t.penup()
    t.goto(x, y)
    t.pendown()
else:
    t.pencolor("red")

t.forward(100)

screen.mainloop()


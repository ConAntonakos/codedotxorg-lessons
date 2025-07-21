# ctrl + shift + p

import turtle

# Create a screen (optional, but good practice)
screen = turtle.Screen()

# Create a Turtle object
t = turtle.Turtle()

t.pensize(5)

t.pencolor("red")

# Move it forward
t.forward(100)

t.right(90)

t.forward(100)

t.penup()

t.right(90)

t.backward(90)

t.pendown()

t.right(90)

t.forward(50)

# Keep the window open until you click
screen.mainloop()

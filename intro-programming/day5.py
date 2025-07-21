import random
import turtle
t = turtle.Turtle()
screen = turtle.Screen()
# screen.bgcolor("red")

colors = ["red", "blue", "green"]
player = {
    "name": "Joandri",
    "score": 1000
}
# del player["score"]
# print(player)
# colors.remove("blue")
# print(colors)
# colors.append("blue")
# print(colors)
# del colors[1]
# print(colors)

# t.setx(100)
# t.sety(-200)
# t.forward(100)

# t.goto(100, 50)
# x = t.xcor()
# y = t.ycor()
# print(x, y)

# def say_hello():
#     print("Hello")

# def greet(name):
#     print("Hello,", name)

# greet("Belina")
# greet("Joandri")

# def add(x, y):
#     return x + y

# print(add(100, 50))

# def subtract(a, b):
#     return a - b
# print(subtract(100, 50))

# def divide(a, b):
#     return a/b

# def multiply(a, b):
#     return a*b

# def draw_square(size):
#     for i in range(4):
#         t.forward(size)
#         t.right(90)

# draw_square(100)
# draw_square(200)
# draw_square(50)

def move_forward():
    t.forward(50)

turtle.listen()
turtle.onkey(move_forward, "Up")


def move_left(size):
    x = t.xcor() # 0
    x -= 20 # Move 20 units to the left
    t.setx(-size) # Set my turtle to that new x coordinate

screen.listen()
screen.onkey(lambda: move_left(100), "t")
# screen.onkeypress(move_left, "Left")


turtle.done()




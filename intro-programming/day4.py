import random
import turtle
t = turtle.Turtle()
# screen = turtle.Screen()

# num = random.randint(1, 20)

# print("Number:", num)

# num = 9

# if num > 10:
#     print("Big!")
#     if num % 2 == 0:
#         print("And even!")
#     else:
#         print("And odd!")
# else:
#     print("Small!")

# score = random.randint(0, 100)
# print("Score:", score)

# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# else:
#     print("Grade: D or below")

#17

# for i in range(1, 5):
#     print(i)

# for j in range(5, 0, -1):
#     print(j)

# total = 0
# for i in range(1, 6):
#     print(i)
#     total = total + i
# #(total += i)
# print("Total:", total)

# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)

# for i in range( 4):
#     print(i)
#     t.forward(100)
#     t.right(90)

# count = 0

# while count < 5:
#     t.forward(50)
#     t.right(random.randint(0, 360))
#     count = count + 1

# colors = ["red", "blue", "green"]

# for i in range(len(colors)):
#     print("Index:", i, "Color:", colors[i])
#     t.pencolor(colors[i])
#     # colors[position], i = position
#     t.forward(50)
#     t.right(180)

colors = [0, 1, 2]
dict = {"name": "Joandri", "age": 1000, "eyeColor": "green"}
dict["age"] = 300
dict["tshirt"] = "black"
print(dict)
for key in dict:
    print(key)
    value = str(dict[key])
    print("My key is " + key + " and my value is " + value)



#18
# count = 1
# while count <= 5:
#     print("Number:", count)
#     count += 1

#22
# colors = ["red", "blue", "green"]
# print(colors[0]) 
# print(colors[1])

#23
# colors = ["red", "blue", "green"]
# colors[1] = "yellow"
# print(colors)

# 31
# colors = ["red", "blue", "green"]
# color = random.choice(colors)
# if color == "red":
#     print("Stop!")
# else:
#     print("Go with", color)

#28
# t = turtle.Turtle()
# colors = ["red", "blue", "green", "yellow"]
# for i in range(5):
#     color = random.choice(colors)
#     t.pencolor(color)
#     if color == "red":
#         t.forward(50)
#     else:
#         t.forward(20)
#     t.right(72)

#33
# colors = ["red", "blue", "green"]
# for color in colors:
#     print(color)


#35
# colors = ["red", "blue", "green"]

# for color in colors:
#     t.pencolor(color)
#     t.forward(50)
#     t.right(90)

# screen.mainloop()
import colorgram
import turtle
import random
turtle.colormode(255)
screen = turtle.Screen()
screen.setup(width=400, height = 350)

colors = colorgram.extract('6. Turtle & Graphical User Interface/Drawing Dots/image.jpg', 30)
rgb_color = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b 
    new_color = (r, g, b)
    rgb_color.append(new_color)

tim = turtle.Turtle()
tim.penup()
tim.ht()
y_position = [-210, -180, -150, -120, -90, -60, -30, 0, 30, 60]
for _ in range(10):
    tim.goto(-120, y=y_position[_] + 70)
    for _ in range (10):
        tim.dot(20, random.choice(rgb_color))
        tim.forward(30)


screen.exitonclick()
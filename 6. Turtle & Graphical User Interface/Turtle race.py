from turtle import Turtle, Screen, TK
import random

screen = Screen()
screen.setup(width=500, height = 400)
is_race_on = False

user_input = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")

turtle_color = ["red", "yellow", "blue", "brown", "purple", "orange"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

if user_input:
    is_race_on = True

for index in range(6):
    tim = Turtle("turtle")
    tim.penup()
    tim.color(turtle_color[index])
    tim.goto(x = -230, y = y_position[index])
    all_turtle.append(tim)

while is_race_on:
    
    for turtle_race in all_turtle:
        turtle_race.forward(random.randint(0, 10))
        if turtle_race.xcor() > 230:
            is_race_on = False
            winning_color = turtle_race.pencolor()
            if winning_color == user_input:
                TK.messagebox.showinfo("Congratulation!", f"You won! {winning_color} turtle is winner")
            else:
                TK.messagebox.showinfo("What a pity!", f"You lost! {winning_color} turtle is winner")


screen.exitonclick()
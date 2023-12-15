from turtle import Screen, Turtle
from Paddle import Paddle_feature
from Ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)


l_paddle = Paddle_feature(-350, 0)
r_paddle = Paddle_feature(350, 0)

ball = Ball()

score = ScoreBoard()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320:
        ball.bounce_x()
        score.r_score_increase()
        
    if ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()
        score.l_score_increase()
        
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.reset_position()
screen.exitonclick()
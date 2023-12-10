from turtle import Screen, Turtle, TK
import time
from snake_characteristic import Snake
from snake_food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(500, 500)
screen.bgcolor("green")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()
snake = Snake()
food = Food()
score = ScoreBoard()

is_game_start = True
    
while is_game_start:
    screen.update()
    time.sleep(0.1)
    screen.listen()
    
    snake.snake_move()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    # checking snake eats food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.ScoreCount()
        snake.extend_snake()
    # Game will be ended if snake run out of the area
    if snake.head.xcor() > 230 or snake.head.xcor() < -230 or snake.head.ycor() > 230 or snake.head.ycor() < -230:
        is_game_start = False
        TK.messagebox.showinfo("You Lost!", f"Your Score: {score.score}")
    # Checking snake eats itself
    for segment in range(len(snake.snake) - 1):
        if snake.head.distance(snake.snake[segment+1]) < 15:
            is_game_start = False
            TK.messagebox.showinfo("You Lost!", f"Your Score: {score.score}")
screen.exitonclick()

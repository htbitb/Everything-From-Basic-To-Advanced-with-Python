from turtle import Turtle

class Paddle_feature(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.init_shape()
        
    def init_shape(self):
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(self.x_cor, self.y_cor)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        
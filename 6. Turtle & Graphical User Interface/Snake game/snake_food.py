from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        random_x = random.randint(-230, 230)
        random_y = random.randint(-230, 230)
        self.goto(random_x, random_y)
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.ht()
        self.penup()
        self.color('black')
        self.goto(0,230)
        self.write(f"Score: {self.score}", align = "center", font=("Arial", 12, "normal"))
    
    def ScoreCount(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align = "center", font=("Arial", 12, "normal"))

        
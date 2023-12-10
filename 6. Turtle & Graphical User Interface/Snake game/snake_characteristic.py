import turtle as tt
class Snake():
    def __init__(self):
        self.starting_position = [(0, 0), (-20, 0), (-40, 0)]
        self.snake =[]
        self.init_snake()
        self.head = self.snake[0]
    
    def init_snake(self):
        for position in self.starting_position:
            self.add_segment(position)
            
    def add_segment(self, position):
            segment = tt.Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.snake.append(segment)  
            
    def snake_move(self):  
        for seg_num in range (len(self.snake) - 1, 0 ,-1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.forward(20)
        
        if self.head.xcor() == 250:
            self.head.goto(-250, )
        elif self.head.xcor() == -250:
            self.head.goto(250, )

            
    def up(self):
        if self.head.heading() == 0 or self.head.heading() == 180:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 0 or self.head.heading() == 180:
            self.head.setheading(270)
        
    def left(self):
        if self.head.heading() == 90 or self.head.heading() == 270:
            self.head.setheading(180)
            
    def right(self):
        if self.head.heading() == 90 or self.head.heading() == 270:
            self.head.setheading(0)
            
    def extend_snake(self):
        self.add_segment(self.snake[-1].position())
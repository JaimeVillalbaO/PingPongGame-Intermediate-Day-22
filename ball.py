from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()    
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x = 10
        self.y = 10
        self.move_speed = 0.1
    
    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)
    
    def bounce(self):
        self.y *= -1
        

    def detect_paddle(self):
        self.x *= -1
        self.move_speed *= 0.8

    def reset_position(self):
        self.goto(0 , 0)
        self.move_speed = 0.1
        self.detect_paddle()
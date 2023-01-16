from turtle import Turtle
import random

class Ball(Turtle):
    random_y = 0
    random_x = 0
    def __init__(self) -> None:
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.pu()
        # self.speed(100)
        self.color("white")
    
    def move(self):
        self.goto(self.xcor() + self.random_x,self.ycor() + self.random_y)

    def reset_position(self):
        self.goto(0, 0)

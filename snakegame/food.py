from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5)
        self.color("pink")
        self.speed("fastest")
        x = random.randint(-360, 360)
        y = random.randint(-360, 360)
        self.goto(x, y)
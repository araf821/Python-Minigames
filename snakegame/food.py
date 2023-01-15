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
        self.refresh()

    def refresh(self):
        x = random.randint(-360, 360)
        y = random.randint(-360, 360)
        if y % 20 != 0:
            y += 10
        self.goto(x, y)

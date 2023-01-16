from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.pu()
        self.color("white")
        
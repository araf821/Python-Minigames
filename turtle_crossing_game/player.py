from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.pu()
        self.setheading(90)
        self.goto(0, -230)

    def move(self):
        self.fd(20)
from turtle import Turtle

class Paddle(Turtle):
    y = 0

    def __init__(self) -> None:
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.pu()
        self.speed(50)
        self.goto(-380, 0)

    def up(self):
        if self.y < 240:
            self.y += 20
        self.goto(-380, self.y)

    def down(self):
        if self.y > -240:
            self.y -= 20
        self.goto(-380, self.y)


class CompPaddle(Turtle):
    y_speed = 30

    def __init__(self) -> None:
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.pu()
        self.goto(375, 0)

    def move(self):
        self.goto(self.xcor(), self.ycor() + self.y_speed)

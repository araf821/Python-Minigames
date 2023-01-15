from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.goto(0, 360)
        self.refresh_text()

    def refresh_text(self):
        self.write(f"Score: {self.score}", move=False,
                   align="center", font=FONT)

    def add(self):
        self.clear()
        self.score += 1
        self.refresh_text()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", move=False, align="center", font=FONT)

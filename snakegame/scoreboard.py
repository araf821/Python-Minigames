from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    score = 0
    highscore = 0
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.goto(0, 360)
        self.refresh_text()

    def refresh_text(self):
        with open("./highscore.txt", mode='r') as file:
            self.highscore = int(file.read())
        self.write(f"Score: {self.score}   Highscore: {self.highscore}", move=False,
                   align="center", font=FONT)

    def add(self):
        self.clear()
        self.score += 1
        self.refresh_text()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("./highscore.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.clear()
        self.refresh_text()
        

    

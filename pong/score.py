from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.ht()
        self.player_score = 0
        self.comp_score = 0
        self.goto(-100, 200)
        self.write(f"{self.player_score}", align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(f"{self.comp_score}", align="center", font=("Courier", 60, "normal"))

    def player_add(self):
        self.player_score += 1
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.player_score}", align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(f"{self.comp_score}", align="center", font=("Courier", 60, "normal"))
    
    def comp_add(self):
        self.comp_score += 1
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.player_score}", align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(f"{self.comp_score}", align="center", font=("Courier", 60, "normal"))
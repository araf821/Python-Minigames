from turtle import Turtle

class UI(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.color("black")
        self.pu()
        self.goto(-318, 215)
        self.write("Level: 1", align="center", font=("Courier", 20, "bold"))

    def level_up(self, level):
        self.clear()
        self.goto(-318, 215)
        self.write(f"Level: {level}", align="center", font=("Courier", 20, "bold"))
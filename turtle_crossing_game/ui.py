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
    
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Courier", 60, "bold"))
        self.goto(0, -15)
        self.write("Your turtle was squished to death and its blood was splattered all over the place!", align="center", font=("Courier", 10, "bold"))

    def game_finished(self):
        self.clear()
        self.goto(0, 0)
        self.write("All Levels Completed!", align="center", font=("Courier", 42, "bold"))
        self.goto(0, -15)
        self.write("Hmmm...now what?", align="center", font=("Courier", 16, "bold"))

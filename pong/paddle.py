from turtle import Turtle

class Paddle(Turtle):
    player_paddle_pieces = []
    computer_paddle_pieces = []

    def __init__(self) -> None:
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        # Player paddle
        y = 50
        for _ in range(5):
            sq = Turtle("square")
            sq.color("white")
            sq.pu()
            sq.goto(-380, y)
            y -= 20
            self.player_paddle_pieces.append(sq)
        # Enemy Paddle
        y = 50
        for _ in range(5):
            sq = Turtle("square")
            sq.color("white")
            sq.pu()
            sq.goto(375, y)
            y -= 20
            self.computer_paddle_pieces.append(sq)
from turtle import Turtle

class Score(Turtle):
    player_score = Turtle()
    computer_score = Turtle()
    line = Turtle()    
    def __init__(self) -> None:
        super()._init__()
        self.create_score_keepers()
        self.create_line()
    
    def create_score_keepers(self):
        pass

    def create_line(self):
        pass


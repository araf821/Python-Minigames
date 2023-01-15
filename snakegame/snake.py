from turtle import Turtle

class Snake():
    pieces = []
    def __init__(self) -> None:
        x = 0
        for _ in range (3):
            piece = Turtle("square")     
            piece.pu()   
            piece.color("white")
            piece.goto(x, 0)
            x -= 50
            
            self.pieces.append(piece)

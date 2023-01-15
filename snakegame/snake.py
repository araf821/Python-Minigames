from turtle import Turtle

move_speed = 20


class Snake():
    pieces = []

    def __init__(self) -> None:
        x = 0
        for _ in range(5):
            piece = Turtle("square")
            piece.pu()
            piece.color("white")
            piece.goto(x, 0)
            x -= 20

            self.pieces.append(piece)

    def move(self):
        for piece in range(len(self.pieces) - 1, 0, -1):
            new_x = self.pieces[piece - 1].xcor()
            new_y = self.pieces[piece - 1].ycor()
            self.pieces[piece].goto(new_x, new_y)
        self.pieces[0].fd(move_speed)

    def move_up(self):
        if (self.pieces[0].heading() == 270):
            return
        for piece in self.pieces:
            piece.setheading(90)

    def move_down(self):
        if (self.pieces[0].heading() == 90):
            return
        for piece in self.pieces:
            piece.setheading(270)

    def move_left(self):
        if (self.pieces[0].heading() == 0):
            return
        for piece in self.pieces:
            piece.setheading(180)

    def move_right(self):
        if (self.pieces[0].heading() == 180):
            return
        for piece in self.pieces:
            piece.setheading(0)

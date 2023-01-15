from turtle import Screen, Turtle

screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Snek")
screen.tracer(0)

t1 = Turtle()
t1.shape("square")
t1.setx(0)
t1.color("white")
t1.pu()

t2 = Turtle()
t2.shape("square")
t2.goto(-20, 0)
t2.color("white")
t2.pu()

t3 = Turtle()
t3.shape("square")
t3.goto(-40, 0)
t3.color("white")
t3.pu()

body_pieces = [t1, t2, t3]

screen.tracer(1)

play = True
while play == True:
    screen.update()
    for piece in body_pieces:
        piece.fd(20)

        

screen.exitonclick()
from turtle import Turtle, Screen

screen = Screen()
screen.listen()
t = Turtle()

def move_forwards():
    t.fd(10)

def move_backwards():
    t.backward(10)

def turn_clockwise():
    t.right(5)

def turn_counterclockwise():
    t.left(5)

def clear_canvas():
    t.reset()


screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="a", fun=turn_counterclockwise)
screen.onkey(key="c", fun=clear_canvas)

screen.exitonclick()

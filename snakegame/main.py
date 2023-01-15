from turtle import Screen, Turtle
from snake import Snake
from time import sleep

screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Snek")
screen.tracer(0)

snake = Snake()

screen.update()

# def move_up():
#     for piece in body_pieces:
#         piece.heading(90)

# def move_down():
#     for piece in body_pieces:
#         piece.heading(270)

# def move_left():
#     for piece in body_pieces:
#         piece.heading(180)

# def move_right():
#     for piece in body_pieces:
#         piece.heading(0)

# play = True
# while play == True:
#     screen.onkey(fun="move_up", key="w")
#     screen.onkey(fun="move_left", key="a")
#     screen.onkey(fun="move_down", key="s")
#     screen.onkey(fun="move_right", key="d")
#     screen.update()
#     sleep(0.1)
#     for piece in range(len(body_pieces) - 1, 0, -1):
#         new_x = body_pieces[piece - 1].xcor()
#         new_y = body_pieces[piece - 1].ycor()
#         body_pieces[piece].goto(new_x, new_y)
#     body_pieces[0].fd(20)
        

screen.exitonclick()
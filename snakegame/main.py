from turtle import Screen, Turtle
from snake import Snake
from time import sleep

screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Snek")
screen.tracer(0)
screen.listen()

snake = Snake()

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

play = True
while play == True:
    screen.onkey(fun=snake.move_up, key="w")
    screen.onkey(fun=snake.move_left, key="a")
    screen.onkey(fun=snake.move_down, key="s")
    screen.onkey(fun=snake.move_right, key="d")
    screen.update()
    sleep(0.1)
    snake.move()
        

screen.exitonclick()
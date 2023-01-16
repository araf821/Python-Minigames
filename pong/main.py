from turtle import Screen
from time import sleep
from score import Score
from ball import Ball
from paddle import Paddle, CompPaddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)
screen.title("Pawng")

score_keeper = Score()
player_paddle = Paddle()
computer_paddle = CompPaddle()
ball = Ball()

screen.onkey(key="w", fun=player_paddle.up)
screen.onkey(key="s", fun=player_paddle.down)

screen.update()
screen.tracer(1)














screen.exitonclick()
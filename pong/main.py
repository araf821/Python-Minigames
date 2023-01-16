from turtle import Screen
from time import sleep
from score import Score
from ball import Ball
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

score_keeper = Score()
paddles = Paddle()


screen.update()













screen.exitonclick()
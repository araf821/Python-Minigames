from turtle import Screen
from time import sleep
from score import Score
from ball import Ball
from paddle import Paddle, CompPaddle
import random

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

# Assiging random movements for the ball
coordinates = [-2, 2]
ball.random_y = random.choice(coordinates)
ball.random_x = random.choice(coordinates)

screen.onkey(key="w", fun=player_paddle.up)
screen.onkey(key="s", fun=player_paddle.down)

screen.update()
screen.tracer(1)

play = True
while play:
    ball.move()
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.random_x *= -1
    elif ball.ycor() > 280 or ball.ycor() < -280:
        ball.random_y *= -1
    elif ball.distance(player_paddle) < 50 and ball.xcor() < -330:
        ball.random_x *= -1
        print("collided")
    elif ball.distance(computer_paddle) < 50 and ball.xcor() > 340:
        ball.random_x *= -1
        print("collided")


screen.exitonclick()

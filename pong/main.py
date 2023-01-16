from turtle import Screen, Turtle
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

line = Turtle()
line.color("white")
line.ht()
line.setheading(270)
line.pensize(5)
line.pu()
line.goto(0, 275)
for _ in range (14):
    line.pendown()
    line.fd(20)
    line.pu()
    line.fd(20)


score_keeper = Score()
player_paddle = Paddle()
computer_paddle = CompPaddle()
ball = Ball()

# Assiging random movements for the ball
coordinates = [-7.5, 7.5]
ball.random_y = random.choice(coordinates)
ball.random_x = random.choice(coordinates)

screen.onkey(key="w", fun=player_paddle.up)
screen.onkey(key="s", fun=player_paddle.down)

# screen.update()
screen.tracer(1)

play = True
while play:
    # screen.update()
    ball.move()
    computer_paddle.move()
    if ball.xcor() > 380:
        score_keeper.player_add()
        sleep(1)
        ball.reset_position()
        ball.random_y = random.choice(coordinates)
        ball.random_x = random.choice(coordinates)
    elif ball.xcor() < -380:
        score_keeper.comp_add()
        sleep(1)
        ball.reset_position()
        ball.random_y = random.choice(coordinates)
        ball.random_x = random.choice(coordinates)
    elif ball.ycor() > 280 or ball.ycor() < -280:
        ball.random_y *= -1
    elif ball.distance(player_paddle) < 45 and ball.xcor() < -320:
        ball.random_x *= -1
        ball.setpos(-325, ball.ycor())
        print("collided")
    elif ball.distance(computer_paddle) < 45 and ball.xcor() > 320:
        ball.random_x *= -1
        ball.setpos(321, ball.ycor())
        print("collided")
    elif computer_paddle.ycor() > 250 or computer_paddle.ycor() < -250:
        computer_paddle.y_speed *= -1

screen.exitonclick()

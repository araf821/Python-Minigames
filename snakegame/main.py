from turtle import Screen
from snake import Snake
from time import sleep
from food import Food

screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Snek")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()

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
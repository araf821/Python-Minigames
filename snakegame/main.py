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

# Initialize snake and its food
snake = Snake()
food = Food()

# Keyboard controls
screen.onkey(fun=snake.move_up, key="w")
screen.onkey(fun=snake.move_left, key="a")
screen.onkey(fun=snake.move_down, key="s")
screen.onkey(fun=snake.move_right, key="d")

play = True
while play == True:
    screen.update()
    sleep(0.1)
    snake.move()

    # Detecting collisions
    if snake.head.distance(food) < 20:
        food.refresh()
        

screen.exitonclick()
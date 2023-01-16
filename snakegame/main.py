from turtle import Screen
from snake import Snake
from time import sleep
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Snek")
screen.tracer(0) 
screen.listen()
scoreboard = Scoreboard()

# Initialize snake and its food
snake = Snake()


food = Food()
screen.update()
sleep(2)

# Keyboard controls
screen.onkey(fun=snake.move_up, key="w")
screen.onkey(fun=snake.move_left, key="a")
screen.onkey(fun=snake.move_down, key="s")
screen.onkey(fun=snake.move_right, key="d")

play = True
while play == True:
    screen.update()
    sleep(0.05)
    snake.move()

    # Collecting Food
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.add()
        snake.add()

    # Detecting collisions
    # Collision with tail
    for piece in snake.pieces[1:]:
        if snake.head.distance(piece) < 10:
            scoreboard.reset()
            snake.reset()

    # Wall Collisions
    snakeX = snake.head.xcor()
    snakeY = snake.head.ycor()
    if snakeX > 380 or snakeX < -380 or snakeY > 380 or snakeY < -380:
        scoreboard.reset()
        snake.reset()

screen.exitonclick()

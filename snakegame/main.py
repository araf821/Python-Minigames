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

    # Detecting collisions

    # Collecting Food
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.add()
        snake.add()
    
    # Collision with tail
    for piece in snake.pieces:
        if snake.head.distance(piece) < 10:
            play = False

    # Growing Bigger
    snakeX = snake.head.xcor()
    snakeY = snake.head.ycor()
    if snakeX > 380 or snakeX < -380 or snakeY > 380 or snakeY < -380:
        play = False
        scoreboard.game_over()

screen.exitonclick()
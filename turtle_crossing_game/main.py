from turtle import Screen
from time import sleep
from cars import Cars
from player import Player
from ui import UI

s = Screen()
s.setup(800, 500)
s.bgcolor("skyblue")
s.tracer(0)

player = Player()

s.listen()
s.onkey(key="w", fun=player.move)

# Level count keeper
ui = UI()
# Depending on the level, number of cars that show up on screen will vary
cars_to_generate = [6, 10, 14, 19, 24]
level = 1
cars = Cars(cars_to_generate[level + 2])

s.tracer(1)

play = True
while play:
    cars.move()

s.exitonclick()
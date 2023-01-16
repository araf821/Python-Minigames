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
s.onkey(key="w", fun=player.up)
s.onkey(key="s", fun=player.down)

# Level count keeper
ui = UI()
# Depending on the level, number of cars that show up on screen will vary
cars_to_generate = [20, 18, 15]
level = 1
cars = Cars()

play = True
while play:
    sleep(0.01)
    s.update()
    cars.generate_car(cars_to_generate[level - 1])
    cars.move()

    # New level initializer
    if player.ycor() > 230:
        cars.clear()
        player.goto(0, -230)
        level += 1
        if level != 4:
            ui.level_up(level)
        else:
            ui.game_finished()
            play = False

    for car in cars.cars:
        if player.distance(car) < 20:
            player.goto(0, -300)
            ui.game_over()


s.exitonclick()
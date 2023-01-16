from turtle import Screen
from time import sleep
from cars import Cars
from player import Player
from ui import UI

s = Screen()
s.setup(800, 500)
s.bgcolor("skyblue")
s.tracer(0)
s.listen()

interface = UI()

player = Player()

s.onkey(key="w", fun=player.move)

s.update()
s.tracer(1)




s.exitonclick()
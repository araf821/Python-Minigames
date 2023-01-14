from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=900, height=700)
screen.listen()

green_turtle = Turtle()
green_turtle.color("green")
green_turtle.shape("turtle")
green_turtle.shapesize(2)
green_turtle.pu()
green_turtle.goto(x=-300, y=100)

blue_turtle = Turtle()
blue_turtle.color("blue")
blue_turtle.shape("turtle")
blue_turtle.shapesize(2)
blue_turtle.pu()
blue_turtle.goto(x=-150, y=100)

yellow_turtle = Turtle()
yellow_turtle.color("yellow")
yellow_turtle.shape("turtle")
yellow_turtle.shapesize(2)
yellow_turtle.pu()
yellow_turtle.goto(x=0, y=100)

pink_turtle = Turtle()
pink_turtle.color("pink")
pink_turtle.shape("turtle")
pink_turtle.shapesize(2)
pink_turtle.pu()
pink_turtle.goto(x=150, y=100)

red_turtle = Turtle()
red_turtle.color("red")
red_turtle.shape("turtle")
red_turtle.shapesize(2)
red_turtle.pu()
red_turtle.goto(x=300, y=100)

turtles = [red_turtle, green_turtle, yellow_turtle, pink_turtle, blue_turtle]

user_bet = screen.textinput(
    "Turtle Race", prompt="Which coloured turtle would you like to bet on?")

green_turtle.goto(-420, y=200)
red_turtle.goto(-420, y=100)
yellow_turtle.goto(-420, y=0)
blue_turtle.goto(-420, y=-100)
pink_turtle.goto(-420, y=-200)


def start_race():
    race = True
    while race == True:
        for turtle in turtles:
            turtle.forward(random.randint(0, 20))
            if turtle.xcor() > 400:
                winner = turtle.pencolor()
                print(f"The winner is the {winner} turtle!")
                race = False
                break


start_race()


screen.exitonclick()

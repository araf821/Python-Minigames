from turtle import Turtle
import turtle
import random
from time import sleep

class Cars():
    cars = []
    random_starting_points = [450, 500, 550, 600, 700, 800, 750, 650, 850, 950, 900, 1000]
    # random_speeds = [10, 20, 30]
    colors = ["red", "green", "blue", "black", "pink", "violet"]
    def __init__(self, num_cars):
        self.generate_cars(num_cars)

    def generate_cars(self, num_cars):
        for _ in range(num_cars):
            car = Turtle()
            car.color(random.choice(self.colors))
            car.pu()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            car.goto(random.choice(self.random_starting_points), random.randint(-200, 200))
            self.cars.append(car)
    
    def move(self):

        for car in self.cars:
            if car.xcor() < -420:
                car.goto(400, random.randint(-200, 200))
                car.color(random.choice(self.colors))
            car.goto(-430, car.ycor())
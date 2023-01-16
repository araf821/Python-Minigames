from turtle import Turtle
import turtle
import random
from time import sleep

class Cars():
    
    def __init__(self):
        self.cars = []
        self.random_starting_points = [450, 500, 550, 600, 700, 800, 750, 650, 850, 950, 900, 1000]
        self.random_speeds = [10, 20, 30]
        self.colors = ["red", "green", "blue", "black", "pink", "violet", "orange"]

    def generate_car(self, car_rate):
        if random.randint(1, car_rate) == 1:
            car = Turtle()
            car.pu()
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(self.colors))
            car.goto(420, random.randint(-200, 200))
            self.cars.append(car)
    
    def move(self):
        for car in self.cars:
            car.bk(3)

    def clear(self):
        for car in self.cars:
            car.clear()
        self.cars = []

    # def generate_cars(self, num_cars):
    #     for _ in range(num_cars):
    #         car = Turtle()
    #         car.color(random.choice(self.colors))
    #         car.pu()
    #         car.speed(10)
    #         car.shape("square")
    #         car.shapesize(stretch_wid=1, stretch_len=2)
    #         car.setheading(180)
    #         car.goto(random.randint(-420, 420), random.randint(-200, 200))
    #         self.cars.append(car)
    
    # def move(self):
    #     for car in self.cars:
    #         if car.xcor() < -400:
    #             car.goto(420, random.randint(-200, 200))
    #         car.fd(6)
    
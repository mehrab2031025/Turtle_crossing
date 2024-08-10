from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.cars = []
        self.start_distance = STARTING_MOVE_DISTANCE
        self.speedup = MOVE_INCREMENT

    def create_cars(self):
        if random.randint(1, 15) == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)

    def move_cars(self):
        for i in self.cars:
            i.backward(self.start_distance)

    def car_speedup(self):
        self.start_distance += self.speedup

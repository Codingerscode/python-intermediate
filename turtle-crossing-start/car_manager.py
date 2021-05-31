from turtle import Turtle
import random
import time
# COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CARS = ["car.gif","car2.gif","car3.gif","car4.gif","bus.gif"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []

        
    def move(self):
        for i in self.cars:
            i.up()
            i.seth(180)
            i.fd(STARTING_MOVE_DISTANCE)
    
    def createcar(self):
        self.cars.append(Turtle(random.choice(CARS)))
        self.cars[len(self.cars)-1].up()
        self.cars[len(self.cars)-1].setpos(x=300,y=random.randint(-130,200))
        self.cars[len(self.cars)-1].fd(STARTING_MOVE_DISTANCE)
    
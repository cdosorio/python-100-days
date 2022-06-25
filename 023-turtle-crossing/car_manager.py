import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

class CarManager():

    def __init__(self) :        
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        y_pos = random.randint(-250, 250)
        new_car = Turtle(shape="square")
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.color(random.choice(COLORS))
        new_car.penup()        
        new_car.goto(x = 290 , y = y_pos )
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.move_distance          
            car.goto(new_x, car.ycor())
            
    def detect_collision(self, turtle):
        for car in self.all_cars:
            if  car.distance(turtle) < 10:           
                return True
        return False

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
        print(f"Distance increased to {self.move_distance}")
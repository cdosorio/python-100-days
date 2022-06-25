import random
from turtle import Turtle

DISTANCE = 10

class Ball(Turtle):

    def __init__(self) :
        super().__init__()
        self.y_direction = 1 # start going up
        self.x_direction = 1 # start going to the right
        self.shape("circle")
        self.penup()
        #self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("blue")
        #self.speed("slow")
        self.move_speed = 0.05

    def move(self):        
        random_x = self.xcor() + DISTANCE * self.x_direction
        random_y = self.ycor() + DISTANCE * self.y_direction
        self.goto(random_x, random_y)

    def bounce_y(self):
        self.y_direction *= -1

    def bounce_x(self):
        self.x_direction *= -1
        self.move_speed *= 0.8
        
    def restart(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()


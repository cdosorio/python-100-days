import time
from turtle import Screen, Turtle
import turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
carManager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="w", fun=turtle.up)

game_is_on = True
loop_counter = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create cars 
    loop_counter += 1
    if (loop_counter % 6 == 0):
        carManager.create_car()
    
    carManager.move_cars()
         
    if carManager.detect_collision(turtle):
        game_is_on = False 
        scoreboard.game_over()
    elif turtle.arrived_top() :
        turtle.restart()
        carManager.increase_speed()
        scoreboard.increment_score()



screen.exitonclick()

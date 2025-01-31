import random
from turtle import Turtle, Screen
import turtle

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle",)
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230 , y = -100 + 30 * turtle_index )
    all_turtles.append(new_turtle)

# race
print(user_bet)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. the {winning_color} is winner")
            else:
                print(f"You've lost. the {winning_color} is winner")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()
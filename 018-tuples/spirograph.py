import random
from turtle import Screen, Turtle

tim = Turtle()
tim.shape("turtle")
tim.color("brown")

# Challenge 2
""" for _ in range(4):
    for _ in range(10):
        tim.penup()
        tim.forward(5)
        tim.pendown()
        tim.forward(5)
    tim.right(90) """


# Challenge 3
""" def draw_shape(sides):
    degress = 360/sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(degress)

for sides in range(3,11):
    draw_shape(sides) """

# Challenge 4
"""screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

angles = [90,180,270]
#colors = ["red", "brown", "green", "blue", "yellow"]
tim.pensize(15)

for _ in range(30):
    dist = random.randint(40,100)
    angle = random.choice(angles)
    tim.pencolor(random_color())    
    tim.forward(dist)
    tim.right(angle) """


# Challenge 5
screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen.exitonclick()




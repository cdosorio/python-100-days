# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)

# # convert to list of tuples
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import random
from turtle import Screen, Turtle

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 
158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
    
screen = Screen()
screen.colormode(255)

space = 40
size_y = 10
size_x = 10

tim = Turtle()
tim.speed("fastest")
tim.hideturtle()
#tim.setpos(0,0)
tim.penup()

for y in range(size_y):  
    for x in range(size_x): 
        tim.begin_fill()             
        tim.setposition(space * x, space * y)
        tim.dot(20, random.choice(color_list))
        tim.end_fill()

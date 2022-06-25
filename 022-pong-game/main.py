import time
from turtle import Screen
from scoreboard import Scoreboard

from paddle import Paddle
from ball import Ball
#from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect colission with wall (top and bottom)
    if ball.ycor() > 280 or ball.ycor() < -280  :
        ball.bounce_y()

    #detect colission with paddles
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # detect if ball goes out 
    elif ball.xcor() > 400:
        ball.restart()
        scoreboard.l_point()
    elif ball.xcor() < -400:
        ball.restart()
        scoreboard.r_point()

screen.exitonclick()
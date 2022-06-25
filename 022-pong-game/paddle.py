from turtle import Turtle
# WIDTH = 20
# HEIGHT = 100
MOVE_DISTANCE = 20
X_POS = 350
Y_POS = 0


class Paddle(Turtle):

    def __init__(self, position) :
        super().__init__()
        
        self.penup()
        self.shape("square")        
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.goto(position)
        
    def go_up(self):        
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
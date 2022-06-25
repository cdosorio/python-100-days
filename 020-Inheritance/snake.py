from turtle import Turtle
INITIAL_SIZE = 3
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT= 180
RIGHT = 0

class Snake:

    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(INITIAL_SIZE):
            x_pos = 0 - 20 * i
            self.add_segment(x = x_pos , y = 0)

    def extend(self):
        self.add_segment(self.segments[-1].xcor(), self.segments[-1].ycor())

    def add_segment(self, x, y):
        new_segment = Turtle(shape="square",)
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(x, y)
        self.segments.append(new_segment)

    def move(self):
        for i in range( len(self.segments) - 1, 0, -1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):       
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

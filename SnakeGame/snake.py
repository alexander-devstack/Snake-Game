from token import RIGHTSHIFTEQUAL
from turtle import Turtle
MOVE_DISTANCE=20
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head=self.segments[0]
        self.move()
        self.up()
        self.down()
        self.right()
        self.left()

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_segment(positions)

    def add_segment(self,position):
            new_turtle = Turtle(shape="square")
            new_turtle.penup()
            new_turtle.shapesize(1, 1)
            new_turtle.goto(position)
            new_turtle.color("white")
            self.segments.append(new_turtle)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def up(self):
        if self.snake_head.heading() !=DOWN:
            self.snake_head.setheading(UP)
    def down(self):
        if self.snake_head.heading() !=UP:
            self.snake_head.setheading(DOWN)
    def right(self):
        if self.snake_head.heading()!=LEFT:
            self.snake_head.setheading(RIGHT)
    def left(self):
        if self.snake_head.heading()!=RIGHT:
            self.snake_head.setheading(LEFT)
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.snake_head=self.segments[0]

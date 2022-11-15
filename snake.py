from turtle import Turtle

Move_distance = 20
UP    = 90
DOWN  = 270
LEFT  = 180
RIGHT = 0

class Snake():

    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):

            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].goto(new_x, new_y)

        self.head.forward(Move_distance)

    def create(self):
        x_cor = 0
        for _ in range(0, 3):
            segment = Turtle(shape='square')
            segment.penup()
            segment.color('white')
            segment.goto(x_cor, 0)
            self.segments.append(segment)
            x_cor -= Move_distance




    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(RIGHT)

from turtle import Turtle

Move_distance = 20
UP    = 90
DOWN  = 270
LEFT  = 180
RIGHT = 0
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
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
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        segment = Turtle(shape='square')
        segment.penup()
        segment.color('white')
        segment.goto(position)
        self.segments.append(segment)


    def extends(self):
        self.add_segment(self.segments[-1].position())

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

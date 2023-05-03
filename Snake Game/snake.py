from turtle import Turtle

STARTING_X_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segment_list = []
        self.create_snake()
        self.head = self.segment_list[0]
        self.tail= self.segment_list[-1]

    def create_snake(self):
        for i in range(3):
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.setposition(y=0, x=STARTING_X_POSITIONS[i])
            self.segment_list.append(new_turtle)

    def refresh_snake(self):
        self.head.goto(1000, 1000)
        self.create_snake()

    def move(self):
        for seg_num in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[seg_num - 1].xcor()
            new_y = self.segment_list[seg_num - 1].ycor()
            self.segment_list[seg_num].goto(new_x, new_y)
        self.segment_list[0].forward(MOVE_DISTANCE)

    def extend(self):
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.setposition(y=self.segment_list[-1].ycor(), x=self.segment_list[-1].xcor())
        self.segment_list.append(new_turtle)


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

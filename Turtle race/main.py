from turtle import Turtle, Screen

tim = Turtle()
tim.color("dark green")
tim.shape("turtle")


def move_forward():
    tim.forward(10)

def move_backward():
    tim.tiltangle(180)
    tim.forward(10)

def move_right():
    tim.setheading(0)
    tim.forward(10)

def move_left():
    tim.setheading(180)
    tim.forward(10)

my_screen = Screen()

my_screen.onkey(fun=move_forward, key="d")
my_screen.onkey(fun=move_backward, key="a")
my_screen.onkey(fun=move_right, key="w")
my_screen.onkey(fun=move_left, key="s")
my_screen.listen()
my_screen.exitonclick()

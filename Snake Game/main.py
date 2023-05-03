
# TODO 1 Create screen

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Initialize the screen

my_screen = Screen()
my_screen.setup(600, 600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

# TODO 1 Create Snake

tim = Snake()
food = Food()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(tim.up, "Up")
my_screen.onkey(tim.down, "Down")
my_screen.onkey(tim.left, "Left")
my_screen.onkey(tim.right, "Right")

game_is_on = True

# TODO 3 Turn the snake

while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    tim.move()

    # detect collision with food
    distance = tim.head.distance(food)
    if distance < 13:
        food.refresh()
        tim.extend()
        scoreboard.increase_score()

    #detect collisiom with the wall
    if tim.head.xcor()>295 or tim.head.xcor()< -295 or tim.head.ycor()>295 or tim.head.ycor()< -295 :
        game_is_on= False
        scoreboard.game_over()

    # # detect collisiom with the tail
    # for segments in tim.segment_list:
    #     if segments == tim.head():
    #         pass
    #     elif tim.head.distance(segments) >10:
    #         game_is_on = False
    #         scoreboard.game_over()

my_screen.exitonclick()

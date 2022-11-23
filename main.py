import time
import turtle

from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
game_is_on =True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extends()
        score.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        #score.game_over()
        score.reset()
        snake.reset()

        #game_is_on = False

    # snake.segments[::2] means keep everything in the list but hold for every second item
    # snake.segments[::-1] will reverse the list
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            #game_is_on = False
            #score.game_over()
            snake.reset()
            score.reset()


    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")











screen.exitonclick()
import time
from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

mamba = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(mamba.up, "Up")
screen.onkey(mamba.down, "Down")
screen.onkey(mamba.left, "Right")
screen.onkey(mamba.right, "Left")



game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    mamba.move()

    #Detecting collision with food
    if mamba.head.distance(food) < 15:
        print("Hummy!")
        food.refresh()
        mamba.food_found()
        scoreboard.increase_score()

    #Detecting collision with the wall
    if mamba.head.xcor() > 280 or mamba.head.xcor() < -280 or mamba.head.ycor() > 280 or  mamba.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    #Detecting collision with the tail
    for square in mamba.snake_body:
        if square == mamba.head:
            pass
        elif mamba.head.distance(square) < 10:
            game_on = False
            scoreboard.game_over()











screen.exitonclick()
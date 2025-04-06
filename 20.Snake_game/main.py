import time
from turtle import Screen
from Snake import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

mamba = Snake()
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











screen.exitonclick()
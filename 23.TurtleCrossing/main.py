import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()


screen.listen()
screen.onkeypress(player.move_up,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if randint(1,6)==1:
        car_manager.create_cars()
    car_manager.move_cars()

    #detect collision with cars
    for car in car_manager.all_cars:
        if player.distance(car)<20:
            game_is_on=False

    #Detect if the car hit the finish line
    if player.is_at_the_finished_line():
        player.go_to_start()
        car_manager.speed_up()
        score.score_up()

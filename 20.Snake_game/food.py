import random
from turtle import Turtle

POSSIBLE_FOOD_COORDS = list(map(lambda a,b: (a,b), range(-280,280,20), range(-280,280,20)))




class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color('red')
        self.speed(0)
        self.food_coords = random.choice(POSSIBLE_FOOD_COORDS)
        self.goto(self.food_coords)

    def refresh(self):
        self.food_coords = random.choice(POSSIBLE_FOOD_COORDS)
        self.goto(self.food_coords)
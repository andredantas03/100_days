import random
from turtle import Turtle
import itertools

#List of all possible entry's food
x1 = [list(range(-280, 290, 20)),list(range(-280, 290, 20))]
x1 = list(itertools.product(*x1))

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color('red')
        self.speed(0)
        self.possible_food_pos = x1.copy()
        self.food_coords = random.choice(x1)
        self.goto(self.food_coords)

    def refresh(self,snake):
        #Remove from possible food's location the body position of all snake parts
        for square in snake.snake_body:
            x,y = tuple(square.pos())
            pos = (round(x,0),round(y,0))
            self.possible_food_pos.remove(pos)
        self.food_coords = random.choice(x1)
        self.goto(self.food_coords)
        self.possible_food_pos = x1.copy()

from turtle import Turtle

WIDTH = 20
HEIGHT = 100


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        self.goto(x = self.pos()[0], y = self.pos()[1]+20)
    def down(self):
        self.goto(x = self.pos()[0], y = self.pos()[1]-20)
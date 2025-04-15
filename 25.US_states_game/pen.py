from turtle import Turtle

FONT = ("Times", 12, "normal")
class Pen(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
    def write(self, arg, move = False, align = "left", font = FONT):
        super().write(arg)
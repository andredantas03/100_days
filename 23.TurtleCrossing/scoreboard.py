from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.hideturtle()
        self.goto(-280,260)
        self.update_score()

    def score_up(self):
        self.level+=1
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

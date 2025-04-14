from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.teleport(x=0,y=260)
        self.color("white")
        self.score = 0
        self.high_score = self.read_file()
        self.update_scoreboard()
        self.hideturtle()

    def read_file(self):
        with open("high_score.txt", mode="r") as file:
            high_score = file.read()
            return int(high_score)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.read_file()}",align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            with open("high_score.txt",mode="w") as file:
                file.write(str(self.score))
        self.score=0
        self.update_scoreboard()

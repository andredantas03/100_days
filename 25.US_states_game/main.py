import turtle
import pandas as pd
from pen import Pen
from scoreboard import Scoreboard

#Building screen
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Building game's logic
game_on = True
data = pd.read_csv("50_states.csv")
data.set_index("state",inplace=True)

#Make a pen to write states name
pen = Pen()
score = Scoreboard()

for answer in score.right_answers:
    x, y = data.loc[answer]
    pen.goto(x, y)
    pen.write(answer)

while game_on:

    answer = screen.textinput(f"{score.score}/50 States Correct",
                          "Whats the state name? ", ).capitalize()
    if answer in data.index:
        x,y = data.loc[answer]
        pen.goto(x,y)
        pen.write(answer)
        score.add_state(answer)
        data.drop(answer, inplace=True)
    if answer == None:
        score.save_file()
        turtle.bye()




turtle.mainloop()
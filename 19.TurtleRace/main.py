import random
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(width=800,height=600)
screen.title("Welcome to the turtle race!")

user_bet = screen.textinput(title="Make your bet!",prompt="Which Turtle will win the reace? Enter a color:")
colors = ["red", "blue", "orange", "green", "pink", "brown"]
y_positions = [-70,-40,-10,20,50,80]
all_turtles = []
inicial_x = -230
final_x = 230

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.teleport(x=-230,y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
else:
    is_race_on = False

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if winner == user_bet:
                print("You Win!!!")
                is_race_on=False
            else:
                print("you loose!")
                is_race_on=False
        rand_distance = random.randint(0,10)
        turtle.fd(rand_distance)



screen.exitonclick()
import colorgram
from turtle import colormode, Turtle, Screen
from random import choice,seed

seed(1) #Setting seed to reproduce results
colormode(255) #Setting colormode to use integers as colors

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

#Using a dictionary to customize the result
parameters = {
    "circle_diam" : 50,
    "space_between" : 1,
    "num_dots_horiz" : 10,
    "num_dots_vert" : 10
}
#The center is the (0,0) position, so it needs to define the inicial and the final position
#to do what the teacher said
inicial_pos = ( -(parameters['num_dots_horiz'] * (parameters['circle_diam']+parameters['space_between']))/2,
                -(parameters['num_dots_vert'] * (parameters['circle_diam']+parameters['space_between']))/2
                )
final_pos = ( (parameters['num_dots_horiz'] * (parameters['circle_diam']+parameters['space_between']))/2,
                (parameters['num_dots_vert'] * (parameters['circle_diam']+parameters['space_between']))/2
                )

tart = Turtle()
tart.speed(0) #highest speed

for j in range(parameters['num_dots_vert']):
    tart.teleport(x=inicial_pos[0],y=inicial_pos[1]+j*(parameters["circle_diam"]+parameters["space_between"]))
    for i in range(parameters['num_dots_horiz']):
        tart.dot(parameters["circle_diam"], choice(rgb_colors))
        tart.teleport(x = tart.pos()[0]+parameters["circle_diam"]+parameters["space_between"])

tart.ht() #Hidding turtle

screen = Screen()
screen.exitonclick()
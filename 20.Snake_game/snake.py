from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (20,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 0
RIGHT = 180

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.adding_squares(position)

    def move(self):
        for square in range(len(self.snake_body) - 1, 0, -1):
            position = (self.snake_body[square - 1].xcor(),self.snake_body[square - 1].ycor())
            self.snake_body[square].goto(position)
        self.head.fd(MOVE_DISTANCE)

    def adding_squares(self,position):
        square = Turtle()
        square.shape("square")
        square.color("white")
        square.penup()
        square.teleport(x=position[0],y=position[1])
        self.snake_body.append(square)

    def food_found(self):
        self.adding_squares(self.snake_body[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


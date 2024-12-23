from turtle import Turtle

MOVE_DISTANCE = 50


class Paddle(Turtle):
    def __init__(self, x_co, y_co):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.x_co= x_co
        self.y_co= y_co
        self.goto(self.x_co, self.y_co)

    def move_up(self):
        self.y_co+=MOVE_DISTANCE
        self.goto(self.x_co, self.y_co)
    def move_down(self):
        self.y_co-=MOVE_DISTANCE
        self.goto(self.x_co, self.y_co)
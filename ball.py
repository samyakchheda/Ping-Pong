from turtle import Turtle
import time

class  Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(0,0)
        self.penup()
        self.move_x=10
        self.move_y = 10

    def move(self):
        new_x=self.xcor()+self.move_x
        new_y=self.ycor()+self.move_y
        self.goto(new_x,new_y)


    def bounce_y(self):
        self.move_y*=-1

    def bounce_x(self):
        self.move_x*=-1

    def miss(self):
        self.goto(0,0)
        self.move_x*=-1
        time.sleep(1)


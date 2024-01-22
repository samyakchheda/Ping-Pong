from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(1, 5)
        self.speed("fastest")
        self.penup()
        self.goto(position, 0)
        self.setheading(90)

    def up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(), new_y)



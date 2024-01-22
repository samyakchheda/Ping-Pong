from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
ball=Ball()
scoreboard=Scoreboard()
screen = Screen()
screen.tracer(0)
screen.setup(height=600,width=1200)
screen.bgcolor("black")
screen.title("Ping Pong")
paddle_l=Paddle(-580)
paddle_r=Paddle(570)

screen.listen()
screen.onkeypress(paddle_r.up,"Up")
screen.onkeypress(paddle_r.down,"Down")
screen.onkeypress(paddle_l.up,"w")
screen.onkeypress(paddle_l.down,"s")
game_is_on=True
time1=0.03
i=0
while game_is_on:
    time.sleep(time1)
    screen.update()
    ball.move()

    if ball.ycor()>285 or ball.ycor()<-285:
        ball.bounce_y()
        i=0

    # elif ball.distance(paddle_r)<40 and ball.xcor()>320 :
    #     ball.bounce_x()
    # elif ball.distance(paddle_l)<40 and ball.xcor()<-320:
    #     ball.bounce_x()

    if ball.xcor()>=550 and ball.distance(paddle_r)<20 and (ball.ycor()<=paddle_r.ycor() or ball.ycor()>=paddle_r.ycor()) or ball.xcor()<=-560 and ball.distance(paddle_l)<20 and (ball.ycor()<=paddle_l.ycor() or ball.ycor()>=paddle_l.ycor()) :
        if i==0:
            ball.bounce_x()
            time1*=0.9
            i+=1
    elif ball.xcor()>610 :
        ball.miss()
        scoreboard.l_point()
        time1=0.03
    elif ball.xcor()<-610:
        ball.miss()
        scoreboard.r_point()
        time1=0.03





screen.exitonclick()
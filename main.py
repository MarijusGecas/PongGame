from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    if ball.distance(r_paddle) <50 and ball.xcor() > 320 or ball.distance(l_paddle) <50 and ball.xcor() < -320:
        ball.bounce_paddle()

    if ball.xcor() > 380 :
        ball.out_of_bound()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.out_of_bound()
        scoreboard.r_point()

screen.exitonclick()
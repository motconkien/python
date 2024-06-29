from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


#setup screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Ping pong game")
screen.bgcolor("black")
screen.tracer(0) #turn off animation

r_pad = Paddle((350,0))
l_pad = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_pad.go_up, "Up")
screen.onkey(r_pad.go_down,"Down")
screen.onkey(l_pad.go_up,"w")
screen.onkey(l_pad.go_down,"s")


is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(r_pad) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(l_pad) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_point()

screen.exitonclick()
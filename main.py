import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.movement()
    ball.bounce()
    scoreboard.update_scoreboard()

    if ball.xcor() > 320 and ball.distance(r_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 340:
        ball.goto(0, 0)
        ball.x_move *= -1
        ball.y_move *= 1
        scoreboard.l_point()
        ball.move_speed = 0.1

    if ball.xcor() < -340:
        ball.goto(0, 0)
        ball.x_move *= -1
        ball.y_move *= 1
        scoreboard.r_point()
        ball.move_speed = 0.1


screen.exitonclick()
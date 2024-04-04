from turtle import Turtle, Screen
from Padle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.tracer(0)
scoreboard = ScoreBoard()

screen.setup(width=1000, height=600)
screen.bgcolor('black')
screen.title('PING PONG GAME')

paddle_l = Paddle(-490 , 0)
paddle_r = Paddle(480, 0)
ball = Ball()


screen.listen()
screen.onkeypress(paddle_r.go_up, 'Up')
screen.onkeypress(paddle_r.go_down, 'Down')
screen.onkeypress(paddle_l.go_up, 'w')
screen.onkeypress(paddle_l.go_down, 's')


game_over = False
while not game_over:
    time.sleep(ball.move_speed)
    
    screen.update()
    ball.move()


    # detect a collisiion with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # detect a collision with a paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() == 450 or ball.distance(paddle_l) < 50 and ball.xcor() == -470:
        ball.detect_paddle()
    

    # detect right paddle miss the ball
    if ball.xcor() > 500:
        ball.reset_position()
        scoreboard.l_point()

    # detect left  paddle miss the ball
    if ball.xcor() < -500:
        ball.reset_position()
        scoreboard.r_point()






screen.exitonclick()
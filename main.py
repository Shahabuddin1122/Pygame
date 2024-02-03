import turtle as t
PlayerAScore = 0
PlayerBScore = 0

window = t.Screen()
window.title("Pong Game")
window.bgcolor('black')
window.setup(width=800,height=600)
window.tracer(0)


leftPaddle=t.Turtle()
leftPaddle.speed(0)
leftPaddle.shape("square")
leftPaddle.color("white")
leftPaddle.shapesize(stretch_len=1,stretch_wid=5)
leftPaddle.penup()
leftPaddle.goto(-350,0)

RightPaddle=t.Turtle()
RightPaddle.speed(0)
RightPaddle.shape("square")
RightPaddle.color("white")
RightPaddle.shapesize(stretch_len=1,stretch_wid=5)
RightPaddle.penup()
RightPaddle.goto(350,0)

ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5,5)
ballXdirection = 0.2
ballYdirection = 0.2

pen=t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score",align="center",font=('Arial',24,'normal'))


#moving the leftpaddle

def leftpaddleup():
    y=leftPaddle.ycor()
    y=y+90
    leftPaddle.sety(y)


def leftpaddledown():
    y=leftPaddle.ycor()
    y=y-90
    leftPaddle.sety(y)

#moving rightpaddle

def rightpaddleup():
    y=RightPaddle.ycor()
    y=y+90
    RightPaddle.sety(y)


def rightpaddledown():
    y=RightPaddle.ycor()
    y=y-90
    RightPaddle.sety(y)


#key

window.listen()
window.onkeypress(leftpaddleup,'w')
window.onkeypress(leftpaddledown,'s')
window.onkeypress(rightpaddleup,'Up')
window.onkeypress(rightpaddledown,'Down')

while True:
    window.update()

    #moving the ball
    ball.setx(ball.xcor()+ballXdirection)
    ball.sety(ball.ycor()+ballYdirection)

    #settingup border
    if ball.ycor()>290:
        ball.sety(290)
        ballYdirection=ballYdirection*-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ballYdirection=ballYdirection*-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ballXdirection=ballXdirection
        PlayerAScore = PlayerAScore
        pen.clear()
        pen.write("player A:{}    Player B:{}".format(PlayerAScore,PlayerBScore),align='center',font=('Arial',24,'normal'))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ballXdirection=ballXdirection*-1
        PlayerBScore = PlayerBScore+1
        pen.clear()
        pen.write("player A:{}    Player B:{}".format(PlayerAScore,PlayerBScore),align='center',font=('Arial',24,'normal'))

    #handling collisions

    if ( ball.xcor()>340)and (ball.xcor()<350)and(ball.ycor()<RightPaddle.ycor()+40 and ball.ycor()>RightPaddle.ycor()-40):
        ball.setx(340)
        ballXdirection=ballXdirection*-1

    if ( ball.xcor()<-340)and(ball.xcor()<-350)and(ball.ycor()<leftPaddle.ycor()+40 and ball.ycor()>leftPaddle.ycor()-40):
        ball.setx(-340)
        ballXdirection=ballXdirection*-1


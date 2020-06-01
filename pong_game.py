import turtle
import random
import winsound
import sys
 #window
wn = turtle.Screen()
wn.title("pong")
wn.setup(width = 680 ,height = 600)
wn.bgcolor("black")
wn.bgpic("bg.gif")
wn.tracer(0)
winsound.PlaySound("Marimba Boy.wav", winsound.SND_ASYNC + winsound.SND_LOOP)

#main menu
menu = turtle.Turtle()
menu.speed(0)
menu.shape("circle")
menu.color("green")
menu.shapesize(stretch_wid = 1.2, stretch_len = 1.2)
menu.penup()
menu.goto(0 , 200)
menu.write("START GAME", align = "center", font = ("algerian",35,"bold"))
menu.hideturtle()

menu2 = turtle.Turtle()
menu2.speed(0)
menu2.shape("circle")
menu2.color("green")
menu2.shapesize(stretch_wid = 1.2, stretch_len = 1.2)
menu2.penup()
menu2.goto(0 , -250)
menu2.write("OUIT GAME", align = "center", font = ("algerian",35,"bold"))
menu2.hideturtle()

def start_game():
    wn.clear()
     #window
    wn2 = turtle.Screen()
    wn2.title("pong")
    wn2.setup(width = 680 ,height = 600)
    wn2.bgcolor("black")
    wn2.bgpic("bg.gif")
    wn2.tracer(0)


    winsound.PlaySound("Off Limits.wav", winsound.SND_ASYNC + winsound.SND_LOOP)


    #score
    score_a = 0
    score_b = 0

    #paddle A
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("green")
    paddle_a.shapesize(stretch_wid = 7, stretch_len = 1)
    paddle_a.penup()
    paddle_a.goto(-290 , 0)

    #paddle B
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("green")
    paddle_b.shapesize(stretch_wid = 7, stretch_len = 1)
    paddle_b.penup()
    paddle_b.goto(280 , 0)

    #ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("green")
    ball.shapesize(stretch_wid = 1.2, stretch_len = 1.2)
    ball.penup()
    ball.goto(0 , 0)
    ball.dx = 0.3
    ball.dy = 0.3

    #score display
    score = turtle.Turtle()
    score.speed(0)
    score.shape("circle")
    score.color("green")
    score.shapesize(stretch_wid = 1.2, stretch_len = 1.2)
    score.penup()
    score.goto(0 , 250)
    score.write("PLAYER A: 0  PLAYER B: 0", align = "center", font = ("algerian",35,"bold"))
    score.hideturtle()


    #paddle movements
    def paddle_a_up():
        y = paddle_a.ycor()
        y += 20 
        paddle_a.sety(y)

    def paddle_b_up():
        y = paddle_b.ycor()
        y += 20 
        paddle_b.sety(y)

    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 20 
        paddle_a.sety(y)

    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 20 
        paddle_b.sety(y)

    def exit_game():
        sys.exit()

    #key bindings
    wn.listen()
    wn2.onkeypress(paddle_a_up, "w")
    wn2.onkeypress(paddle_b_up, "Up")
    wn2.onkeypress(paddle_b_down, "Down")
    wn2.onkeypress(paddle_a_down, "s")
    wn2.onkeypress(exit_game, "2")

    game_over = False

    #main game loop
    while not game_over:
        wn2.update()
        #ball movements
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)
        ball.tilt(30)

        #collison detection
        #ball and wall
        if ball.ycor() >= 300 or ball.ycor() <= -300 :
            ball.dy *= -1
            
        if ball.xcor() >= 340:
            score_a += 1
            score.clear()
            score.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("algerian", 35, "bold"))
            ball.goto(0,0)
            ball.dx *= -1

        if ball.xcor() <= -340:
            score_b += 1
            score.clear()
            score.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("algerian", 35, "bold"))
            ball.goto(0,0)
            ball.dx *= -1

        if ball.xcor() - 20 <= paddle_a.xcor() and ball.ycor() < paddle_a.ycor() + 70 and ball.ycor() > paddle_a.ycor() - 70:
            ball.dx *= -1 
            #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        
        elif ball.xcor() + 20 >= paddle_b.xcor() and ball.ycor() < paddle_b.ycor() + 70 and ball.ycor() > paddle_b.ycor() - 70:
            ball.dx *= -1
            #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) 
           

            

wn.listen()
wn.onkeypress(start_game, "w")


while True:
    wn.update()

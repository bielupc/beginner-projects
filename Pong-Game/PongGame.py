import turtle
import winsound
import pyautogui, sys
import pygame

pygame.init()

button1 = turtle.Turtle()
button2 = turtle.Turtle()
button3 = turtle.Turtle()
button4 = turtle.Turtle()

# Screen
wn = turtle.Screen()
wn.title("PONG")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.color("white")
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("square")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = -0.25

# score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 | Player B: 0", align="center", font="Impact", )


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


def play_but():
    pen.goto(-223, -167)
    pen.pencolor("black")
    pen.write("PLAY", font=("impact", 20))


def quit_but():
    pen.pencolor("black")
    pen.goto(180, -167)
    pen.write("QUIT", font=("impact", 20))


def play_again():
    pen.pencolor("black")
    pen.goto(-270, -167)
    pen.write("PLAY AGAIN", font=("impact", 18))


def quit_2but():
    pen.pencolor("black")
    pen.goto(180, -167)
    pen.write("QUIT", font=("impact", 20))


def xd(x, y):
    button1.hideturtle()
    button2.hideturtle()
    game()


def xd2(x, y):
    wn.exitonclick()


# Keys
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Pre game loop
def game_intro():
    intro = True
    pen.clear()
    pen.goto(0, 0)
    pen.pencolor("white")
    pen.write("PONG", align="center", font=("impact", 100,))
    pen.goto(250, -290)
    pen.write("Biel Altimira", font=("impact", 20,))

    while intro:
        button1.showturtle()
        button2.showturtle()
        paddle_b.hideturtle()
        paddle_a.hideturtle()
        ball.hideturtle()
        play_but()
        quit_but()
        wn.listen()

        x, y = pyautogui.position()

        if x in range(700, 842) and y in range(695, 756):
            button1.goto(-200, -150)
            button1.shape("square")
            button1.color("grey")
            button1.shapesize(stretch_wid=3, stretch_len=7)
            wn.onclick(xd)
        else:
            button1.goto(-200, -150)
            button1.shape("square")
            button1.color("white")
            button1.shapesize(stretch_wid=3, stretch_len=7)

        if x in range(1100, 1243) and y in range(695, 756):
            button2.goto(200, -150)
            button2.shape("square")
            button2.color("grey")
            button2.shapesize(stretch_wid=3, stretch_len=7)
            wn.onclick(xd2)
        else:
            button2.goto(200, -150)
            button2.shape("square")
            button2.color("white")
            button2.shapesize(stretch_wid=3, stretch_len=7)
        wn.update()


# Main loop
def game(score_a=0, score_b=0, winner=0):
    pen.clear()
    pen.goto(0, 250)
    pen.pencolor("white")
    pen.write(f"Player A: {score_a} | Player B: {score_b}", align="center", font=("Impact", 20))
    button3.hideturtle()
    button4.hideturtle()
    while True:
        wn.update()
        paddle_b.showturtle()
        paddle_a.showturtle()
        ball.showturtle()
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)


        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write(f"Player A: {score_a} | Player B: {score_b}", align="center", font=("Impact", 20))
            winsound.PlaySound("coin.wav", winsound.SND_ASYNC)

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write(f"Player A: {score_a} | Player B: {score_b}", align="center", font=("Impact", 20))
            winsound.PlaySound("coin.wav", winsound.SND_ASYNC)

        if ball.xcor() < -340 and paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50:
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if ball.xcor() > 340 and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50:
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        if score_a == 1:
            winsound.PlaySound("correct.m4a", winsound.SND_ASYNC)
            button3.showturtle()
            button4.showturtle()
            winner = "PLAYER A WON!"
            paddle_a.hideturtle()
            paddle_b.hideturtle()
            ball.hideturtle()
            pen.goto(0, 0)
            pen.pencolor("white")
            pen.write(f"CONGRATULATIONS, {winner}", align="Center", font=("impact", 30))
            button3.goto(-200, -150)
            button3.shape("square")
            button3.color("white")
            button3.shapesize(stretch_wid=3, stretch_len=7)
            quit_2but()
            button4.goto(200, -150)
            button4.shape("square")
            button4.color("white")
            button4.shapesize(stretch_wid=3, stretch_len=7)
            play_again()

        if score_b == 2:
            button4.showturtle()
            button3.showturtle()
            winsound.PlaySound("correct.m4a", winsound.SND_ASYNC)
            winner = "PLAYER B WON!"
            paddle_a.hideturtle()
            paddle_b.hideturtle()
            ball.hideturtle()
            pen.pencolor("white")
            pen.goto(0, 0)
            pen.write(f"CONGRATULATIONS, {winner}", align="Center", font=("impact", 30))
            button3.goto(-200, -150)
            button3.shape("square")
            button3.color("white")
            button3.shapesize(stretch_wid=3, stretch_len=7)
            quit_2but()
            button4.goto(200, -150)
            button4.shape("square")
            button4.color("white")
            button4.shapesize(stretch_wid=3, stretch_len=7)
            play_again()


game_intro()


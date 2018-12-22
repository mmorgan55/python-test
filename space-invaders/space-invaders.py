import turtle
import time
import os

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("SPACE INVADERS")

# Create screen for playing
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("green")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(4)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Create basic player
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

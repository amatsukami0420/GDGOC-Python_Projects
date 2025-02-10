import turtle
import math

def heart(k):
    return 15 * math.sin(k)**3

def heart1(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# Set up the turtle
turtle.speed(0)
turtle.bgcolor('black')
turtle.color('pink')
turtle.penup()
turtle.hideturtle()

# Draw the heart shape
for i in range(6000):
    x = heart(i / 100) * 20
    y = heart1(i / 100) * 20
    turtle.goto(x, y)
    turtle.pendown()

turtle.done()
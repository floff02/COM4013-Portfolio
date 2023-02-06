import turtle
import random

x = 0
y = 0
dx = 0
dy = 0

def setup():
    
    global x, y, dx, dy
    turtle.title("Classic DVD Screen Saver")
    turtle.setup(800, 600)
    turtle.bgcolor("black")
    turtle.penup()
    x = random.randint(-400, 400)
    y = random.randint(-300, 300)
    dx = random.uniform(0.5, 2.5)
    dy = random.uniform(0.5, 2.5)

def draw():
    global x, y, dx, dy
    turtle.clear()
    turtle.color("white")
    turtle.goto(x, y)
    turtle.write("DVD", align="center", font=("Arial", 36, "normal"))
    x += dx
    y += dy
    if x > 400 or x < -400:
        dx = -dx
    if y > 300 or y < -300:
        dy = -dy
    turtle.ontimer(draw, 1)

setup()
draw()
turtle.done()
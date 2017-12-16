import turtle
import time

def drawing_turtles():
    window = turtle.Screen()
    window.bgcolor("black")

    brad()
    jon()
    time.sleep(2)

    window.exitonclick()

def brad():
    brad = turtle.Turtle()
    brad.color("green")
    brad.speed(2)
    for i in range(0, 8):
        brad.forward(100)
        brad.right(45)

def jon():
    jon = turtle.Turtle()
    jon.color("pink")
    jon.shape("arrow")

    jon.circle(100)


drawing_turtles()

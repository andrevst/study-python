import turtle
import time

def drawing_turtles():
    window = turtle.Screen()
    window.bgcolor("black")

    brad()
    jon()
    bjorn()

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
    jon.speed(3)
    jon.circle(100)

def bjorn():
    bjorn = turtle.Turtle()
    bjorn.color("red")
    bjorn.speed(4)
    bjorn.forward(200)
    bjorn.left(60)
    bjorn.backward(200)
    bjorn.left(60)
    bjorn.forward(200)

drawing_turtles()

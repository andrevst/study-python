import turtle
import time

def draw_square():
    window = turtle.Screen()
    window.bgcolor("black")

    time.sleep(2)

    brad = turtle.Turtle()
    brad.color("green")
    brad.speed(2)
    brad.forward(100)
    brad.right(45)
    brad.forward(100)
    brad.right(45)
    brad.forward(100)
    brad.right(45)
    brad.forward(100)
    brad.right(45)
    brad.forward(100)
    brad.right(45)
    brad.forward(100)
    brad.right(45)
    brad.forward(100)
    brad.right(45)
    brad.forward(100)
    brad.right(45)

    jon = turtle.Turtle()
    jon.color("pink")
    jon.shape("arrow")

    jon.circle(100)

    window.exitonclick()

draw_square()

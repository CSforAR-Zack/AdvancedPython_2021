from turtle import Turtle, Screen
from random import randint

def main():
    t = Turtle()
    s = Screen()

    s.tracer(0)
    s.bgcolor('black')
    t.speed(0)
    t.penup()

    colors: list = ['hotpink', 'orange', 'cyan']

    for dot in range(1000):
        x = randint(-500, 500)
        y = randint(-500, 500)
        t.goto(x, y)
        size = randint(10, 75)

        if x < -167 and y > 167:
            t.dot(size, colors[0])
        elif x > 167:
            t.dot(size, colors[2])
        else:
            t.dot(size, colors[1])

    s.mainloop()

main()

from turtle import Turtle, Screen
from time import sleep

t = Turtle()
t2 = Turtle()
s = Screen()

movement = 10
direction = -1
distance = 0
distanceMax = 500
speedFactor = 0.05

t.hideturtle()
t2.hideturtle()
t.speed(0)
t2.speed(0)
s.tracer(0)
t.left(90)
t2.backward(200)
t2.left(90)
s.bgcolor("black")

while True:
    t.clear()
    t2.clear()
    t.forward(movement * direction)
    t2.forward(movement * direction * 1.5)
    distance += movement
    t.dot(100, "cyan")
    t2.dot(75, "orange")
    if distance > distanceMax:
        direction = -direction
        distance = 0
    s.update()
    sleep(speedFactor)

s.mainloop()

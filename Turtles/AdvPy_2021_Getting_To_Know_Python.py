from turtle import Turtle, Screen

# Creating Turtle and Screen
t: Turtle = Turtle()
s: Screen = Screen()

#sideLength: int = int(input('Give me a sidelength: '))
sideLength: int = s.numinput('Input Window', 'Give me a num:')

# Draw square
sideNum: int = 0

while sideNum < 4:
    t.forward(sideLength)
    t.right(90)
    sideNum += 1

t.right(180)

for side in range(4):
    t.forward(sideLength)
    t.left(90)
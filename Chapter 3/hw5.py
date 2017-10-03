import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess=turtle.Turtle()
tess.shape("turtle")
tess.color("blue")
tess.stamp()

for i in range(12):
    tess.penup()
    tess.forward(100)
    tess.pendown()
    tess.forward(10)
    tess.penup()
    tess.forward(10)
    tess.stamp()
    tess.backward(120)
    tess.left(30)
    
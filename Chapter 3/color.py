import turtle
wn = turtle.Screen()

alex = turtle.Turtle()
colors = ["red","orange","green","yellow"]
for i in colors:
    print(i)
    alex.color(i)
    alex.forward(100)
    alex.left(100)
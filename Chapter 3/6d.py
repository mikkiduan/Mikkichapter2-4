import turtle
wn=turtle.Screen()
owen=turtle.Turtle()
sides=int(input("how many sides?"))
lenth=int(input("how long is each sides?"))
for i in range(sides):
    owen.forward(lenth)
    owen.left(360/sides)
import turtle

obj=turtle.Turtle()

obj.speed(1)

window=turtle.Screen()
window.bgcolor("black")

obj.goto(0,-100)
obj.pensize(5)

obj.color("red")
obj.fillcolor("red")
obj.left(140)
obj.forward(180)
obj.circle(-90,200)

obj.setheading(60)
obj.circle(-90,200)
obj.forward(176)
obj.end_fill()




turtle.done()



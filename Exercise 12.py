# Write a program that draws four squares in the center
# of the screen, as shown in Figure 1.18a.
# Figure 1.18a is shown on pg. 28 in the textbook.


import turtle

turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(150)

turtle.penup()
turtle.goto( 0, 0)

turtle.pendown()
turtle.forward(150)

turtle.penup()
turtle.goto( 0, 0)
turtle.left(90)
turtle.pendown()

turtle.forward(150)

turtle.penup()
turtle.goto( 0, 0)

turtle.left(90)
turtle.pendown()
turtle.forward(150)

turtle.penup()
turtle.goto(0,0)





turtle.done()
# File: SeychellesFlag.py
# Student: Gaytri Riya Vasal
# UT EID: grv377
# Course Name: CS303E
# 
# Date Created: 11/22/2021
# Date Last Modified: 11/23/2021
# Description of Program: The following program will render a picture of the Seychelles Flag.

import turtle

def drawtriangle (turtle, x1, y1, x2, y2, x3, y3):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.setheading (0)
    turtle.pendown ()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.setheading (90)
    turtle.goto(x1, y1)

def drawquadrilateral (turtle, x1, y1, x2, y2, x3, y3, x4, y4):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.setheading (0)
    turtle.pendown ()
    turtle.goto(x2, y2)
    turtle.setheading (90)
    turtle.goto(x3, y3)
    turtle.goto(x4, y4)
    turtle.goto(x1, y1)

def drawtriangle2 (turtle, x1, y1, x2, y2, x3, y3):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.setheading (270)
    turtle.pendown ()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x1, y1)
    
myBlue = "#003D88"
myYellow = "#FCD955"
myRed = "#D72323"
myWhite = "#FFFFFF"
myGreen = "#007B3A"

turtle = turtle.Turtle()

turtle.fillcolor(myBlue)
turtle.begin_fill ()
drawtriangle(turtle, 0, 300, 200, 300, 0, 0)
turtle.end_fill ()

turtle.fillcolor(myYellow)
turtle.begin_fill ()
drawtriangle(turtle, 200, 300, 400, 300, 0, 0)
turtle.end_fill ()

turtle.fillcolor(myRed)
turtle.begin_fill ()
drawquadrilateral(turtle, 400, 300, 600, 300, 600, 200, 0, 0)
turtle.end_fill ()

turtle.fillcolor(myWhite)
turtle.begin_fill ()
drawtriangle2(turtle, 600, 200, 600, 100, 0, 0)
turtle.end_fill ()

turtle.fillcolor(myGreen)
turtle.begin_fill ()
drawtriangle2(turtle, 600, 100, 600, 0, 0, 0)
turtle.end_fill ()

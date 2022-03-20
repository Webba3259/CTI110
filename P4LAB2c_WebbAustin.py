# snowflake
    # Date 3/20/2022
    # CTI-110 P4LAB2c:snowflake
    # Webb Austin
    #        
import turtle                   

wn = turtle.Screen()                #playground
wn.bgcolor("lightBlue")             #blue
wn.title("Good morning!")           #window title

alice = turtle.Turtle()             #alice in wonderland = snowflake?
alice.color("white")                #snow is white
alice.pensize(3)                    #line width?
alice.speed(0)                      #zoom
alice.shape("turtle")               #turtles are cute
alice.penup()                       #relocate the turtle (could be illegal)
alice.forward(30)
alice.backward(30)
alice.left(45)
alice.pendown()                     #leaving the turtle

def branch():
    for i in range(3):
        for i in range(3):
            alice.forward(30)
            alice.back(30)
            alice.right(45)
        alice.left(90)
        alice.back(30)
        alice.left(45)
    alice.right(90)
    alice.forward(90)

for i in range(8):
    branch()
    alice.left(45)

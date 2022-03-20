# shapes
    # Date 3/20/2022
    # CTI-110 P3LAB2b:initials
    # Webb Austin
    #        
import turtle                   

wn = turtle.Screen()                #playground
wn.bgcolor("lightBlue")             #blue
wn.title("Good morning!")           #window title

alice = turtle.Turtle()             #alice in wonderland
alice.color("yellow")               #yellow?
alice.pensize(3)                    #line width?
alice.speed(0)                      #zoom
alice.shape("turtle")               #turtles are cute
alice.penup()                       #relocate the turtle (could be illegal)
alice.goto(-200, 200)               #new turtle home
alice.pendown()                     #leaving the turtle


ethos = turtle.Turtle()             #second turtle so first isn't lonely
ethos.color("blue")                 #different turtle different color
ethos.pensize(3)                    #same width
ethos.speed(0)                      #ZOOM
ethos.shape("turtle")               #turtles are still cute
ethos.penup()                       #turtle needs new home
ethos.goto(0, 200)                  #found new home
ethos.pendown()                     #leave turtle


alice.left(60)                  #this Draws an a
alice.forward(100)
alice.right(120)
alice.forward(100)
alice.back(50)
alice.right(120)
alice.forward(50)
alice.penup()
alice.goto(-270, 200)

ethos.left(130)                 #this draws a akward W
ethos.forward(100)
ethos.back(100)
ethos.right(70)
ethos.forward(50)
ethos.right(100)
ethos.forward(50)
ethos.left(100)
ethos.forward(100)
ethos.right(55)
                                #this brings the turtles together so they aren't lonely
ethos.penup()
ethos.goto(-300, 200)





wn.exitonclick()                #this closes the window when you click on it =)

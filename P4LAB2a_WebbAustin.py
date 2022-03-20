import turtle                   

wn = turtle.Screen()                #playground? okay this opened the graphic
wn.bgcolor("pink")                  #background color
wn.title("Good morning!")           #window title

alice = turtle.Turtle()             #i named my turtle Alice
alice.color("yellow")                #turtle color,
alice.pensize(3)                    #line width?
alice.speed(0)                      #i saw a video that made this go zoom?
alice.shape("turtle")               #turtles are cute
alice.penup()                       #make the turtle go somewhere else
alice.goto(-200, -200)              #location
alice.pendown()                     #remember to put pen down


ethos = turtle.Turtle()             #second turtle for second shape
ethos.color("blue")                 #this one is blue
ethos.pensize(3)                    #same width
ethos.speed(0)                      #ZOOM
ethos.shape("turtle")               #turtles are still cute

for i in [0, 1, 2, 3]:              #this draws a square
    alice.forward(50)               #distance traveled
    alice.left(90)                  #angle
    ethos.forward(50)
    ethos.left(120)

wn.exitonclick()

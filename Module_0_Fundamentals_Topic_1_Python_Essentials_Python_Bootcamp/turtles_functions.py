#corey b. holstege
#2018-08-23
#http://interactivepython.org/runestone/static/thinkcspy/Functions/functions.html

#import modules
import turtle

#create a function
def drawSquare(t, sz):
	"""Make turtle t draw a square of width side sz."""
	
	for i in range (4):
		t.forward(sz)
		t.left(90)

#set up the window
wn = turtle.Screen()
wn.bgcolor('lightgreen')

#create alex
alex = turtle.Turtle()

#draw a square
drawSquare(alex, 50)

#move alex
alex.penup()
alex.goto(100,100)
alex.pendown()

#draw a square
drawSquare(alex, 50)

#exit window
wn.exitonclick()
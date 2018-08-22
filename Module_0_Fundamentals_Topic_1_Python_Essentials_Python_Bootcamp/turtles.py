# corey b. holstege
# 2018-08-22
# http://interactivepython.org/runestone/static/thinkcspy/PythonTurtle/OurFirstTurtleProgram.html

import turtle				# allows us to use the turtles library

background_color = input("What color background do you desire?")
tess_color = input("What color should Tess the Turtle be?")
tess_pensize = input("How big should Tess' tail be?")

wn = turtle.Screen()		# creates a graphics window
#wn.bgcolor("lightgreen")	# set the background color
wn.bgcolor(background_color)

alex = turtle.Turtle()		# create a turtle named alex
alex.color("red")			# set the color of alex to red
alex.pensize(3)				# set the width of alex's line
alex.shape("turtle")		#arrow, blank, circle, classic, square, triangle, turtle
alex.speed(5)				#1(slowest) to 10(fastest)

tess = turtle.Turtle()		# create a turtle named tess
#tess.color("blue")			# set the color of tess to blue
tess.color(tess_color)
#tess.pensize(3)			# set the width of tess's line
tess.pensize(int(tess_pensize))
tess.shape("turtle")
tess.speed(1)				#1(slowest) to 10(fastest)

jose = turtle.Turtle()
jose.shape("turtle")

#make alex move (inefficient method)
#alex.forward(200)			# tell alex to move forward by 200 units
#alex.left(90)				# tell alex to turn by 90 degrees
#alex.forward(200)			# tell alex to move forward by 200 units
#alex.left(90)				# tell alex to turn by 90 degrees
#alex.forward(200)			# tell alex to move forward by 200 units
#alex.left(90)				# tell alex to turn by 90 degrees
#alex.forward(200)			# tell alex to move forward by 200 units
#alex.left(90)				# tell alex to turn by 90 degrees

#make alex move (more efficient method)
#for i in [0,1,2,3]:
#	alex.forward(200)
#	alex.left(90)

#make alex move (even more efficiently)	
for i in range(4):
	alex.forward(200)
	alex.left(90)

#make alex create a second square
for i in range (4):
	alex.forward(50)
	alex.right(90)
	
#make alex move more efficiently with colored lines
#for acolor in ['yellow','red','purple','blue']:
#	alex.color(acolor)
#	alex.forward(200)
#	alex.left(90)

#moves alex but no line is drawn
#alex.up()
#alex.forward(100)
#alex.down()

tess.up()
for size in range (5, 60, 2):	#start with size 5 and grow by 2
	tess.stamp()				#leave an impression on the canvas
	tess.forward(size)			#move tess along
	tess.right(24)				#turn tess

jose.penup()
for size in range(10):
	jose.forward(50)
	jose.stamp()
	jose.forward(-50)
	jose.right(36)
	
wn.exitonclick()			# wait for user click on the canvas
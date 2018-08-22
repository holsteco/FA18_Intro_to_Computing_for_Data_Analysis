# corey b. holstege
# 2018-08-22
#http://interactivepython.org/runestone/static/thinkcspy/Labs/lab03_01.html
#https://docs.python.org/3/library/turtle.html

#import modules
import turtle
import random

#create screen
wn = turtle.Screen()
wn.bgcolor('lightblue')

#create lance and andy
lance = turtle.Turtle()
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

#move lance and andy to starting positions
andy.up()
lance.up()
andy.goto(-100,20)
lance.goto(-100,-20)

#race code
for turtle_race in range (100):
	andy.forward(random.randrange(1,5))
	lance.forward(random.randrange(1,5))

#exit screen
wn.exitonclick()
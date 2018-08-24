#corey b. holstege
#2018-08-24
#http://interactivepython.org/runestone/static/thinkcspy/Functions/mainfunction.html

import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""

    for i in range(4):
        t.forward(sz)
        t.left(90)


def main():                      # Define the main function
    wn = turtle.Screen()         # Set up the window and its attributes
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()       # create alex
    drawSquare(alex, 50)         # Call the function to draw the square

    wn.exitonclick()

if __name__ == "__main__":		# Invoke the main function
	main()                           
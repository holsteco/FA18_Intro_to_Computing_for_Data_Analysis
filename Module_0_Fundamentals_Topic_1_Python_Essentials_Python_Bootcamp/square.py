#corey b. holstege
#2018-08-23
#http://interactivepython.org/runestone/static/thinkcspy/Functions/TheAccumulatorPattern.html

def square(x):
    runningtotal = 0
    for counter in range(x):
        runningtotal = runningtotal + x

    return runningtotal

toSquare = 10
squareResult = square(toSquare)
print("The result of", toSquare, "squared is", squareResult)
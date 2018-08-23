#corey b. holstege
#2018-08-23
#http://interactivepython.org/runestone/static/thinkcspy/Functions/Functionscancallotherfunctions.html

def fnc_square(x):
	    y = x * x
	    return y
	
def fnc_sum_of_squares(x, y, z):
	    a = fnc_square(x)
	    b = fnc_square(y)
	    c = fnc_square(z)
	
	    return a + b + c
	
a = -5
b = 2
c = 10
result = fnc_sum_of_squares(a, b, c)
print(result)
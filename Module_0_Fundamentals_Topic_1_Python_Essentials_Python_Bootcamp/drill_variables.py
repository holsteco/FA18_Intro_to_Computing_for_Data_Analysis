# Assign the value 3 to the variable a. What is the type of a?
# How do you know the value of a?
print("--Q1--")
a = 3
print(type(a))
print(a)

# Assign the value 4 to the variable b.
print("--Q2--")
b = 4
print(b)

# Assign the result of dividing a by b to the variable d.
# What is the type of d?
print("--Q3--")
d = (a/b)
print(d)
print(type(d))

# Assign the result of dividing a by b to the variable e using *integer* division.
# What is the type of e?
print("--Q4--")
e = (a//b)
print(e)
print(type(e))

# Assign the result of calculating the remainder of a `div` b to the variable f,
# where `div` means integer division.
# Hint: this operation is known as `mod` or "modulus".
print("--Q5--")
f = (7%2)
print(f)
print(type(f))

# If the int values [0,7) (0, 1, 2, 3, 4, 5, 6) refer to Monday through Sunday,
# and today is Monday, what day of the week will it be in 999 days?
print("--Q6--")
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
todaysDate = 1
daysElapsed = 999
futureDay = ((todaysDate + daysElapsed) % 7)
print(days[futureDay])

# Assign the result of the sum a squared plus b squared to the variable c.
print("--Q7--")
c = (a**2)+(b**2)
print(c)
print(type(c))

# Assign the string value "foo" to the variable x.
print("--Q8--")
x = "foo"
print(x)
print(type(x))

# Assign the string value "fighter" to the variable y.
print("--Q9--")
y = "fighter"
print(y)
print(type(y))

# Assign the value of x + y to the variable z. What is the value of z?
print("--Q10--")
z = x + y
print(z)
print(type(z))

# Add 1 to z. What happens? --> error can't add int and str
print("--Q11--")
zz = z + 1
print(zz)
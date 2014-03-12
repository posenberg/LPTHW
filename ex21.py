def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a,b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

#A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"


age2 = subtract(40, 12)
height2 = add(-14, 90)
weight2 = divide(2014, 14)
iq2 = add(34, 28)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age2, height2, weight2, iq2)

stuff = subtract(age2, multiply(weight2, multiply(iq2, add(iq2, height2))))

print "This is: ", stuff, "."
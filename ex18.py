
def print_two(*args):
	#this one is like your scripts with argv
	# to use *args means you take all the arguments in a function as place them as a list.
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
	print "arg1: %r" % arg1

def print_none():
	print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
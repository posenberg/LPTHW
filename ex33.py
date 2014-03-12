i = 0
numbers = []
max_num = 160
while i < max_num:
	print "At the top i is %d" % i
	numbers.append(i)

	i = i * 2
	print "Numbers now: ", numbers
	print "At the bottom i is % d" % i

print "The numbers: "

for num in numbers:
	print num


#Drill 1. Convert this while-loop to a function that you can call, 
# and replace 6 in the test (i < 6) with a variable.
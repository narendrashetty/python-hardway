i = 0
numbers = []

while i < 6:
	print "at the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Contents now: ", numbers
	print "At the bottom i is %d" % i
	
print "The numbers are: "

for n in numbers:
	print n
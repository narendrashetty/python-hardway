a = 10
b = 20
c = 30

if a < b:
	print "a is lesser than b"
elif a > b:
	print "a is greater than b"
else:
	print "not sure"

if c > b:
	print "c is greater than b"
elif c < b:
	print "c is lesser than b"
else:
	print "not sure"
	
b += 10

if b >= c:
	print "b is greater or equal to c"
	
if b == c:
	print "b is equal to c"
else:
	print "It is not equal"

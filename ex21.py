def add(a, b):
	print "Adding %d + %d :" % (a, b)
	return a + b
	
def sub(a, b):
	print "Subtracting %d - %d :" % (a, b)
	return a - b
	
def mul(a, b):
	print "Multiplying %d * %d :" % (a, b)
	return a * b
	
def div(a, b):
	print "Dividing %d / %d :" % (a, b)
	return a / b
	
r1 = add(10, 20)
r2 = sub(10, 5)
r3 = mul(10, 2)
r4 = div(10, 2)

print "Result1 is %d\nResult2 is %d\nResult3 is %d\nResult4 is %d" % (r1, r2, r3, r4)

trick = add(r1, sub(r2, mul(r3, div(r4, 2))))

print "The result is ", trick
#functions

def first(arg1, arg2):
	print "args: %s, %s" % (arg1, arg2)
	
print "passing value"
first(10, 20)

print "passing variables"
a = 10
b = 20
first(a, b)

print "operating while calling"
first(10 + 20, 30 + 40)

print "operating on variable while calling"
first(a + 10, b + 10)
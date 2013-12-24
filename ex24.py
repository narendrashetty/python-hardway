print "all out here"
print "you\'d use escape sequences for \\ or newline \n or for \t tab"

print """
multiline it is
so whr it goes on
and
on and
on
"""

a = 10 - 2 + 3 - 6

print "Result is ", a

def fun1(arg):
	b = arg *500
	c = b / 100
	d = c + 10
	return b, c, d

p, q, r = fun1(1000)

print "The result is %d %d and %d" % (p, q, r)
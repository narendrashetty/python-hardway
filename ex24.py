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

v = 1000

p, q, r = fun1(v)

print "The result is %d %d and %d" % (p, q, r)

v /= 10

print "Can also call function here so we get %d %d and %d" % fun1(v)
#functions

def first(*args):
	arg1, arg2 = args
	print "args: %s, %s" % (arg1, arg2)
	
def second(arg1, arg2):
	print "args: %s, %s" % (arg1, arg2)
	
def third(arg1):
	print "args: %s" % (arg1)
	
def fourth():
	print "None"
	
first("aaa", "bbb")

second("aaa", "bbb")

third("aaa")

fourth()
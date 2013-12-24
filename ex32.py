int_arr = [1, 2, 3, 4]
string_arr = ['aaa', 'bbb', 'ccc', 'ddd']
mixed_arr = [1, 'aaa', 2, 'bbb']

for n in int_arr:
	print "%d" % n

for s in string_arr:
	print "%s" % s
	
for m in mixed_arr:
	print "%r" % m
	
#dynamic array

dynamic_arr = []

for i in range(0, 6):
	print "Adding %d in dynamic_arr" % i
	dynamic_arr.append(i)

for i in dynamic_arr:
	print "%d" % i
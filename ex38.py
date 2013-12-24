str = "one two three four five six"

print "lets add element to string"

arr = str.split(' ')
new = ["seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen"]

while len(arr) < 10:
	a = new.pop()
	print "adding ", a
	arr.append(a)
	print "There's %d elements in the list" % len(arr)
	
print "completed adding: ", arr

print arr[1]
print arr[-1]
print arr.pop()
print ', '.join(arr)
print '#'.join(arr[3:5])

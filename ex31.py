prompt = '>'
print "enter 1:operation or 2:exit"

a = raw_input(prompt)

if a == "1":
	print "you have slelected 1"
	print "1. add number"
	print "2. subtract number"
	
	r = raw_input(prompt)
	
	if r == "1":
		print "added"
	elif r == "2":
		print "subtracted"
	else:
		print "invalid"
		
elif a == "2":
	print "thank you for using"
	
else:
	print "invalid"
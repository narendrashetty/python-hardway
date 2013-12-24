from sys import exit

def gold_room():
	print "This is gold room.. hw much do u want?"
	
	next = raw_input("> ")
	if "0" in next or "1" in next:
		q = int(next)
	else:
		dead("wrong input")
		gold_room()
	
	if q < 50:
		print "good job"
		exit(0)
	else:
		dead("limit exceeded")

def beer_room():
	print "what will you do to move the bear"
	flag = False
	
	while True:
		next = raw_input("> ")
		if next == "take honey":
			dead("not happening")
		elif next == "taunt beer" and not flag:
			print "beer has moved"
			flag = True
		elif next == "taunt beer" and flag:
			dead("not again")
		elif next == "open door" and flag:
			gold_room()
		else:
			print "Invalid"
		
def deer_room():
	print "Deer is here"
	print "what will you do? flee or eat your head"
	
	next = 	raw_input("> ")
	if "flee" in next:
		start()
	elif "head" in next:
		dead("head eaten")
	else:
		deer_room()
		
def dead(why):
	print why

def start():
	print "select door right or left"
	
	next = raw_input("> ")
	
	if next == "left":
		beer_room()
	elif next == "right":
		deer_room()
	else:
		dead("type sumthing")

start()
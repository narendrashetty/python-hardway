name = 'Narendra N Shetty'
age = 23 #:)
height = 74 #inches
weight = 180 #lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

#using %s
print "Let's talk about %r." % name
#using %r
print "Let's talk about %r." % name

print "%s is %d inches tall, which is %.2f centimetre." % (name, height, height * 2.54)
print "%s is %d pounds heavy, which is equal to %.2f kilograms." % (name, weight, weight/2.2046)
print "%s has got %s eyes and %s hair." % (name, eyes, hair)
print "%s has got %s colour teeth." % (name, teeth)

print "If i add %d, %d and %d i get %d."% (age, height, weight, age + height + weight)
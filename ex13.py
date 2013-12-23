#command line

#import argv from sys module
from sys import argv

#spliting the parameters in different variables
a, b, c, d = argv

#first parameter contains filename, the rest contains passed values
print "file name: ", a
print "first parameter: ", b
print "second parameter: ", c
print "third parameter: ", d

#combining both raw_input and argv
b = raw_input("enter 1st: ")
c = raw_input("enter 2nd: ")
d = raw_input("enter 3rd: ")

print "first parameter: ", b
print "second parameter: ", c
print "third parameter: ", d
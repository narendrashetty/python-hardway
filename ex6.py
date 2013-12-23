#creating a string variable with formats %d
x = "There are %d types of people." % 10
#creating a string variable 'binary
binary = "binary"
#and another string variable
do_not = "don't"

#creating a variable y using the above 2 strings by placing it using string formats 
y = "Those who know %s and those who %s." % (binary, do_not)

#printing both x and y in different lines
print x
print y

#using %r and %s where %r(raw) used for debugging
print "I said: %r." % x
print "I also said: '%s'." % y

#creating a boolean variable
hilarious = False
#and a string with format %r
joke_evaluation = "Isn't that joke so funny?! %r"

#combining both in 1 variable and printing it
print joke_evaluation % hilarious

w = "This is the left side of..."
e = " a string with a right side."

#concatination of both string w and e using + operator and printing it
print w + e
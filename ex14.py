from sys import argv

script, name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (name, script)

print "Do you like me %s?" % name
like = raw_input(prompt)

print "Where do you live %s?" % name
live = raw_input(prompt)

print "What kind of computer do you have?"
comp = raw_input(prompt)

print "Whats your favourite tourism spot?"
spot = raw_input(prompt)

print """
you said %r about liking me.
You live in %r
You have a %r computer.
And you like %r.
""" % (like, live, comp, spot)

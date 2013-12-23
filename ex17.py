from sys import argv
from os.path import exists

a, sfname, dfname = argv

print "copying file from %s to %s" % (sfname, dfname)

infile = open(sfname)
indata = infile.read()

print "size of input file : %d bytes" % len(indata)

print "output file exists? %r" % exists(dfname)
print "enter to continue"
raw_input()

outfile = open(dfname, 'w')
outfile.write(indata)

print "successfully copied"

infile.close()
outfile.close()

#1 line long

#open(dfname, 'w').write(open(sfname).read()).close()
#importing argv from sys package
from sys import argv

#spliting
a, fname = argv

#function to print all contents
def fn1(f):
	print f.read()

#function to move the cursor to start of the file
def fn2(f):
	f.seek(0)

#function to print a line
def fn3(ln, f):
	print ln, f.readline()
	
#opening a file
cfile = open(fname)

print "printing all contents"
fn1(cfile)

print "rewinding to start of the file"
fn2(cfile)

print "printing 3 lines"

line = 1
fn3(line, cfile)

line = line + 1
fn3(line, cfile)

line += 1
fn3(line, cfile)

from sys import argv

a, fname = argv

print "erasing the file ",fname
print "to escape press [ctrl-C]."
print "Enter to confirm"

raw_input()

print "opening the file"
target = open(fname, 'w')

print "deleting the content using truncate"
target.truncate()

print "lets write into the file"

l1 = raw_input("line1: ")
l2 = raw_input("line2: ")
l3 = raw_input("line3: ")

print "writing into file ..."

target.write(l1)
target.write("\n")
target.write(l2)
target.write("\n")
target.write(l3)
target.write("\n")

target.close()
print "write completed"
print "content of %r is " % fname

print open(fname).read()
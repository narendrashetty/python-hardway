import urllib, htmllib, formatter, sys
a, arg = sys.argv
myurl = urllib.urlopen("http://%s" % arg)
data = myurl.read()
myurl.close()
format = formatter.AbstractFormatter(formatter.NullWriter())
parse = htmllib.HTMLParser(format)
parse.feed(data)
for link in parse.anchorlist:
	print link
import htmllib, urllib, formatter, sys

website = urllib.urlopen("http://www.swaroopsm.com")
data = website.read()
website.close()
format = formatter.AbstractFormatter(formatter.DumbWriter(sys.stdout))
parse = htmllib.HTMLParser(format)
parse.feed(data)
parse.close()
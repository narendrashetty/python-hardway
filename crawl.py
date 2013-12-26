import urllib, re, sys, htmllib, formatter

a, url = sys.argv

content = urllib.urlopen('http://%s' % url).read()

format = formatter.AbstractFormatter(formatter.NullWriter())

parse = htmllib.HTMLParser(format)
parse.feed(content)

links = []
links = parse.anchorlist
for link in links:
	if re.search('http', link) != None:
		print link
		web = urllib.urlopen(link).read()
		parse.feed(web)
		for morelink in parse.anchorlist:
			if re.search('http', morelink) != None:
				print morelink
		
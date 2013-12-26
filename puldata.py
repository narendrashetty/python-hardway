import urllib, re, sys

a, arg = sys.argv

content = urllib.urlopen('http://finance.google.com/finance?q=%s' % arg).read()

print re.search('<span id="ref.*>(.*)<',content).group(1)
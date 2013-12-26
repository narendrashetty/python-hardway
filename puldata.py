import urllib, re, sys

a, arg = sys.argv

content = urllib.urlopen('http://in.finance.yahoo.com/q?s=%s' % arg).read()

print re.search('<span id=".*>(.*)</span>', content).group(1)
import urllib
myurl = urllib.urlopen("http://www.google.com")
print myurl
content = myurl.readlines()
print content
header = myurl.info()
print header.getheader("date")
print header.getheader("content-type")

urllib.urlretrieve("http://www.google.com", filename = "urlcontent")


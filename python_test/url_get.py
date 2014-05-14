import urllib, urllib2
url = 'http://dna.daum.net'

u = urllib.urlopen(url)
data = u.read()

#print data

try:
   data = urllib2.urlopen(url).read()
except urllib2.HTTPError, e:
   print "HTTP error: %d" % e.code
except urllib2.URLError, e:
   print "Network error: %s" % e.reason.args[1]

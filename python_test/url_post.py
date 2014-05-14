import urllib

url = "http://apis.daum.net/search/knowledge?&;output=xml&q=OpenAPI"

apikey = "DAUM_SEARCH_DEMO_APIKEY"
output = "xml"
q = "OpenAPI"

params = urllib.urlencode({
	'apikey': apikey,
	'output': output,
	'q': q
})

data = urllib.urlopen(url, params).read()
print data

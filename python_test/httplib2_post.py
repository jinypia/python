import httplib2
http = httplib2.Http()

url = "http://apis.daum.net/search/knowledge?&;output=xml&q=OpenAPI"

apikey = "DAUM_SEARCH_DEMO_APIKEY"
output = "xml"
q = "OpenAPI"

import urllib
params = urllib.urlencode({
	'apikey': apikey,
	'output': output,
	'q': q
})

response, content = http.request(url, 'POST', params,
headers = {'Content-type': 'application/x-www-form-urlencoded'}
)

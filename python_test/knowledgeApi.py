import simplejson, urllib
apikey = "{test input}"
SEARCH_BASE ="http://apis.daum.net/search/knowledge"

def search(query, **args):
    args.update({
            'apikey': apikey,
            'q': query,
            'output': 'json'
    })

    url = SEARCH_BASE + '?' + urllib.urlencode(args)
    
    result = simplejson.load(urllib.urlopen(url))

    return result['channel']

info = search('OpenAPI')
for item in info['item']:
    print item['title']

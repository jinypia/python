import urllib
from xml.dom import minidom

def knowledge_by_query(q):
	url = "http://apis.daum.net/search/knowledge?apikey=DAUM_SEARCH_DEMO_APIKEY&;output=xml&q=" + q
	dom = minidom.parse(urllib.urlopen(url))

	items = dom.getElementsByTagName("item")
	for item in items:
		for node in item.childNodes:
			if node.nodeName == "title":
				print node.childNodes[0].nodeValue

print knowledge_by_query("OpenAPI")


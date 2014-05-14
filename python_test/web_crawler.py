from crawler.crawler import Crawler

# create Crawler object
mycrawler = Crawler()

# assign URL and add it to seed list
seeds = ['http://www.example.com/'] 
mycrawler.add_seeds(seeds)

# assign regular url pattern
url_patterns = ['^(.+example\.com)(.+)$'] 
mycrawler.start(url_patterns)

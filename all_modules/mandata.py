##from bs4 import BeautifulSoup
##import requests
## 
##url = 'http://proxy-hunter.blogspot.com/2010/03/18-03-10-speed-l1-hunter-proxies-310.html'
##r = requests.get(url)
##r.content
##r.encoding
##soup = BeautifulSoup(r.text)
##regex  = r.compile(r'^(\d{3}).(\d{1,3}).(\d{1,3}).(\d{1,3}):(\d{2,4})')
##proxylist = soup.find_All(attrs = {"class":"Apple-style-span", "style": "color: black;"}, text = regex)
##data = proxylist[0]
##for x in data.split('\n'):
##        print x


from bs4 import BeautifulSoup as Soup
import re, urllib 
url = 'http://proxy-hunter.blogspot.com/2010/03/18-03-10-speed-l1-hunter-proxies-310.html'
document = urllib.urlopen(url)
tree = Soup(document.read())
regex  = re.compile(r'^(\d{3}).(\d{1,3}).(\d{1,3}).(\d{1,3}):(\d{2,4})')
proxylist = tree.find_All(attrs = {"class":"Apple-style-span", "style": "color: black;"}, text = regex)
data = proxylist[0]
for x in data.split('\n'):
        print x

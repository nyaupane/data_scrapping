import requests
from bs4 import BeautifulSoup
url = 'http://www.acem.edu.np/index.php?page=content&id=5'
r = requests.get(url)
soup = BeautifulSoup(r.text)
p = soup.find_all("div",{"class":"items-leading"})
print p.get_text()

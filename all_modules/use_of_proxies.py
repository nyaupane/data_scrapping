import requests
from bs4 import BeautifulSoup
proxies = {
    "http":"http://111.11.255.11:80"}
url = 'http://www.acem.edu.np/index.php?page=content&id=5,proxies=proxies'
r = requests.get(url)
soup = BeautifulSoup(r.text)
p = soup.find_all("div",{"class":"items-leading"})
print p

import requests
from bs4 import BeautifulSoup
proxies = {
    "http":"http://111.11.255.11:80"}
url = 'http://www.election.gov.np/election/np/bbvrs,proxies=proxies'
r = requests.get(url)
soup = BeautifulSoup(r.text)
print soup.text

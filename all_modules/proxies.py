import requests
from bs4 import BeautifulSoup
proxy = {
    "http":"http://163.177.79.4:8103"}
url = 'http://http://www.election.gov.np/election/np/bbvrs,proxies=proxy'
r = requests.post(url)
soup = BeautifulSoup(r.content)
print soup


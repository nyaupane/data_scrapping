import requests
from bs4 import BeautifulSoup
proxy = {
    "http":"http://182.254.153.54:80"}
#url = 'http://http://www.election.gov.np/election/np/bbvrs,proxies=proxy'
r = requests.post('http://http://www.election.gov.np/election/np/bbvrs',proxies=proxy)
soup = BeautifulSoup(r.text)
print soup


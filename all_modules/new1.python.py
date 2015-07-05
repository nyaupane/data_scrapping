import requests
import os 
from bs4 import BeautifulSoup
for i in range(1,139):
    url = ('http://www.kaymu.com.np/womens-clothing/?page='+str(i))
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    p = soup.find_all("div",{"class":"info"})
    for link in p:
        print link.text
    

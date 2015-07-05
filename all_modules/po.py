import requests
from bs4 import BeautifulSoup
payload = {'key1':'value1','kay2':'value2','key3':'value3','key4':'value4'
    }
r = requests.get('https://www.kaymu.com.np/customer/account/dashboard/?action=log&source=em/',params = payload)
print r.content

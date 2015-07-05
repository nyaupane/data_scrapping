import requests
from bs4 import BeautifulSoup
payload = {'LoginForm[email]': 'narayan.nyaupane37@gmail.com', 'LoginForm[password]':'20212050','LoginForm[rememberme]':'0','yt0':'login'}
r = requests.post('https://www.kaymu.com.np/customer/list/salesvalidation', params=payload)
print (r.text)
##p = soup.find_all("a",{"href":"/customer/list/salesvalidation/"})
##for data in p:
##    print data.text
##     payload = {'key1': 'value1', 'key2': 'value2'}
##r = requests.post("http://httpbin.org/post", data=payload)
## print(r.text)

import requests
from bs4 import BeautifulSoup
payload = {'LoginForm[email]':'narayan.nyaupane37@gmail.com','LoginForm[password]':'20212050'}
r = requests.get("/https://www.kaymu.com.np/customer/account/dashboard/?action=log&source=em/post",params=payload)
soup = BeautifulSoup(r.text)
p = soup.find_all("div",{"class":"info"})
print p

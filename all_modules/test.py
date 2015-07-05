import requests
from bs4 import BeautifulSoup
import MySQLdb
db = MySQLdb.connect("localhost","root","root","name_rate")
cursor = db.cursor()
for i in range(116,119):
    url = 'http://www.kaymu.com.np/womens-clothing/?page='+str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
##    q = soup.find_all("span",{"class":"title ellipsis"})
    price = soup.find_all("div",{"class":"itm-price special"})
    for output in price:
        print output.text
##    for data in q:
##        output1 = data.text
####        print output1
##        for output in price:
##            output2=output.text
##            print output2
##        sql = """INSERT INTO INFORMATION(NAME_PRODUCT,PRICE) VALUES (%s,$s)"""
##        cursor.execute(sql,[output1,output2])
##        db.commit()
            

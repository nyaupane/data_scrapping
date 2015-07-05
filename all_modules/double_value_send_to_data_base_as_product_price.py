import requests
from bs4 import BeautifulSoup
import MySQLdb
db = MySQLdb.connect("localhost","root","root","name_rate")
cursor = db.cursor()
for i in range(116,119):
    url = 'http://www.kaymu.com.np/womens-clothing/?page='+str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    q = soup.find_all("span",{"class":"title ellipsis"})
    
    r = soup.find_all("div",{"class":"itm-price special"})
    for data in q:
        print data.text
        for name in r:
            print name.text
            
##            cursor.execute("DROP TABLE IF EXISTS INFORMATION")
##            sql = """CREATE TABLE INFORMATION (
##            ID INT NOT NULL AUTO_INCREMENT,
##            NAME_PRODUCT  VARCHAR(20) NOT NULL)"""
##            cursor.execute(sql)
            sql = """INSERT INTO INFORMATION(NAME_PRODUCT,PRICE) VALUES (%s,%s)"""
            cursor.execute(sql,[data.text,name.text])
            db.commit()
            break

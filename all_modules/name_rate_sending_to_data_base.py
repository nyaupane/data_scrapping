import requests
from bs4 import BeautifulSoup
import MySQLdb
for i in range(116,119):
    url = 'http://www.kaymu.com.np/womens-clothing/?page='+str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    p = soup.find_all("span",{"class":"title ellipsis"})
    q = soup.find_all("div",{"class":"itm-price ellipsis ptm pbs"})
    for link,data in p,q:
        db = MySQLdb.connect("localhost","root","root","name_rate")
        print 'name-rate table is connected'
        cursor = db.cursor()
##        cursor.execute("DROP TABLE IF EXISTS INFORMATION")
##        sql = """CREATE TABLE INFORMATION (
##         NAME_PRODUCT  VARCHAR(20) NOT NULL,
##         COST  INT(20) )"""
##        cursor.execute(sql)
        sql = """INSERT INTO INFORMATION(NAME_PRODUCT,COST) VALUES (%s,%s)"""
        cursor.execute(sql,[link.text,data.text])
        db.commit()

    

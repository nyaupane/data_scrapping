import requests
from bs4 import BeautifulSoup
import MySQLdb
for i in range(116,119):
    url = 'http://www.kaymu.com.np/womens-clothing/?page='+str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    q = soup.find_all("div",{"class":"itm-price ellipsis ptm pbs"})
    for data in q:
        print data.text
        db = MySQLdb.connect("localhost","root","root","name_rate")
##        print 'name-rate table is connected'
        cursor = db.cursor()
##        cursor.execute("DROP TABLE IF EXISTS INFORMATION")
##        sql = """CREATE TABLE INFORMATION (
##         ID INT NOT NULL AUTO_INCREMENT,
##         NAME_PRODUCT  VARCHAR(20) NOT NULL)"""
##        cursor.execute(sql)
        sql = """INSERT INTO INFORMATION(NAME_PRODUCT) VALUES (%s)"""
        cursor.execute(sql,[data.text])
        db.commit()

    

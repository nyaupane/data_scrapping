import requests
from bs4 import BeautifulSoup
import MySQLdb
db = MySQLdb.connect("localhost","root","root","name_rate")
print 'name-rate table is connected'
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS INFORMATION")
sql = """CREATE TABLE INFORMATION (
         NAME_PRODUCT  VARCHAR(20) NOT NULL,
         COST  INT(20) )"""

cursor.execute(sql)
sql = """INSERT INTO INFORMATION(NAME_PRODUCT,
         COST)
         VALUES ('white t shor', '500')"""
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
    



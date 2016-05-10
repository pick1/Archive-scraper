from urlparse import urljoin
from urllib2 import urlopen
import requests
from bs4 import BeautifulSoup
import MySQLdb
import re

#mysql portion
mydb = MySQLdb.connect(host='localhost',
   user= '****',
   passwd='****',
   db='****')
cur = mydb.cursor()
# setup MySQL table for storage
def store (headline):
    cur.execute('INSERT IGNORE INTO OILNEWS (headline) VALUES ( \"%s\")',(headline, ))
    cur.connection.commit()
base_url = "http://oilprice.com/Latest-Energy-News/World-News"

# page request; page 1 through n
n = 376
for i in range(1, n+1):
    if (i == 1):
    # handle first page
        response = urlopen(base_url)
    response = urlopen(base_url + "/Page-%d.html" % i)
    html = response

    # data parsing
    soup = BeautifulSoup(html.read().decode('utf-8'),"lxml")
    table = soup.find('div', {'class':'tableGrid__column tableGrid__column--articleContent category'})
    for a in table.find_all('a', href=True)[::2][:-5]:
        headline = a['href']
        store(headline)
        print headline

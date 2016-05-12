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
def store (auth_date, url):
    cur.execute('INSERT IGNORE INTO OILNEWS (auth_date, url) VALUES ( \"%s\", \"%s\")',(auth_date, url ))
    cur.connection.commit()
base_url = "http://oilprice.com/Latest-Energy-News/World-News"
# request page 1 through n; where 1 = max. pages to scrape
n = 1  
for i in range(1, n+1):
    if (i == 1):
    # handle first page
        response = urlopen(base_url)
    response = urlopen(base_url + "/Page-%d.html" % i)
    html = response
    soup = BeautifulSoup(html.read().decode('utf-8'),"lxml")
    main_div = soup.select_one("div.tableGrid__column.tableGrid__column--articleContent.category")
    divs = main_div.select('div.categoryArticle__content')
    for d in divs:
        auth_date = d.select_one("p.categoryArticle__meta").text
        url = d.a["href"]
        store (auth_date, url)
        print (auth_date, url)
        print '\n'

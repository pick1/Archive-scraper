from urlparse import urljoin
from urllib2 import urlopen
import requests
from bs4 import BeautifulSoup
import MySQLdb
import re


base_url = "http://advances.sciencemag.org/"
html = urlopen(base_url)
soup = BeautifulSoup(html.read().decode('utf-8'),"lxml")
#links = soup.findAll("a","href")
headlines = soup.findAll("div", "highwire-cite-title media__headline__title")
links = soup.findAll(class_="highwire-cite-linked-title")
for link in links:
    url = (urljoin(base_url, link["href"]))
#    print url
for headline in headlines:
    text = (headline.get_text())
    print  text, url

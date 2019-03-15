import requests
from bs4 import BeautifulSoup
import pandas as pd


titles = []
authors = []
dates = []
pitches = []
links = []
abstracts = []

base_url = "http://advances.sciencemag.org"
html = requests.get(base_url)
soup = BeautifulSoup(html.text, "lxml")
headlines = soup.findAll("div", "highwire-cite-title media__headline__title")
box = soup.findAll(class_="headline-list item-list highwire-list " \
                          "highwire-article-citation-list")
for b in box[0]:
    titles.append(str(b.h3.text))
    authors.append(str(b.p.text).strip("By "))
    dates.append(b.find(class_="highwire-cite-metadata byline").time.text)
    pitch = str(b.div.find(class_="highwire-cite-snippet media__deck")
                .text).strip('\n')
    pitches.append(pitch)
    link = base_url + b.div.find(class_="highwire-cite-linked-title")['href']
    links.append(link)
    abstract_get = requests.get(link)
    abstract_soup = BeautifulSoup(abstract_get.text, "lxml")
    abstract_tag = abstract_soup.findAll(class_="section abstract")
    for a in abstract_tag:
        abst = str(a.p.text)
        abstracts.append(abst)

df = pd.DataFrame(list(zip(titles, authors, dates, pitches, links, abstracts)),
                  columns=['titles', 'authors', 'dates',
                           'pitches', 'links', 'abstracts'])
df.dates = pd.to_datetime(df.dates)


import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "http://oilprice.com/Latest-Energy-News/World-News"

""" request page 1 through n; where 'n = 1' = max. pages to scrape
    (current page count = 906)"""

auths = []
dates = []
sums = []
urls = []

n = 1
for i in range(1, n+1):
    if (i == 1):
        # handle first page
        response = requests.get(base_url)
    response = requests.get(base_url + "/Page-%d.html" % i)
    html = response
    soup = BeautifulSoup(html.text, "lxml")
    main_div = soup.select_one("div.tableGrid__column.tableGrid__column-"
                               "-articleContent.category")
    divs = main_div.select('div.categoryArticle__content')
    for d in divs:
        auth_date = str(d.select_one("p.categoryArticle__meta").text)
        auths.append(auth_date.split(" | ")[1])
        dates.append(auth_date.split(" | ")[0])
        sums.append(d.select_one("p.categoryArticle__excerpt").text)
        urls.append(d.a["href"])
        df = pd.DataFrame(list(zip(auths, dates, sums, urls)),
                          columns=['author', 'date', 'summary', 'url'])
        df.date = pd.to_datetime(df.date)

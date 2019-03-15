import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from datetime import datetime as dt


today = dt.now().strftime('%Y-%m-%d')

links = []
drugname = []
strength = []
ingreds = []
mstat = []
doses = []
subs = []
cos = []
subc = []
substat = []

base_url = 'https://www.accessdata.fda.gov/scripts/cder/daf/index.'\
           'cfm?event=report.page'

base_link_url = 'https://www.accessdata.fda.gov/scripts/cder/daf/index.'\
                'cfm?event=overview.process&ApplNo='

html = requests.get(base_url)
soup = BeautifulSoup(html.content, "html.parser")

table = soup.findAll('table')
rows = table[0].findAll("tr")
if len(soup.findAll('th')) > 0:
        rows = rows[1:]
for row in rows:
    link = base_link_url + str(row.td.br.text).split('#')[1]
    links.append(link)
    linkhtml = requests.get(link)
    linksoup = BeautifulSoup(linkhtml.text, "lxml")
    linkrow = linksoup.findAll('tbody')[0]
    linktds = linkrow.findAll('td')
    drugname.append(linktds[0].text)
    strength.append(linktds[2].text)
    mstat.append(linktds[4].text)
    tds = row.findAll('td')
    ingreds.append(tds[1].get_text())
    doses.append(tds[2].get_text())
    subs.append(tds[3].get_text())
    cos.append(tds[4].get_text())
    subc.append(tds[5].get_text())
    if len(str(subc)) > 1:
        subc.append(subc)
    else:
        subc.append(np.nan)
    substat.append(tds[6].get_text())

df = pd.DataFrame(list(zip(cos, drugname, subs, substat, mstat,
                           links, ingreds, doses, subc, strength)),
                  columns=['company', 'drugname', 'submission',
                           'submission_status', 'marketing_status',
                           'link', 'ingredients', 'dosage',
                           'submission_class', 'strength'])
df['date'] = pd.to_datetime(today)

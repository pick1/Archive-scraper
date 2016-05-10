import requests
from bs4 import BeautifulSoup
import MySQLdb

#mysql portion
mydb = MySQLdb.connect(host='localhost',
       user= 'root',
       passwd='MYSQL',
       db='testdb')
cur = mydb.cursor()
def store (drug_name, active_ingredient, dosage_form_route, sponsor, submission_type):
        cur.execute('INSERT IGNORE INTO FDA (drug_name, active_ingredient, dosage_form_route, sponsor, submission_type) VALUES (\"%s\", \"%s\", \"%s\", \"%s\", \"%s\")',(drug_name, active_ingredient, dosage_form_route, sponsor, submission_type))
        cur.connection.commit()

base_url = 'http://www.fda.gov/Drugs/NewsEvents/ucm130961.htm'
html = requests.get(base_url)
soup = BeautifulSoup(html.content, "html.parser")

table = soup.findAll('table')
rows = table[0].findAll("tr")
if len(soup.findAll('th')) > 0:
        rows = rows[1:]
for row in rows:
        cells = row.findAll('td')
        drug_name = cells[0].get_text()
        active_ingredient =  cells[1].get_text()
        dosage_form_route = cells[2].get_text()
        sponsor = cells[3].get_text()
        submission_type = cells[4].get_text()
        store(drug_name, active_ingredient, dosage_form_route, sponsor, submission_type)
        data = {
           'drug_name': cells[0].get_text(),
           'active_ingredient': cells[1].get_text(),
           'dosage_form_route': cells[2].get_text(),
           'sponsor': cells[3].get_text(),
           'submission_type': cells[4].get_text(),
        }

        print data
        print '\n'
mydb.close()

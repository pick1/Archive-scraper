## Archive-scraper
This is a repository for various web scraping scripts with Python. These scripts primarily focue on gathering data which has exhibited influence upon various market sectors.

#### fda_scrape.py

Programmatically accesses the FDA.gov website to retreive most recent FDA data related to the pharmaceutical approval process. Data is subsequently broken down into constituent pieces (drug name, ingredient, company etc...). The resultant data is then stored in a relational database (MySQL).

packages:
 - BeautifulSOup
 - MysSQLdb

#### oil_scrape.py

Programmatically accesses energy news from oilprice.com to retreive recent headlines and article links related to the energey sector. Data is checked for uniqueness before being sent to storage.

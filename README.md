## Archive-scraper
This is a repository for various web scraping scripts with Python. These scripts primarily focue on gathering data which has exhibited influence upon various market sectors.

packages:
 - BeautifulSOup
 - Pandas
 - requests

#### fda_scrape.py

Programmatically accesses the FDA.gov website. Retreives most recent company data published by the FDA related to the pharmaceutical approval process. Data is subsequently broken down into constituent pieces (drug name, ingredient, company etc...). The resultant data is then stored in a Pandas DataFrame to expedite the desired storage process.

#### oil_scrape.py

Python script for programmatically accessing energy news from oilprice.com. Uses `requests` and BeautifulSoup to retreive recent headlines and article links related to the energey sector. Default gathers headlines and summaries from the frontpage. Alter `n=x` to the depth of the pages to scrape (current page count is 906). Data for each is appended to a list, zipped and formatted to Pandas DataFrame for ease of storage (flat file, database etc...).

#### science.py

Python script access online journal ScienceAdvances and retrieves data. Data retreived starts with articles on the front page and gathers information re: author, date, blurb, url. Url is used to access the article-page and retrieve the article summary. Data is then appended to lists, zipped and formatted to Pandas DataFrame for ease of storage.

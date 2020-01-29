import requests
from bs4 import BeautifulSoup, SoupStrainer
import csv
import re
url = "https://www.census.gov/programs-surveys/popest.html"

r = requests.get(url)

html_code = r.text

soup = BeautifulSoup(html_code, 'html.parser')

links_set = set()

for item in soup.find_all('a', href=re.compile(r'^(http|/.)')):
    links_set.add(item.get('href'))

clean_URIs = [x for x in links_set if x[:4]=='http']
edited_URIs = ["https://www.census.gov" + x for x in links_set if x[:1]=='/']
final_URIs = clean_URIs + edited_URIs


with open("deliverable.csv", "w") as csv_file:
    writer = csv.writer(csv_file,delimiter="\n")
    writer.writerow(final_URIs)
import requests
from bs4 import BeautifulSoup, SoupStrainer
import csv
import re
url = "https://www.census.gov/programs-surveys/popest.html"

# send and catch the url request
r = requests.get(url)

# capture the html code
html_code = r.text

soup = BeautifulSoup(html_code, 'html.parser')
links_set = set()

for item in soup.find_all('a',href=re.compile(r'html')):  
    links_set.add(item.get('href'))

URIs = [x for x in links_set if x[:4]=='http']
edited_URIs = ["https://www.census.gov" + x for x in links_set if x[:1]=='/']
final_URIs = URIs + edited_URIs

if "https://www.census.gov/programs-surveys/popest.html" in final_URIs:
    final_URIs = final_URIs.remove("https://www.census.gov/programs-surveys/popest.html")
    
if "http://www.census.gov/programs-surveys/popest.html" in final_URIs:
    final_URIs = final_URIs.remove("https://www.census.gov/programs-surveys/popest.html")

final_set = set()

for item in final_URIs:  
    final_set.add(item)

with open("deliverable.csv", "w") as csv_file:
    writer = csv.writer(csv_file,delimiter="\n")
    writer.writerow(final_set)   
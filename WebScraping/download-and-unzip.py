from bs4 import BeautifulSoup
from datetime import datetime
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen

import requests

time = datetime.now().strftime("%Y-%m-%d")
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
page = requests.get(r"https://www.whoisdownload.com/newly-registered-domains", headers={"User-Agent": user_agent}).text
soup = BeautifulSoup(page, 'html.parser')
file_destination_path = r"C:\Nowy folder"
valid_results_date = []
valid_results_link = []

html = list(soup.children)[2]
div_search = html.find_all('div', id='table_wraper')
div_search_inside = div_search[0]
table_search = div_search_inside.find_all('table', class_='cart_table')
body_search = table_search[0].find('tbody')
obj_to_str = str(body_search)
obj_list_container = obj_to_str.split('\n')

for tags in obj_list_container:
    if 'Newly Registered Domains of' in tags:
        valid_results_date.append(tags.split('<b>')[1].split('</b>')[0])
    elif 'href' in tags:
        valid_results_link.append(tags.split("href")[1].split('"')[1])

url = valid_results_link[0]

with urlopen(url) as zipfiles:
    with ZipFile(BytesIO(zipfiles.read())) as zfile:
        zfile.extractall(file_destination_path)


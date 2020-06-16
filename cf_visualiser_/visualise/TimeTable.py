from bs4 import BeautifulSoup
import requests
from lxml import html

def fetch_time_table():

    url = "https://codeforces.com/contests"
    page = requests.get(url)

    bs=BeautifulSoup(page.content, 'html.parser')
    table_body = bs.find_all('table', class_="")

    cnt = 0
    for item in table_body:
        rows = item.find_all('tr')
        for row in rows:
            cols=row.find_all('td')
            cols=[x.text.strip() for x in cols]

            if len(cols) == 0:
                cnt = cnt + 1

            if cnt < 2 and len(cols)>=3:
                yield cols
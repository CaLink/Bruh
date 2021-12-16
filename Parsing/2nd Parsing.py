import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://ru.m.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B6%D0%B4%D1%83%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BD%D1%8B%D0%B9_%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81_%D1%81%D1%87%D0%B0%D1%81%D1%82%D1%8C%D1%8F"

page = requests.get(url)
text = page.text
soup = BeautifulSoup(text)

table = soup.find('table', {'class':'wikitable sortable'})

line = table.find('tbody')
lines = []
column = []
for t in line.find_all('tr'):
    tLine = []
       

    for j in t.find_all('td'):
        if j.find_all('a'):
            tLine.append(j.find('a').text)
        else:
            tLine.append(j.text)
    lines.append(tLine)


for i in line.find_all('th'):
    column.append(i.text)


df = pd.DataFrame(lines, columns=column)
print(df)

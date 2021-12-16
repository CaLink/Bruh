import pandas as pd
from pandas.core.frame import DataFrame
import requests
from bs4 import BeautifulSoup

pageStart = "https://www.hse.ru/ba/political/courses/page"
pageEnd = ".html?year=2021"

data = []

for i in range(4):
    url = pageStart + str(i+1) + pageEnd
    page = requests.get(url).text
    html = BeautifulSoup(page,"lxml")

    courses = html.find_all(class_='edu-events__item')
    courses.pop(0)

    for j in courses:
        
        toAdd = []
        
        toAdd.append(j.find(class_='link link_dark').text)
        toAdd.append(j.get('data-href'))
        toAdd.append(j.find(class_="edu-program_status").text)
        toAdd.append(j.find(class_="b-program__lang edu-events__lang").text)

        data.append(toAdd)
        
df = pd.DataFrame(data,columns=['Name','URL','Status','Lang'])


print(df)


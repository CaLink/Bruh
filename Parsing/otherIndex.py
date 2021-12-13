import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

url = "http://www.vybory.izbirkom.ru/region/region/izbirkom?action=show&root=1000004&tvd=100100084849070&vrn=100100084849062&region=0&global=true&sub_region=0&prver=0&pronetvd=null&vibid=100100084849070&type=227"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

page = requests.get(url,headers = headers) #Server return 403
text = page.text

html = BeautifulSoup(text,"lxml")

table = html.find('table',{'class':'table-fixed-columns table-bordered table-striped table-sm'})

#GetColumnName

column = table.find_all('thead')

columns = []

for i in column[0].find_all('th'):
    if i.find('a'):
        columns.append(i.find('a').text)
    elif i.find('b'):
        columns.append(i.find('b').text)
    else:
        columns.append("temp")

line = table.find_all('tbody')

lines = []

for i in line[0].find_all('tr'):
    tempLine = []
    
    for j in i.find_all('td'):

        if j.find('nobr'):
            if j.find('b'):
                tempLine.append(j.find('b').text)
            else:
                tempLine.append(j.find('nobr').text)
        else:
            tempLine.append(j.text)
    
    lines.append(tempLine)

        

df = pd.DataFrame(lines,columns=columns)
df.to_csv("SecondParse.csv")
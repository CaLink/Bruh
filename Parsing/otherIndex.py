import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

url = "http://www.vybory.izbirkom.ru/region/region/izbirkom?action=show&root=1000004&tvd=100100084849070&vrn=100100084849062&region=0&global=true&sub_region=0&prver=0&pronetvd=null&vibid=100100084849070&type=227"

page = requests.get(url) #Server return 403
text = page.text

html = BeautifulSoup(text,"lxml")

table = html.find({'class':'table-fixed-columns table-bordered table-striped table-sm"'})

print(table.prettify())



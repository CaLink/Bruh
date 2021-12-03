import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

class News():

    def __init__(
        self,link = 'link',date='date',aut='author',
        desc='description',title='title',txt='text',
        tag='rubric',dif='difficult'):

        self.link   = link
        self.date   = date
        self.author = aut
        self.desc   = desc
        self.title  = title
        self.text   = txt
        self.tags = tag
        self.dif    = dif


    def toDick(self):
        return {'link':self.link,'date':self.date,'tags':self.tags,'author':self.author, 'difficult':self.dif,'title':self.title,'desc':self.desc,'text':self.text}

    
    def MakeNewsFromURL(newsUrl):
        global url

        newNews = []

        for url in newsUrl:

            ret = None

            currentPage = requests.get(mainUrl + url)
            currentPageText = currentPage.text
            currentPageHTML = BeautifulSoup(currentPageText, features="lxml")

            link = mainUrl + url
            
            date = ""
            for i in currentPageHTML.find_all('time')[0].find_all('span'):
                date += i.text + ' '

            tags = ""
            for i in currentPageHTML.find_all('a',{'data-rubric':True}):
                tags += i.text + ' '

            diff = currentPageHTML.find('span',{'class':'difficult-value'}).text

            title = currentPageHTML.find_all('h1')[0].text
            if "/material/" in url:
                title += '\n' + currentPageHTML.find('p',{'class':'subtitle'}).text

            text = ""

            for i in currentPageHTML.find('div',{'class':'body js-mediator-article'}).find_all('p'):
                text += i.text + '\n'


            aut=''
            if "/material/" in url:
                aut = currentPageHTML.find('meta', {'name':'author'}).get('content')
            else:
                aut = currentPageHTML.find('div',{'class':'body js-mediator-article'}).find_all('p')[-1].text

            
            ret = News(link,date,aut,'idk',title,text,tags,diff)

            newNews.append(ret)

            sleep(2)
            print('sas')

        return newNews


mainUrl = 'https://nplus1.ru'

page = requests.get(mainUrl)
text = page.text

html = BeautifulSoup(text, "lxml")

#news = html.find_all('item')
news = html.find_all('article',{"class":"item"})

links = []

for n in news:
    for l in n.find_all('a',{'data-id':True}):
        links.append(l.get('href'))
        
#print(*links,sep='\n')
#print(news[1].prettify())
#print(len(news))
#print(news[1].text)


NewsList = News.MakeNewsFromURL(links)


df = pd.DataFrame.from_records(n.toDick() for n in NewsList)

df.to_csv("Ad.csv")

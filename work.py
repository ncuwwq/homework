import requests
from bs4 import BeautifulSoup
def get():
        r=requests.get('http://news.ncu.edu.cn/')
        r.encoding='utf-8'
        demo=r.text
        soup=BeautifulSoup(demo,'html.parser')
        for news in soup.select('.newslist')
            x=soup.select('ul')
            print(x)
get()


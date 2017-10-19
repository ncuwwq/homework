import requests
from bs4 import BeautifulSoup
def get():
    try:
        r=requests.get('http://news.ncu.edu.cn/')
        r.encoding='utf-8'
        demo=r.text
        soup=BeautifulSoup(demo,'html.parser')
        x=soup.find_all('title')
        print(x)
    except:
        print("爬取失败")

get()


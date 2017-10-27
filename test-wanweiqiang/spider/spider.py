import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return""

def main():
    goods='w'
    url='http://opac.ncu.edu.cn/opac/search_adv_result.php?sType0=any&q0='+goods
    infoList=[]
    html=getHTMLText(url)
    soup=BeautifulSoup(html,"html.parser")
    f=soup.find('table')
    print(f)
main()





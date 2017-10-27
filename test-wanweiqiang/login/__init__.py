import requests
from bs4 import BeautifulSoup

url = "https://os.ncuos.com/loginBox/login"
UA = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"

header = {"User-Agent": UA,
          "Referer": "https://os.ncuos.com/index/indexApp"
          }

x = requests.Session()
f = x.get(url, headers=header)

soup = BeautifulSoup(f.content, "html.parser")
once = soup.find('input', {'name': 'once'})['value']
print(once)

postData = {'u': '6108117001',
            'p': '990570',
            'once': once,
            'next': '/'
            }
x.post(url,
       data=postData,
        headers=header)
f = x.get('https://os.ncuos.com/index/indexApp', headers=header)
print(f.content.decode())
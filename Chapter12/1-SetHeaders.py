import requests
from bs4 import BeautifulSoup

session = requests.Session()

headers = {"User-Agent": "User-Agent:Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",
           "Accept": "This is accept"
           }
url = 'https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending'
req = session.get(url, headers=headers)
bsObj = BeautifulSoup(req.text, 'lxml')
print(bsObj.find('table', {'class': 'table-striped'}).get_text)

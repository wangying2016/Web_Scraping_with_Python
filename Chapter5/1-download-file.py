from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('http://books.toscrape.com/')
bsObj = BeautifulSoup(html, 'html.parser')
imgs = bsObj.findAll('img', {'class': 'thumbnail'})
count = 1
for img in imgs:
    url = img.attrs['src']
    if url.find('http:') == -1:
        url = 'http://books.toscrape.com/%s ' % url
    urlretrieve(url, 'logo%d.jpg' % count)
    count += 1



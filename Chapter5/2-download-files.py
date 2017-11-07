from urllib.request import urlretrieve
from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import os


def downloadImages(page, bsObj, url):
    # 1. Create directory.
    imgDir = '2-download-images/page%d' % page
    if os.path.exists(imgDir) is False:
        os.makedirs(imgDir)

    # 2. Download images.
    imgUrls = bsObj.findAll('img', {'class': 'thumbnail'})
    count = 0
    for img in imgUrls:
        count += 1
        imgUrl = urljoin(url, img.attrs['src'])
        print('Download image url: %s' % imgUrl)
        urlretrieve(imgUrl, '%s/%d.jpg' % (imgDir, count))


url = 'http://books.toscrape.com/'
page = 0

while True:
    # 1. Open new page.
    html = urlopen(url)
    bsObj = BeautifulSoup(html, 'html.parser')

    # 2. Download images.
    page += 1
    downloadImages(page, bsObj, url)

    # 3. Move to next page.
    nextPage = bsObj.find('a', text='next')
    if nextPage is not None:
        url = urljoin(url, nextPage.attrs['href'])
        print('Enter new page: %s' % url)
    else:
        break

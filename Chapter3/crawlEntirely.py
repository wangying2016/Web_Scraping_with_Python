from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def getLinks(pageUrl):
    global pages
    html = urlopen('https://en.wikipedia.org' + pageUrl)
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll('a', href=re.compile('^(/wiki/)')):
        if link.attrs['href'] not in pages:
            # We have encountered a new page
            newPage = link.attrs['href']
            print(newPage)
            pages.add(newPage)
            getLinks(newPage)


pages = set()
getLinks('')
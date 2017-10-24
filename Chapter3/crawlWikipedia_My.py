from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from random import randint


def getLinks(url: str) -> list:
    """
    return a list of links on the url page.
    """
    html = urlopen('https://en.wikipedia.org' + url)
    bsObj = BeautifulSoup(html)
    return bsObj.find('div', {'id': 'bodyContent'}) \
                .findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))


links = getLinks('/wiki/Kevin_Bacon')
while len(links) is not 0:
    link = links[randint(0, len(links))]
    print(link.attrs['href'])
    links = getLinks(link.attrs['href'])

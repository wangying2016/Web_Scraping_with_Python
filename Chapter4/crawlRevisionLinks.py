from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re


def getLinks(articleUrl):
    html = urlopen('https://en.wikipedia.org' + articleUrl)
    bsObj = BeautifulSoup(html, 'html.parser')
    return bsObj.find('div', {'id': 'bodyContent'}
                      ).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))


def getHistoryIPs(pageUrl):
    # Format of revision history pages is:
    # https://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl = pageUrl.replace('/wiki/','')
    historyUrl = 'https://en.wikipedia.org/w/index.php?title=' \
                 + pageUrl + '&action=history'
    print('history url is: ' + historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, 'html.parser')

    # finds only the links with class 'mw-annonuserlink' which has IP addresses
    # instead of usernames
    ipAddresses = bsObj.findAll('a', {'class': 'mw-anonuserlink'})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

random.seed(datetime.datetime.now())
links = getLinks('/wiki/Python_(programming_language)')

while len(links) > 0:
    for link in links:
        print('-------------------------------')
        historyIps = getHistoryIPs(link.attrs['href'])

        for historyIP in historyIps:
            print(historyIP)

    newLink = links[random.randint(0, len(links) - 1)].attrs['href']
    links = getLinks(newLink)

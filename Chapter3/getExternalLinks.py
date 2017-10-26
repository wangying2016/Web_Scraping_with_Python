from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import datetime
import random


homePage = 'http://www.qq.com/'
pages = set()
random.seed(datetime.datetime.now())


# Retrieves a list of all Internal links found on a page.
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # Finds all links that begin with a '/'
    for link in bsObj.findAll('a', href=re.compile('^(/|.*' + includeUrl + ')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks


# Retrieves a list of all external links found on a page.
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # Finds all links that start with 'http' or 'www' that do
    # not contain the current URL
    for link in bsObj.findAll('a',
                              href=re.compile('^(http|www|https)((?!' + excludeUrl + ').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def splitAddress(address):
    addressParts = address.replace('http://', '').replace('https://', '').split('/')
    return addressParts


def getRandomExternalLink(startingPage):
    try:
        html = urlopen(startingPage)
    except HTTPError:
        print('Open ' + startingPage + ' failed. Reset to home page.')
        return homePage
    bsObj = BeautifulSoup(html, 'html.parser')
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(bsObj, startingPage)
        # Add judgement.
        if len(internalLinks) == 0:
            print('Open ' + startingPage + ' failed. Reset to home page.')
            return homePage
        return getRandomExternalLink(internalLinks[random.randint(0,
                                     len(internalLinks) - 1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    # Add judgement.
    if externalLink is None:
        print('Open ' + startingSite + ' failed. Reset to home page.')
        externalLink = homePage
    print('Random external link is: ' + externalLink)
    followExternalOnly(externalLink)


followExternalOnly(homePage)

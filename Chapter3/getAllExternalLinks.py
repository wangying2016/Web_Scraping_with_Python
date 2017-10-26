from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


allExtLinks = set()
allIntLinks = set()


def getInternalLinks(bsObj, includeUrl):
    """
    Get the list of the internal links.
    """
    internalLinks = []
    for link in bsObj.findAll('a', href=re.compile('^(/|.*' + includeUrl +')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks



def getExternalLinks(bsObj, excludeUrl):
    """
    Get the list of the external links.
    """
    externalLinks = []
    for link in bsObj.findAll('a', href=re.compile('^(http|https|www)((?!' + excludeUrl + ').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def splitAddress(address):
    """
    Split the address.
    """
    return address.replace('http://', '').replace('https://', '').split('/')


def getAllExternalLinks(siteUrl):
    """
    Get all the external links. Collects a list of all
    external URLs found on the site.
    """
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html, 'html.parser')
    internalLinks = getInternalLinks(bsObj, splitAddress(siteUrl)[0])
    externalLinks = getExternalLinks(bsObj, splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            print('About to get link: ' + link)
            allIntLinks.add(link)
            getAllExternalLinks(link)


getAllExternalLinks('https://www.oreilly.com')
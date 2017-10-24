from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4 import re


html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html)

# My solution
# div = bsObj.find('div', {'id': 'bodyContent'})
# links = div.findAll('a', {'href': re.compile('^/wiki/[^:]*$')})
# for link in links:
#     print(link.attrs['href'])

# Author's solution
# Regular expression  ^((?![A-Z]).)*$
# "Does not contain". This odd pairing of symbols, immediately
# preceding a character(or regular expression), indicates that
# character should not be found in that specific place in the
# larger string. This can be tricky to use; after all, the
# character might be found in a different part of the string.
# If trying to eliminate a character entirely, use in conjunction
# with a ^ and $ at either end.
for link in bsObj.find('div', {'id': 'bodyContent'}) \
        .findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')):
    print(link.attrs['href'])

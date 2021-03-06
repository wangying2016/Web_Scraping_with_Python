from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import re
import string
import pprint


def cleanInput(input):
    input = input.upper()
    input = re.sub('\n+', ' ', input)
    input = re.sub('\[[0-9]*\]', '', input)
    input = re.sub(' +', ' ', input)
    input = bytes(input, 'UTF-8')
    input = input.decode('ascii', 'ignore')
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower == 'i'):
            cleanInput.append(item)
    return cleanInput


def getNgrams(input, n):
    input = cleanInput(input)
    output = dict()
    for i in range(len(input) - n + 1):
        newNGram = ' '.join(input[i:i+n])
        if newNGram in output:
            output[newNGram] += 1
        else:
            output[newNGram] = 1
    return output


html = urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)')
bsObj = BeautifulSoup(html, 'html.parser')
content = bsObj.find('div', {'id': 'mw-content-text'}).get_text()
ngrams = getNgrams(content, 2)
ngrams = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))
pprint.pprint(ngrams)
print('2-grams count is: ' + str(len(ngrams)))

from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4 import re


html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
images = bsObj.findAll("img", {"src": re.compile("\.\./img/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])
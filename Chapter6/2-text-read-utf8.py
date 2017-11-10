from urllib.request import urlopen
textPage = urlopen(
    'http://www.pythonscraping.com/pags/warandpeace/chatper1-ru.txt')
print(str(textPage.read()), 'utf-8')

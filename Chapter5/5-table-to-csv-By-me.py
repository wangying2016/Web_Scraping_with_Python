import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors')
bsObj = BeautifulSoup(html, 'html.parser')

with open('test.csv', 'w+', newline='', encoding='utf-8') as csvFile:
    writer = csv.writer(csvFile)

    rows = bsObj.findAll('table', {'class': 'wikitable'})[0].findAll('tr')
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)








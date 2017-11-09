from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql
import re

conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       passwd='123456',
                       db='mysql',
                       charset='utf8')
cur = conn.cursor()
cur.execute('USE wikipedia')


# 这个函数要剔除的是两个情况：
# 1. 这个 url 没有记录过
# 2. 这个 url 记录过，并且存在 fromPageId 为该 url 的记录（为了防止 url 跳转到自己所以去掉）
def pageScraped(url):
    cur.execute('SELECT * FROM pages WHERE url = %s', url)
    if cur.rowcount == 0:
        return False
    page = cur.fetchone()

    cur.execute('SELECT * FROM links WHERE fromPageId = %s', int(page[0]))
    if cur.rowcount == 0:
        return False
    return True


def insertPageIfNotExists(url):
    cur.execute('SELECT * FROM pages WHERE url = %s', url)
    if cur.rowcount == 0:
        cur.execute('INSERT INTO pages (url) VALUES (%s)', url)
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]


def insertLink(fromPageId, toPageId):
    cur.execute('SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s',
                (int(fromPageId), int(toPageId)))
    if cur.rowcount == 0:
        cur.execute('INSERT INTO links (fromPageId, toPageId) VALUES (%s, %s)',
                    (int(fromPageId), int(toPageId)))
        conn.commit()


def getLinks(pageUrl, recursionLevel):
    if recursionLevel > 4:
        return
    pageId = insertPageIfNotExists(pageUrl)
    html = urlopen('https://en.wikipedia.org' + pageUrl)
    bsObj = BeautifulSoup(html, 'html.parser')
    for link in bsObj.findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')):
        insertLink(pageId, insertPageIfNotExists(link.attrs['href']))
        if not pageScraped(link.attrs['href']):
            # We have encountered a new page, add it and search it for links
            newPage = link.attrs['href']
            print(newPage)
            getLinks(newPage, recursionLevel + 1)
        else:
            print('Skipping: ' + str(link.attrs['href']) + ' found on ' + pageUrl)


getLinks('/wiki/Kevin_Bacon', 0)
cur.close()
conn.close()


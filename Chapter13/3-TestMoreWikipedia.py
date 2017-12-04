from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest


class TestWikipedia(unittest.TestCase):
    bsObj = None
    url = None

    def test_PageProperties(self):
        global bsObj
        global url

        url = 'https://en.wikipedia.org/wiki/Monty_Python'
        # Test the first 100 pages we encounter
        for i in range(1, 100):
            bsObj = BeautifulSoup(urlopen(url), 'lxml')
            titles = self.titleMatchesURL()
            self.assertEquals(titles[0], titles[1])
            self.assertTrue(self.contentExists())
            url = self.getNextLink()
        print('Done!')

    def titleMatchesURL(self):
        global bsObj
        global url
        pageTitle = bsObj.find('h1').get_text()
        urlTitle = url[(url.index('/wiki/')+6):]
        urlTitle = urlTitle.replace('_', ' ')
        urlTitle = unquote(urlTitle)
        return [pageTitle.lower(), urlTitle.lower()]

    def contentExists(self):
        global bsObj
        content = bsObj.find('div', {'id': 'mw-content-text'})
        if content is not None:
            return True
        return False

    def getNextLink(self):
        # Returns random link on page, using technique from chapter 5


if __name__ == '__main__':
    unittest.main()



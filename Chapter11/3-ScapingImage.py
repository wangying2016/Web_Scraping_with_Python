import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver


# Create new Selenium driver
driver = webdriver.PhantomJS(executable_path='PhantomJS.exe')
driver.get('http://www.amazon.com/War-Peace-Leo-Nikolyas')
time.sleep(2)

# Click on the book preview button
driver.find_element_by_id('sitbLogoImg').click()
imageList = set()

# Wait for the page to load
time.sleep(5)

# While the right arrow is available for clicking, turn through pages
while 'pointer' in dirver.find_element_by_id('sitReaderRightPageTurner'
                                             ).get_attribute('style'):
    driver.find_element_by_id('sitReaderRightPageTurner').click()
    time.sleep(2)

    # Get any new pages that have loaded(multiple pages can  load at once,
    # but duplicates will not be added to a set)
    pages = driver.find_elements_by_xpath('//div[@class="pageImage"]/div/img')
    for page in pages:
        image = page.get_attribute('src')
        imageList.add(image)

    driver.quit()

# Start processing the images we've collected URLs for with Tesseract
for image in sorted(imageList):
    urlretrieve(image, 'page.jpg')
    p = subproces.Popen(['tesseract', 'page.jpg', 'page'],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    f = open('page.txt', 'r')
    print(f.read())

from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='D:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
driver.get('https://en.wikipedia.org/wiki/Monty_Python')
assert 'Monty Python' in driver.title
driver.close()


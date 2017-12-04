from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='D:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
driver.implicitly_wait(5)
driver.get('https://github.com/wangying2016')
driver.get_screenshot_as_file('github.png')

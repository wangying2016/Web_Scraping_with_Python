from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.PhantomJS(executable_path='D:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
driver.get('http://pythonscraping.com/pages/files/form.html')

firstnameField = driver.find_element_by_name('firstname')
lastnameField = driver.find_element_by_name('lastname')
submitButton = driver.find_element_by_id('submit')

### METHOD 1 ###
firstnameField.send_keys('Ryan')
lastnameField.send_keys('Mitchell')
submitButton.click()
#################

### METHOD 2 ###
actions = ActionChains(driver
                       ).click(firstnameField).send_keys('Ryan'
                       ).click(lastnameField).send_keys('Michell'
                       ).send_keys(Keys.RETURN)
actions.perform()
#################

print(driver.find_element_by_tag_name('body').text)

driver.close()

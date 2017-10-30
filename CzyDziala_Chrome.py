import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.google.com/xhtml')
driver.maximize_window()
time.sleep(5)
driver.quit()
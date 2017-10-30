import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.python.org')
#driver.maximize_window()

time.sleep(2)
driver.close()
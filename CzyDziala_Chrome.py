import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.python.org')
driver.maximize_window()

time.sleep(2)

print ('Test PASSED')

driver.close()
import time
from selenium import webdriver

#driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.get('https://www.google.pl')
driver.maximize_window()

SearchField = driver.find_element_by_name('q')
SearchField.send_keys('fasola')

# Aby zwinac liste propozycji, klikamy w Logo Google
ClickOnLogo = driver.find_element_by_id('hplogo')
ClickOnLogo.click()

time.sleep(2)
przycisk = driver.find_element_by_name('btnK')
przycisk.click()

#time.sleep(2)

try:
    assert 'fasola - Szukaj w Google' in driver.title
    print ('Test PASSED')
finally:
    driver.close()

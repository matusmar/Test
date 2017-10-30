import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.pl')
driver.maximize_window()

PoleTekstowe = driver.find_element_by_name('q')

PoleTekstowe.send_keys('fasola')
#PoleTekstowe.submit()

KlikWLogo = driver.find_element_by_id('hplogo')
KlikWLogo.click()

print ('Kliknieto w Logo')
time.sleep(2)

przycisk = driver.find_element_by_name('btnK')
przycisk.click()

time.sleep(2)
try:
    assert "https://pl.wikipedia.org/wiki/Fasola" in driver.page_source
    print ('Test PASSED')
finally:
    time.sleep(2)
    driver.close()

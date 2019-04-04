from selenium import webdriver
from selenium.webdriver.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/usr/lib/firefox-esr/firefox-bin')
ff = webdriver.Firefox(firefox_binary=binary)

ff.get('http://google.com')
ff.find_element_by_id('lst-ib').send_keys('Programação funcional')
ff.find_element_by_id('_fZl').click()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("./drivers/chromedriver")
browser.get('https://www.linuxhint.com')
print('Title: %s' % browser.title)
browser.quit()
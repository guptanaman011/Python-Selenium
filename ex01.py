from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
chromeOptions = Options()
chromeOptions.add_argument("-headless")
browser = webdriver.Chrome("./drivers/chromedriver", options=chromeOptions)
browser.get('https://www.linuxhint.com')
print('Title: %s' % browser.title)
browser.quit()


# headless = without GUI
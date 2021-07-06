from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
chromeOptions = Options()
chromeOptions.add_argument("-headless")
browser = webdriver.Chrome("./drivers/chromedriver", options=chromeOptions)
browser.get('https://www.lipsum.com/feed/html')
lipsum = browser.find_element_by_id('lipsum')
print(lipsum.text)
browser.quit()


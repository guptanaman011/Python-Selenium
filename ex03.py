from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
chromeOptions = Options()
chromeOptions.add_argument("-headless")
browser = webdriver.Chrome("./drivers/chromedriver", options=chromeOptions)
browser.get('http://random-name-generator.info/')
listOfNames = browser.find_element_by_class_name('nameList')
print(listOfNames.text)
browser.quit()

# OR we can also write listOfNames = browser.find_elements_by_css_selector('div.results ol.nameList li')
# for name in listOfNames
# print(name.txt)
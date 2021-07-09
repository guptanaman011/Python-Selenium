from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
browser.get("https://www.instagram.com")
sleep(2)
browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys("your_username")

browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys("your_password")

browser.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button > div").click()
sleep(5)

element = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys("#puppies")
element.send


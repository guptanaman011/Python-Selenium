from selenium import webdriver
from time import sleep

browser = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
browser.get("https://en.wikipedia.org")
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
sleep(3)
browser.close()
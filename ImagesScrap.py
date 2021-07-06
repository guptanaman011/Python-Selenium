from selenium import webdriver

browser = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")

browser.get("https://www.instagram.com/explore/tags/puppies/")
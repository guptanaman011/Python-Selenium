from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
driver.get("https://www.instagram.com/")
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()

username.send_keys("cloud1234011")
password.send_keys("Cloud@123")

log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(2)
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
keyword = "#cat"
searchbox.send_keys(keyword)
my_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + keyword[1:] + "/')]")))
my_link.click()

n_scrolls = 3
for i in range(1, n_scrolls):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)

#select images
images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]
images = images[:-2] #slicing-off IG logo and Profile picture

print("Number of scrapped images: ", len(images))

#creating directory to store our images

import os
import wget

path = os.getcwd()
#path = os.path.join(path, hashtag)
path = os.path.join(path, keyword[1:] + "s")
os.mkdir(path)

counter = 0
for image in images:
    save_as = os.path.join(path, str(counter) + '.jpg')
    #save_as = os.path.join(path, hashtag + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1

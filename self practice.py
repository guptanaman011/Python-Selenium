from selenium import webdriver
from time import sleep

class instagramBot(object):
    def __init__(self, username, password):

        self.opts = webdriver.ChromeOptions()
        self.opts.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.opts,executable_path="./drivers/chromedriver.exe")
        self.username = username
        self.password = password

        self.driver.get("https://instagram.com")
        sleep(2)

        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(username)

        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)

user_name = "your_username"
password = "your_password"

instagramBot(user_name, password)


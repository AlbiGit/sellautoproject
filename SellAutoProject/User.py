from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
class User():
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
    def register(self):
        register = self.driver.find_element(By.ID, '#registration_btnundefined')
        register.click()

    def create(self,username,password,email):
        username = self.driver.find_element(By.NAME,'usernameRegisterPage')
        username.send_keys(username)

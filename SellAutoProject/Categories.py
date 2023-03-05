from selenium import webdriver
from selenium.webdriver.common.by import By
class Categories():
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
    def speakers(self):
        speakers = self.driver.find_element(By.CSS_SELECTOR, "#speakersImg")
        speakers.click()
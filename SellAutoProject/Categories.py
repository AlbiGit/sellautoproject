from selenium import webdriver
from selenium.webdriver.common.by import By
class Categories():
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
    def category_id(self,categoryid):
        if categoryid == 1:
            speakers = self.driver.find_element(By.CSS_SELECTOR, "#speakersImg")
            speakers.click()
        elif categoryid == 2:
            tablets = self.driver.find_element(By.CSS_SELECTOR, "#tabletsImg")
            tablets.click()
        elif categoryid == 3:
            headphones = self.driver.find_element(By.CSS_SELECTOR, "#headphonesImg")
            headphones.click()
        elif categoryid == 4:
            laptops = self.driver.find_element(By.CSS_SELECTOR, "#laptopsImg")
            laptops.click()
        elif categoryid == 5:
            mice = self.driver.find_element(By.CSS_SELECTOR, "#miceImg")
            mice.click()
        else:
            raise ValueError

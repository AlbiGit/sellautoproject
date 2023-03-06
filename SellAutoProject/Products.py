from selenium import webdriver
from selenium.webdriver.common.by import By
class Products():
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def product_select(self,pnum):
        plist = self.driver.find_elements(By.CLASS_NAME, 'imgProduct')
        plist[pnum].click()

    def product_add(self,anum):
        for i in range(anum):
            add = self.driver.find_element(By.CLASS_NAME, 'plus')
            self.driver.implicitly_wait(10)
            add.click()

    def product_cart(self):
        cart = self.driver.find_element(By.NAME, 'save_to_cart')
        cart.click()
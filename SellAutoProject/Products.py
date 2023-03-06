from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
class Products():
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def product_select(self,pnum):
        pnum-=1
        plist = self.driver.find_elements(By.CLASS_NAME, 'imgProduct')
        plist[pnum].click()

    def product_add(self,anum:int):
        anum -= 1
        for i in range(anum):
            add = self.driver.find_element(By.CLASS_NAME, 'plus')
            add.click()
        return anum+1

    def product_cart(self):
        cart = self.driver.find_element(By.NAME, 'save_to_cart')
        cart.click()
    def product_name(self):
        name = self.driver.find_element(By.CSS_SELECTOR, '.roboto-regular.screen768.ng-binding').text
        return name
    def product_price(self):
        price = self.driver.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > h2:nth-child(2)').text
        price = price.replace(',', '')
        return float(price[1:])
    # def product_colour(self):
    #     colour = self.driver.find_element(By.CSS_SELECTOR, 'div:nth-child(1) > div:nth-child(2) > span:nth-child(2)')
    #     return colour
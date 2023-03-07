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

    def product_price(self):
        price = self.driver.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > h2:nth-child(2)').text
        price = price.replace(',', '')
        return float(price[1:])

    def compare_product_in_cart(self,idp,pquantity,colour):
        idp -= 1
        plist = self.driver.find_elements(By.CLASS_NAME, 'imgProduct')
        plist[idp].click()
        pquantity -= 1
        for i in range(pquantity):
            add = self.driver.find_element(By.CLASS_NAME, 'plus')
            add.click()
        colour -= 1

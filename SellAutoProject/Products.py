from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
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

    def compare_product_in_cart(self,idp,pquantity):
        idp -= 1
        plist = self.driver.find_elements(By.CLASS_NAME, 'imgProduct')
        plist[idp].click()
        pquantity -= 1
        for i in range(pquantity):
            add = self.driver.find_element(By.CLASS_NAME, 'plus')
            add.click()
        cart = self.driver.find_element(By.NAME, 'save_to_cart')
        cart.click()
        sleep(1)
        name = self.driver.find_elements(By.CSS_SELECTOR, 'tbody tr:nth-child(1) td:nth-child(2) a:nth-child(1) h3:nth-child(1)')
        cart_name = self.driver.find_elements(By.CSS_SELECTOR, '.roboto-regular.screen768.ng-binding')
        quantity = self.driver.find_elements(By.CSS_SELECTOR, 'td:nth-child(2) > a:nth-child(1) > label:nth-child(2)')
        pcolour =  self.driver.find_elements(By.CSS_SELECTOR, 'label:nth-child(3) > span:nth-child(1)')
        cart_colour = self.driver.find_elements(By.CSS_SELECTOR, 'label:nth-child(3) > span:nth-child(1)')
        cart_price = self.driver.find_elements(By.CSS_SELECTOR, 'tbody tr:nth-child(1) td:nth-child(3) p:nth-child(1)')
        price = self.driver.find_elements(By.CSS_SELECTOR, 'div:nth-child(2) > h2:nth-child(2)')
        # print(name[0].text[:27],pquantity+1,pcolour[0].text,round(float(cart_price[0].text[1:])))
        # print(cart_name[0].text[:27],int(quantity[0].text[-1:]),cart_colour[0].text,round(float(price[0].text[1:])*float(quantity[0].text[-1:])))
        if name[0].text[:27] == cart_name[0].text[:27] and pquantity+1 == int(quantity[0].text[-1:]) and pcolour[0].text == cart_colour[0].text and round(float(cart_price[0].text[1:])) == round(float(price[0].text[1:])*float(quantity[0].text[-1:])):
            return 'match'
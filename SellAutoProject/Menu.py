from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
class Menu():
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def mouse_cart(self):
        action = ActionChains(self.driver)
        menu = self.driver.find_element(By.ID, 'menuCart')
        action.move_to_element(menu).perform()

    def get_total(self):
        total = 0
        items = self.driver.find_elements(By.CSS_SELECTOR, 'a:nth-child(1) > label:nth-child(2)')
        for i in range (len(items)):
            total += int(items[i].text[-1:])
        return total
    def get_cart_total(self):
        carttotal = self.driver.find_element(By.CSS_SELECTOR, 'span.roboto-medium.cart-total.ng-binding').text
        carttotal = carttotal.replace(',', '')
        return float(carttotal[1:])
    def cart_total_price(self):
        total = driver.find_element(By.CSS_SELECTOR, 'span.roboto-medium.cart-total.ng-binding').text
        return total(cartprice[1:])
    def list_cart(self):
        cartlist = self.driver.find_elements(By.CSS_SELECTOR, 'tbody:nth-child(1) > tr')
        return cartlist
    def remove_cart(self,item:int):
        remove = self.driver.find_elements(By.CSS_SELECTOR, 'div.removeProduct.iconCss.iconX')
        removeditem = self.driver.find_element(By.CSS_SELECTOR, 'tbody:nth-child(1) > tr:nth-child(1)').text
        remove[item-1].click()
        return removeditem
    def click_cart(self):
        cart = self.driver.find_element(By.ID, 'menuCart')
        cart.click()
    def edit_item(self,item):
        item -= 1
        edit = self.driver.find_elements(By.CSS_SELECTOR, "a.edit.ng-scope")
        edit[item].click()
    def cart_checkout(self):
        checkout = self.driver.find_element(By.XPATH, "(//button[@id='checkOutPopUp'])[1]")
        checkout.click()
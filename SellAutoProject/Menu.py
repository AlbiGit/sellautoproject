from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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

    def compate_total_cart(self):
        total
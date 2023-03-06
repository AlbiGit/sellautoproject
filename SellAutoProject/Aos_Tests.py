from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from Categories import Categories
from Products import Products
from Menu import Menu
class Aos_unittest(TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(r"C:\cell\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.implicitly_wait(10)
        self.category = Categories(self.driver)
        self.product = Products(self.driver)
        self.menu = Menu(self.driver)
    def test_speakers(self):
        self.category.speakers()

    def test_product_select(self):
        self.category.speakers()
        self.product.product_select(1)

    def test_product_add(self):
        self.category.speakers()
        self.product.product_select(1)
        self.product.product_add(1)

    def test_product_cart(self):
        self.category.speakers()
        self.product.product_select(1)
        self.product.product_add(1)
        self.product.product_cart()

    def test_mouse_cart(self):
        self.menu.mouse_cart()

    def test_get_total(self):
        self.category.speakers()
        self.product.product_select(1)
        self.product.product_add(1)
        self.product.product_cart()
        self.driver.back()
        self.product.product_select(2)
        self.product.product_add(2)
        self.product.product_cart()
        sleep(3)
        self.menu.mouse_cart()
        self.menu.get_total()
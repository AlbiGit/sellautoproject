from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from Categories import Categories
from Products import Products
from Menu import Menu
from User import User
class Aos_unittest(TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(r"C:\cell\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.implicitly_wait(10)
        self.category = Categories(self.driver)
        self.product = Products(self.driver)
        self.menu = Menu(self.driver)
        self.user = User(self.driver)
        self.list = []
    def test_one(self):
        self.category.category_id(1)
        self.product.product_select(1)
        self.product.product_add(1)
        self.product.product_cart()
        self.driver.back()
        self.product.product_select(2)
        self.product.product_add(2)
        self.product.product_cart()
        self.menu.mouse_cart()
        self.assertEqual(self.menu.get_total(),self.menu.get_cart_total())

    def test_two(self):
        self.category.category_id(2)
        self.product.product_select(1)
        self.product.product_cart()
        self.assertEqual(self.product.product_name(),self.menu.cart_name())
        self.assertEqual(self.product.product_quantity(),self.menu.cart_quantity())

    def test_three(self):
        self.category.category_id(1)
        self.product.product_select(1)
        self.product.product_add(1)
        self.product.product_cart()
        self.driver.back()
        self.product.product_select(2)
        self.product.product_add(2)
        self.product.product_cart()
        self.menu.mouse_cart()
        cart = self.menu.list_cart()
        item = self.menu.remove_cart(1)
        self.assertNotEqual(cart,self.menu.mouse_cart())
        self.assertNotIn(item,self.menu.list_cart())

    def test_four(self):
        self.category.category_id(1)
        self.product.product_select(1)
        self.product.product_add(1)
        self.product.product_cart()
        self.menu.click_cart()
        self.assertEqual(self.driver.find_element(By.XPATH, "//a[normalize-space()='SHOPPING CART']").text,"SHOPPING CART")

    def test_five(self):
        self.category.category_id(1)
        self.product.product_select(3)
        self.product.product_add(1)
        fnum = self.product.product_add(1)*self.product.product_price()
        self.product.product_cart()
        self.driver.back()
        self.product.product_select(1)
        self.product.product_add(3)
        self.product.product_cart()
        snum = self.product.product_add(3)*self.product.product_price()
        self.driver.back()
        self.driver.back()
        self.category.category_id(2)
        self.product.product_select(1)
        self.product.product_add(2)
        self.product.product_cart()
        tnum = self.product.product_add(2)*self.product.product_price()
        self.menu.mouse_cart()
        self.assertEqual(fnum+snum+tnum,self.menu.get_cart_total())
    def test_six(self):
        proone = 3
        protwo = 2
        editone = 2
        edittwo = 5
        self.category.category_id(1)
        self.product.product_select(3)
        self.product.product_add(proone)
        self.product.product_cart()
        self.driver.back()
        self.product.product_select(1)
        self.product.product_add(protwo)
        self.product.product_cart()
        self.menu.click_cart()
        self.menu.edit_item(1)
        self.product.product_add(editone)
        self.product.product_cart()
        self.menu.edit_item(2)
        self.product.product_add(edittwo)
        self.product.product_cart()
        self.assertEqual(self.menu.cart_quantity(1),editone)
        self.assertEqual(self.menu.cart_quantity(2),edittwo)

    def test_seven(self):
        self.category.category_id(2)
        self.product.product_select(3)
        self.product.product_cart()
        self.driver.back()
        self.assertEqual(self.driver.current_url,'https://www.advantageonlineshopping.com/#/category/Tablets/3')
        self.driver.back()
        self.assertEqual(self.driver.current_url, 'https://www.advantageonlineshopping.com/#/')

    def test_eight(self):
        self.category.category_id(2)
        self.product.product_select(3)
        self.product.product_cart()
        self.driver.back()
        self.category.category_id(1)
        self.product.product_select(3)
        self.product.product_add(2)
        self.product.product_cart()
        self.menu.mouse_cart()
        self.user.register()
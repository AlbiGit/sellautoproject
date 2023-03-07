from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from Categories import Categories
from Products import Products
from Menu import Menu
from User import User
from time import sleep
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
        itemone = 2
        itemtwo = 3
        self.category.category_id(1)
        self.driver.implicitly_wait(10)
        self.product.product_select(1)
        self.product.product_add(itemone)
        self.product.product_cart()
        self.driver.back()
        self.product.product_select(2)
        self.product.product_add(itemtwo)
        self.product.product_cart()
        sleep(2)
        self.assertEqual(self.menu.get_total(),itemone+itemtwo)

    def test_two(self):
        self.category.category_id(1)
        sleep(3)
        one = self.product.compare_product_in_cart(1, 2)
        self.driver.back()
        two = self.product.compare_product_in_cart(3, 5)
        self.driver.back()
        self.driver.back()
        self.category.category_id(3)
        three = self.product.compare_product_in_cart(1, 1)
        self.assertEqual(one,'match')
        self.assertEqual(two,'match')
        self.assertEqual(three,'match')
    def test_three(self):
        self.category.category_id(1)
        self.driver.implicitly_wait(10)
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
        self.assertEqual(self.menu.in_cart_quantity(1),editone)
        self.assertEqual(self.menu.in_cart_quantity(2),edittwo)

    def test_seven(self):
        self.category.category_id(2)
        self.product.product_select(3)
        self.product.product_cart()
        self.driver.back()
        self.assertEqual(self.driver.current_url,'https://www.advantageonlineshopping.com/#/category/Tablets/3')
        self.driver.back()
        self.assertEqual(self.driver.current_url, 'https://www.advantageonlineshopping.com/#/')


    def test_delete(self):
        self.user.delete_user('KetaKing420','300Rats')
    def test_eight(self):
        self.category.category_id(2)
        self.product.product_select(3)
        self.product.product_cart()
        self.driver.back()
        self.product.product_select(2)
        self.product.product_add(2)
        self.product.product_cart()
        self.menu.mouse_cart()
        self.list = self.menu.list_cart()
        self.menu.cart_checkout()
        self.user.register()
        sleep(1)
        self.user.create('KetaKing420','300Rats','crackpipes@sewers.groud')
        sleep(3)
        self.user.order_next()
        sleep(2)
        self.user.safepay('KetaKing420','300Rats')
        sleep(1)
        track = self.driver.find_element(By.CSS_SELECTOR, "#orderNumberLabel").text
        self.user.go_orders()
        sleep(1)
        torders = self.driver.find_elements(By.CSS_SELECTOR, "tbody>tr>td:nth-of-type(1)>label.ng-binding")
        self.assertEqual(track,torders[0].text)
        self.menu.click_cart()
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, 'label.roboto-bold.ng-scope').text,'Your shopping cart is empty')
        self.user.delete()

    def test_nine(self):
        self.category.category_id(1)
        sleep(1)
        self.product.product_select(3)
        self.product.product_cart()
        self.driver.back()
        self.product.product_select(1)
        self.product.product_add(2)
        self.product.product_cart()
        sleep(2)
        self.list = self.menu.list_cart()
        self.menu.cart_checkout()
        sleep(1)
        self.user.login_checkout()
        self.user.order_next()
        sleep(1)
        self.user.masterpay()
        sleep(1)
        track = self.driver.find_element(By.CSS_SELECTOR, "#orderNumberLabel").text
        sleep(1)
        self.user.go_orders()
        sleep(5)
        torders = self.driver.find_elements(By.CSS_SELECTOR, "tbody>tr>td:nth-of-type(1)>label.ng-binding")
        for i in range (len(torders)):
            if track == torders[i].text:
                torders = torders[i].text
        self.assertEqual(track,torders)
        self.menu.click_cart()
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, 'label.roboto-bold.ng-scope').text,'Your shopping cart is empty')

    def test_ten(self):
        username = 'Ratlord420'
        self.user.login('Ratlord420','Ratlord420')
        sleep(1)
        self.assertEqual(self.user.verify_login(),username)
        self.user.signout()
        self.assertNotEqual(self.user.verify_login(),username)

    def tearDown(self) -> None:
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        sleep(1)
        self.driver.quit()

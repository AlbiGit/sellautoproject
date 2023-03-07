from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
class User():
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
    def login_checkout(self):
        user = self.driver.find_element(By.NAME, 'usernameInOrderPayment')
        user.send_keys('Ratlord420')
        upass = self.driver.find_element(By.NAME, 'passwordInOrderPayment')
        upass.send_keys('Ratlord420')
        log = self.driver.find_element(By.ID, 'login_btnundefined')
        log.click()
    def register(self):
        register = self.driver.find_element(By.ID, 'registration_btnundefined')
        register.click()

    def create(self,username,password,email):
        name = self.driver.find_element(By.NAME,'usernameRegisterPage')
        name.send_keys(username)
        pword = self.driver.find_element(By.NAME,'passwordRegisterPage')
        pword.send_keys(password)
        pcword = self.driver.find_element(By.NAME,'confirm_passwordRegisterPage')
        pcword.send_keys(password)
        em = self.driver.find_element(By.NAME,'emailRegisterPage')
        em.send_keys(email)
        agree = self.driver.find_element(By.NAME,'i_agree')
        sleep(2)
        agree.click()
        self.driver.implicitly_wait(10)
        register = self.driver.find_element(By.ID, 'register_btnundefined')
        self.driver.implicitly_wait(10)
        register.click()

    def order_next(self):
        nexto = self.driver.find_element(By.ID, 'next_btn')
        nexto.click()

    def safepay(self,username,password):
        name = self.driver.find_element(By.NAME,'safepay_username')
        name.send_keys(username)
        pword = self.driver.find_element(By.NAME,'safepay_password')
        pword.send_keys(password)
        sleep(2)
        pay = self.driver.find_element(By.ID, 'pay_now_btn_SAFEPAY')
        pay.click()

    def masterpay(self):
        masterpay = self.driver.find_element(By.NAME, 'masterCredit')
        masterpay.click()
        pay = self.driver.find_element(By.ID, 'pay_now_btn_MasterCredit')
        pay.click()

    def go_orders(self):
        user = self.driver.find_element(By.ID, 'menuUserLink')
        user.click()
        sleep(1)
        usersettings = self.driver.find_element(By.XPATH, "//label[@role='link'][normalize-space()='My orders']")
        usersettings.click()
    def delete(self):
        user = self.driver.find_element(By.ID, 'menuUser')
        user.click()
        self.driver.implicitly_wait(10)
        usersettings = self.driver.find_elements(By.CSS_SELECTOR, 'label.option.roboto-medium.ng-scope')
        usersettings[1].click()
        delete = self.driver.find_element(By.CLASS_NAME,'deleteBtnText')
        delete.click()
        red = self.driver.find_element(By.CSS_SELECTOR,'.deletePopupBtn.deleteRed')
        red.click()

    def delete_user(self,username,password):
        user = self.driver.find_element(By.ID, 'menuUser')
        user.click()
        userw = self.driver.find_element(By.NAME, 'username')
        userw.send_keys(username)
        passw = self.driver.find_element(By.NAME, 'password')
        passw.send_keys(password)
        log = self.driver.find_element(By.ID, 'sign_in_btnundefined')
        log.click()
        sleep(1)
        user = self.driver.find_element(By.ID, 'menuUser')
        user.click()
        self.driver.implicitly_wait(10)
        usersettings = self.driver.find_elements(By.CSS_SELECTOR, 'label.option.roboto-medium.ng-scope')
        usersettings[1].click()
        delete = self.driver.find_element(By.CLASS_NAME,'deleteBtnText')
        delete.click()
        red = self.driver.find_element(By.CSS_SELECTOR,'.deletePopupBtn.deleteRed')
        red.click()
        sleep(2)

    def login(self,username,password):
        user = self.driver.find_element(By.ID, 'menuUser')
        user.click()
        userw = self.driver.find_element(By.NAME, 'username')
        userw.send_keys(username)
        passw = self.driver.find_element(By.NAME, 'password')
        passw.send_keys(password)
        log = self.driver.find_element(By.ID, 'sign_in_btnundefined')
        log.click()

    def verify_login(self):
        user = self.driver.find_element(By.CSS_SELECTOR,'.hi-user.containMiniTitle.ng-binding').text
        return user
    def signout(self):
        user = self.driver.find_element(By.ID, 'menuUser')
        user.click()
        sleep(1)
        usersettings = self.driver.find_elements(By.CSS_SELECTOR, 'label.option.roboto-medium.ng-scope')
        usersettings[-1].click()
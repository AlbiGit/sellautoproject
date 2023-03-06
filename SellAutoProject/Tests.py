from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from Categories import Categories
class Tests():
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
    def one(self):

        # speakers = driver.find_elements(By.CLASS_NAME, 'imgProduct')
        # speakers[0].click()
        #
        # add = driver.find_element(By.CLASS_NAME, 'plus')
        # driver.implicitly_wait(10)
        # add.click()

        # cart = driver.find_element(By.NAME, 'save_to_cart')
        # cart.click()

        driver.back()

        # speakers = driver.find_elements(By.CLASS_NAME, 'imgProduct')
        # speakers[1].click()
        #
        # add = driver.find_element(By.CLASS_NAME, 'plus')
        # add.click()
        # add.click()
        #
        # cart = driver.find_element(By.NAME, 'save_to_cart')
        # cart.click()

        # action = ActionChains(driver)
        # menu = driver.find_element(By.ID, 'menuCart')
        # action.move_to_element(menu).perform()

        # qpo = driver.find_elements(By.CSS_SELECTOR, ' a:nth-child(1) > label:nth-child(2)')
        # po = qpo[0].text
        #
        # qpt = driver.find_elements(By.CSS_SELECTOR, ' a:nth-child(1) > label:nth-child(2)')
        # pt = qpt[1].text

        total = driver.find_element(By.CSS_SELECTOR, 'label.roboto-regular.ng-binding').text
        sump = int(po[-1:]) + int(pt[-1:])

        if int(total[1]) == sump:
            print('v')
        else:
            print('x')
        sleep(3)

    def two(self):
        driver = webdriver.Chrome(r"C:\cell\chromedriver.exe")

        driver.get("https://www.advantageonlineshopping.com/#/")
        driver.implicitly_wait(10)
        driver.maximize_window()

        # click on category speakers
        category = driver.find_element(By.CSS_SELECTOR, "#speakersImg")
        category.click()

        # click on the speaker 1
        speakers = driver.find_elements(By.CLASS_NAME, 'imgProduct')
        speakers[0].click()

        # add 1 to Quantity(total=2)
        add = driver.find_element(By.CLASS_NAME, 'plus')
        driver.implicitly_wait(10)
        add.click()

        # click add to cart
        cart = driver.find_element(By.NAME, 'save_to_cart')
        cart.click()

        # go back
        driver.back()

        # click on the speaker 2
        speakers = driver.find_elements(By.CLASS_NAME, 'imgProduct')
        speakers[1].click()

        # add 2 to Quantity(total=3)
        add = driver.find_element(By.CLASS_NAME, 'plus')
        driver.implicitly_wait(10)
        add.click()
        add.click()

        # click add to cart
        cart = driver.find_element(By.NAME, 'save_to_cart')
        cart.click()

        # go back
        driver.back()

        # click on the speaker 3
        speakers = driver.find_elements(By.CLASS_NAME, 'imgProduct')
        speakers[2].click()

        # add 3 to Quantity(total=4)
        add = driver.find_element(By.CLASS_NAME, 'plus')
        driver.implicitly_wait(10)
        add.click()
        add.click()
        add.click()

        # click add to cart
        cart = driver.find_element(By.NAME, 'save_to_cart')
        cart.click()

        # open cart pop up window
        action = ActionChains(driver)
        menu = driver.find_element(By.ID, 'menuCart')
        action.move_to_element(menu).perform()

        # verify speaker 1 name
        if driver.find_element(By.XPATH,
                               "//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[3]/td[2]/a[1]/h3[1]").text == "BOSE SOUNDLINK BLUETOOTH SP...":
            print('speaker 1 name:', driver.find_element(By.XPATH,
                                                         "//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[3]/td[2]/a[1]/h3[1]").text)

        else:
            print("speaker 1 name error")

        # verify speaker 1 Quantity
        if driver.find_element(By.XPATH,
                               "//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[3]/td[2]/a[1]/label[1]").text == "QTY: 2":
            print('speaker 1 Quantity:', driver.find_element(By.XPATH,
                                                             "//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[3]/td[2]/a[1]/label[1]").text)
        else:
            print("speaker 1 Quantity error:")

        # verify speaker 1 color
        if driver.find_element(By.XPATH,
                               "//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[3]/td[2]/a[1]/label[2]/span[1]").text == "BLACK":
            print('speaker 1 color:', driver.find_element(By.XPATH,
                                                          "//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[3]/td[2]/a[1]/label[2]/span[1]").text)
        else:
            print("speaker 1 color error:")

        # verify speaker 1 price
        if driver.find_element(By.XPATH,
                               "//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[3]/td[3]/p[1]").text == "$539.98":
            print('speaker 1 price:', driver.find_element(By.XPATH,
                                                          "//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[3]/td[3]/p[1]").text)
        else:
            print("speaker 1 price error:")

        # verify speaker 2 name
        if driver.find_element(By.XPATH,
                               "//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/a[1]/h3[1]").text == "BOSE SOUNDLINK WIRELESS SPE...":
            print('speaker 2 name:', driver.find_element(By.XPATH,
                                                         "//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/a[1]/h3[1]").text)
        else:
            print("speaker 2 name error:")

        # verify speaker 2 Quantity
        if driver.find_element(By.XPATH,
                               "//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/a[1]/label[1]").text == "QTY: 3":
            print('speaker 2 Quantity:', driver.find_element(By.XPATH,
                                                             "//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/a[1]/label[1]").text)
        else:
            print("speaker 2 Quantity error:")

        # verify speaker 2 color
        if driver.find_element(By.XPATH,
                               "//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/a[1]/label[2]/span[1]").text == "TURQUOISE":
            print('speaker 2 color:', driver.find_element(By.XPATH,
                                                          "//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/a[1]/label[2]/span[1]").text)
        else:
            print("speaker 2 color error:")

        # verify speaker 2 price
        if driver.find_element(By.XPATH,
                               "//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/p[1]").text == "$387.00":
            print('speaker 2 price:', driver.find_element(By.XPATH,
                                                          "//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[3]/td[3]/p[1]").text)
        else:
            print("speaker 2 price error:")

        # verify speaker 3 name
        if driver.find_element(By.XPATH,
                               "//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[1]/h3[1]").text == "HP ROAR MINI WIRELESS SPEAKER":
            print('speaker 3 name:', driver.find_element(By.XPATH,
                                                         "//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[1]/h3[1]").text)
        else:
            print("speaker 3 name error:")

        # verify speaker 3 Quantity
        if driver.find_element(By.XPATH,
                               "//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[1]/label[1]").text == "QTY: 4":
            print('speaker 3 Quantity:', driver.find_element(By.XPATH,
                                                             "//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[1]/label[1]").text)
        else:
            print("speaker 3 Quantity error:")

        # verify speaker 3 color
        if driver.find_element(By.XPATH,
                               "//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[1]/label[2]/span[1]").text == "RED":
            print('speaker 3 color:', driver.find_element(By.XPATH,
                                                          "//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[1]/label[2]/span[1]").text)
        else:
            print("speaker 3 color error:")

        # verify speaker 3 price
        if driver.find_element(By.XPATH,
                               "//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/p[1]").text == "$179.96":
            print('speaker 3 price:', driver.find_element(By.XPATH,
                                                          "//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/p[1]").text)
        else:
            print("speaker 3 price error:")

        sleep(5)

    def three(self):
        driver = webdriver.Chrome(r"C:\cell\chromedriver.exe")

        driver.get("https://www.advantageonlineshopping.com/#/")
        driver.implicitly_wait(10)
        driver.maximize_window()

        category = driver.find_element(By.CSS_SELECTOR, "#speakersImg")
        category.click()

        speakers = driver.find_elements(By.CLASS_NAME, 'imgProduct')
        speakers[0].click()

        cart = driver.find_element(By.NAME, 'save_to_cart')
        cart.click()

        driver.back()

        speakers = driver.find_elements(By.CLASS_NAME, 'imgProduct')
        speakers[1].click()

        cart = driver.find_element(By.NAME, 'save_to_cart')
        cart.click()

        action = ActionChains(driver)
        menu = driver.find_element(By.ID, 'menuCart')
        action.move_to_element(menu).perform()

        cartlist = driver.find_elements(By.CSS_SELECTOR, 'tbody:nth-child(1) > tr')
        remove = driver.find_elements(By.CSS_SELECTOR, 'div.removeProduct.iconCss.iconX')
        removeditem = driver.find_element(By.CSS_SELECTOR, 'tbody:nth-child(1) > tr:nth-child(1)').text
        remove[0].click()

        updatedcart = driver.find_elements(By.CSS_SELECTOR, 'tbody:nth-child(1) > tr')
        updateditem = driver.find_element(By.CSS_SELECTOR, 'tbody:nth-child(1) > tr:nth-child(1)').text

        if cartlist != updatedcart and removeditem != updateditem:
            print('v')
        else:
            print('x')
        sleep(3)

    def four(self):
        driver = webdriver.Chrome(r"C:\cell\chromedriver.exe")

        driver.get("https://www.advantageonlineshopping.com/#/")
        driver.implicitly_wait(10)
        driver.maximize_window()

        # click on category speakers
        category = driver.find_element(By.CSS_SELECTOR, "#speakersImg")
        category.click()

        # click on the speaker 1
        speakers = driver.find_elements(By.CLASS_NAME, 'imgProduct')
        speakers[0].click()

        # add 1 to Quantity(total=2)
        add = driver.find_element(By.CLASS_NAME, 'plus')
        driver.implicitly_wait(10)
        add.click()

        # click add to cart
        cart = driver.find_element(By.NAME, 'save_to_cart')
        cart.click()

        # open cart page
        cart_page = driver.find_element(By.CSS_SELECTOR, "#menuCart")
        cart_page.click()

        # verify SHOPPING CART text on the path
        if driver.find_element(By.XPATH, "//a[normalize-space()='SHOPPING CART']").text == "SHOPPING CART":
            print('verify text:', driver.find_element(By.XPATH, "//a[normalize-space()='SHOPPING CART']").text)
        else:
            print("error:")

        sleep(5)

    def five(self):
        driver = webdriver.Chrome(r"C:\cell\chromedriver.exe")

        driver.get("https://www.advantageonlineshopping.com/#/")
        driver.implicitly_wait(10)
        driver.maximize_window()

        category = driver.find_element(By.CSS_SELECTOR, "#speakersImg")
        category.click()

        speakers = driver.find_elements(By.CLASS_NAME, 'imgProduct')
        speakers[0].click()

        cart = driver.find_element(By.NAME, 'save_to_cart')
        cart.click()
        fprice = driver.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > h2:nth-child(2)').text
        fprice = float(fprice[1:])
        driver.back()

        speakers = driver.find_elements(By.CLASS_NAME, 'imgProduct')
        speakers[1].click()

        add = driver.find_element(By.CLASS_NAME, 'plus')
        add.click()

        cart = driver.find_element(By.NAME, 'save_to_cart')
        cart.click()
        sprice = driver.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > h2:nth-child(2)').text
        sprice = float(sprice[1:])
        driver.back()

        speakers = driver.find_elements(By.CLASS_NAME, 'imgProduct')
        speakers[2].click()

        add = driver.find_element(By.CLASS_NAME, 'plus')
        add.click()
        add.click()

        cart = driver.find_element(By.NAME, 'save_to_cart')
        cart.click()
        tprice = driver.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > h2:nth-child(2)').text
        tprice = float(tprice[1:])

        action = ActionChains(driver)
        menu = driver.find_element(By.ID, 'menuCart')
        action.move_to_element(menu).perform()

        sumprice = fprice + 2 * sprice + 3 * tprice

        cartprice = driver.find_element(By.CSS_SELECTOR, 'span.roboto-medium.cart-total.ng-binding').text

        if sumprice == float(cartprice[1:]):
            print('v')
        else:
            print('x')
        sleep(3)

    def six(self):
        driver = webdriver.Chrome(r"C:\cell\chromedriver.exe")

        driver.get("https://www.advantageonlineshopping.com/#/")
        driver.implicitly_wait(10)
        driver.maximize_window()

        # click on category speakers
        category = driver.find_element(By.CSS_SELECTOR, "#speakersImg")
        category.click()

        # click on the speaker 1
        speakers = driver.find_elements(By.CLASS_NAME, 'imgProduct')
        speakers[0].click()

        # add 1 to Quantity(total=2)
        add = driver.find_element(By.CLASS_NAME, 'plus')
        driver.implicitly_wait(10)
        add.click()

        # click add to cart
        cart = driver.find_element(By.NAME, 'save_to_cart')
        cart.click()

        # go back
        driver.back()

        # click on the speaker 2
        speakers = driver.find_elements(By.CLASS_NAME, 'imgProduct')
        speakers[1].click()

        # add 2 to Quantity(total=3)
        add = driver.find_element(By.CLASS_NAME, 'plus')
        driver.implicitly_wait(10)
        add.click()
        add.click()

        # click add to cart
        cart = driver.find_element(By.NAME, 'save_to_cart')
        cart.click()

        # open cart page
        cart_page = driver.find_element(By.CSS_SELECTOR, "#menuCart")
        cart_page.click()

        # edit speaker 1
        driver.implicitly_wait(50)

        edits = driver.find_elements(By.CSS_SELECTOR, "a.edit.ng-scope")
        edits[0].click()

        add = driver.find_element(By.CLASS_NAME, 'plus')
        for i in range(4):
            add.click()

        # click add to cart
        add_button = driver.find_element(By.NAME, 'save_to_cart')
        add_button.click()

        sleep(1)
        edits = driver.find_elements(By.CSS_SELECTOR, "a.edit.ng-scope")
        edits[1].click()

        add = driver.find_element(By.CLASS_NAME, 'plus')
        for i in range(3):
            add.click()
        add_button = driver.find_element(By.NAME, 'save_to_cart')
        add_button.click()

        sleep(3)
    def seven(self):
        driver = webdriver.Chrome(r"C:\cell\chromedriver.exe")

        driver.get("https://www.advantageonlineshopping.com/#/")
        driver.implicitly_wait(10)
        driver.maximize_window()

        category = driver.find_element(By.CSS_SELECTOR, "#tabletsImg")
        category.click()

        speakers = driver.find_elements(By.CLASS_NAME, 'imgProduct')
        speakers[0].click()

        cart = driver.find_element(By.NAME, 'save_to_cart')
        cart.click()

        driver.back()

        turl = driver.current_url
        if turl == 'https://www.advantageonlineshopping.com/#/category/Tablets/3':
            print('v')
        else:
            print('x')
        driver.back()
        murl = driver.current_url
        if murl == 'https://www.advantageonlineshopping.com/#/':
            print('v')
        else:
            print('x')

        sleep(3)

    def eight(self):
        driver = webdriver.Chrome(r"C:\cell\chromedriver.exe")

        driver.get("https://www.advantageonlineshopping.com/#/")
        driver.implicitly_wait(10)
        driver.maximize_window()

        # click on category speakers
        category = driver.find_element(By.CSS_SELECTOR, "#speakersImg")
        category.click()

        # click on the speaker 1
        speakers = driver.find_elements(By.CLASS_NAME, 'imgProduct')
        speakers[0].click()

        # add 1 to Quantity(total=2)
        add = driver.find_element(By.CLASS_NAME, 'plus')
        driver.implicitly_wait(10)
        add.click()

        # click add to cart
        cart = driver.find_element(By.NAME, 'save_to_cart')
        cart.click()

        # open cart page
        cart_page = driver.find_element(By.CSS_SELECTOR, "#menuCart")
        cart_page.click()

        # click checkout
        checkout_button = driver.find_element(By.XPATH, "(//button[@id='checkOutPopUp'])[1]")
        checkout_button.click()

        # username
        username = driver.find_element(By.XPATH, "//input[@name='usernameInOrderPayment']")
        username.send_keys("ofek12")

        # password
        password = driver.find_element(By.XPATH, "//input[@name='passwordInOrderPayment']")
        password.send_keys("Ofek12")

        # click login
        driver.implicitly_wait(10)
        login = driver.find_element(By.CSS_SELECTOR, "#login_btnundefined")
        login.click()

        # click next
        next = driver.find_element(By.CSS_SELECTOR, "#next_btn")
        next.click()

        # SafePay username
        safepayuser = driver.find_element(By.CSS_SELECTOR, "input[name='safepay_username']")
        safepayuser.send_keys("ofek12")

        # SafePay password
        safepaypassword = driver.find_element(By.CSS_SELECTOR, "input[name='safepay_password']")
        safepaypassword.send_keys("Ofek12")

        # check if order completed
        driver.implicitly_wait(10)
        if driver.find_element(By.XPATH, "//h3[normalize-space()='ORDER PAYMENT']").text == "ORDER PAYMENT":
            print('verify text:', driver.find_element(By.XPATH, "//h3[normalize-space()='ORDER PAYMENT']").text)
        else:
            print("error:")

        # open cart page
        cart_page = driver.find_element(By.CSS_SELECTOR, "#menuCart")
        cart_page.click()

        # check that the cart is empty
        if driver.find_element(By.CSS_SELECTOR, ".roboto-bold.ng-scope").text == 'Your shopping cart is empty':
            print('verify text:', driver.find_element(By.CSS_SELECTOR, ".roboto-bold.ng-scope").text)
        else:
            print("cart is not empty:", driver.find_element(By.CSS_SELECTOR, ".roboto-bold.ng-scope").text)

        # click the user icon
        usericon = driver.find_element(By.CSS_SELECTOR, ".hi-user.containMiniTitle.ng-binding")
        username.click(driver.find_element(By.XPATH, "(//label[@role='link'][normalize-space()='My orders'])[1]"))

        sleep(5)

    def nine(self):
        driver = webdriver.Chrome(r"C:\cell\chromedriver.exe")

        driver.get("https://www.advantageonlineshopping.com/#/")
        driver.implicitly_wait(10)
        driver.maximize_window()

        category = driver.find_element(By.CSS_SELECTOR, "#speakersImg")
        category.click()

        speakers = driver.find_elements(By.CLASS_NAME, 'imgProduct')
        speakers[0].click()

        add = driver.find_element(By.CLASS_NAME, 'plus')
        driver.implicitly_wait(10)
        add.click()

        cart = driver.find_element(By.NAME, 'save_to_cart')
        cart.click()

        driver.back()

        speakers = driver.find_elements(By.CLASS_NAME, 'imgProduct')
        speakers[1].click()

        add = driver.find_element(By.CLASS_NAME, 'plus')
        add.click()
        add.click()

        cart = driver.find_element(By.NAME, 'save_to_cart')
        cart.click()

        action = ActionChains(driver)
        menu = driver.find_element(By.ID, 'menuCart')
        action.move_to_element(menu).perform()

        checkout = driver.find_elements(By.NAME, 'check_out_btn')
        checkout[0].click()

        user = driver.find_element(By.NAME, 'usernameInOrderPayment')
        user.send_keys('Ratlord420')

        upass = driver.find_element(By.NAME, 'passwordInOrderPayment')
        upass.send_keys('Ratlord420')

        log = driver.find_element(By.ID, 'login_btnundefined')
        log.click()

        next = driver.find_element(By.ID, 'next_btn')
        next.click()

        mstcr = driver.find_element(By.NAME, 'masterCredit')
        mstcr.click()

        pay = driver.find_element(By.ID, 'pay_now_btn_MasterCredit')
        pay.click()

        action = ActionChains(driver)
        menu = driver.find_element(By.ID, 'menuCart')
        action.move_to_element(menu).perform()
        sleep(1)
        ecart = driver.find_element(By.CSS_SELECTOR, 'label.center.roboto-medium.ng-scope').text
        if ecart == 'Your shopping cart is empty':
            print('v')
        else:
            print('x')
        sleep(3)

    def ten(self):
        driver = webdriver.Chrome(r"C:\cell\chromedriver.exe")

        driver.get("https://www.advantageonlineshopping.com/#/")
        driver.implicitly_wait(10)
        driver.maximize_window()

        # click on the user icon
        usericon = driver.find_element(By.CSS_SELECTOR, "#menuUserSVGPath")
        usericon.click()

        # username
        username = driver.find_element(By.XPATH, "//input[@name='username']")
        username.send_keys("ofek12")

        # password
        password = driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys("Ofek12")

        # click sign in
        signin = driver.find_element(By.CSS_SELECTOR, "#sign_in_btnundefined")
        signin.click()

        # # click account name
        # accountname=driver.find_elements(By.CSS_SELECTOR,"#hrefUserIcon" )
        # accountname[0].click()

        # click my account
        myaccount = driver.find_element(By.CSS_SELECTOR, "#menuUserLink")
        sleep(1)
        myaccount.click()
        driver.implicitly_wait(10)
        # action = ActionChains(driver)
        # action.move_to_element(myaccount).perform()
        menu = driver.find_elements(By.CSS_SELECTOR, 'label.option.roboto-medium.ng-scope')
        menu[1].click()

        # verify logging in
        if driver.find_element(By.XPATH, "//h3[normalize-space()='MY ACCOUNT']").text == "MY ACCOUNT":
            print("logged in:", driver.find_element(By.XPATH, "//h3[normalize-space()='MY ACCOUNT']").text)
        else:
            print("not logged in:", driver.find_element(By.XPATH, "//h3[normalize-space()='MY ACCOUNT']").text)

        # log out
        myaccount = driver.find_element(By.CSS_SELECTOR, "#menuUserLink")
        sleep(1)
        myaccount.click()
        driver.implicitly_wait(10)
        menu2 = driver.find_elements(By.XPATH, "//label[@role='link'][normalize-space()='Sign out']")
        menu2[0].click()

        # verify logged out
        usericon = driver.find_element(By.CSS_SELECTOR, "#menuUserSVGPath")
        sleep(3)
        usericon.click()
        sleep(4)
        driver.implicitly_wait(10)
        # print(driver.find_element(By.CSS_SELECTOR,".displayed").text)
        if driver.find_element(By.CSS_SELECTOR, ".displayed").text == "Username":
            print(driver.find_element(By.CSS_SELECTOR, ".displayed").text)
        else:
            print("not logged out")

        sleep(3)
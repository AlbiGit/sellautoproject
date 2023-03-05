from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
def testone():
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

    qpo = driver.find_elements(By.CSS_SELECTOR, ' a:nth-child(1) > label:nth-child(2)')
    po = qpo[0].text

    qpt = driver.find_elements(By.CSS_SELECTOR, ' a:nth-child(1) > label:nth-child(2)')
    pt = qpt[1].text

    total = driver.find_element(By.CSS_SELECTOR, 'label.roboto-regular.ng-binding').text
    sump = int(po[-1:]) + int(pt[-1:])

    if int(total[1]) == sump:
        print('v')
    else:
        print('x')
    sleep(3)
def testthree():
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


def testfive():
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

    add = driver.find_element(By.CLASS_NAME,'plus')
    add.click()

    cart = driver.find_element(By.NAME, 'save_to_cart')
    cart.click()
    sprice = driver.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > h2:nth-child(2)').text
    sprice = float(sprice[1:])
    driver.back()

    speakers = driver.find_elements(By.CLASS_NAME, 'imgProduct')
    speakers[2].click()

    add = driver.find_element(By.CLASS_NAME,'plus')
    add.click()
    add.click()

    cart = driver.find_element(By.NAME, 'save_to_cart')
    cart.click()
    tprice = driver.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > h2:nth-child(2)').text
    tprice = float(tprice[1:])

    action = ActionChains(driver)
    menu = driver.find_element(By.ID, 'menuCart')
    action.move_to_element(menu).perform()

    sumprice = fprice+2*sprice+3*tprice

    cartprice = driver.find_element(By.CSS_SELECTOR, 'span.roboto-medium.cart-total.ng-binding').text

    if sumprice == float(cartprice[1:]):
        print('v')
    else:
        print('x')
    sleep(3)

def testseven():
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

def testnine():
    driver = webdriver.Chrome(r"C:\cell\chromedriver.exe")

    driver.get("https://www.advantageonlineshopping.com/#/")
    driver.implicitly_wait(10)
    driver.maximize_window()

    category = driver.find_element(By.CSS_SELECTOR,"#speakersImg")
    category.click()

    speakers = driver.find_elements(By.CLASS_NAME,'imgProduct')
    speakers[0].click()

    add = driver.find_element(By.CLASS_NAME,'plus')
    driver.implicitly_wait(10)
    add.click()

    cart = driver.find_element(By.NAME, 'save_to_cart')
    cart.click()

    driver.back()

    speakers = driver.find_elements(By.CLASS_NAME,'imgProduct')
    speakers[1].click()

    add = driver.find_element(By.CLASS_NAME,'plus')
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

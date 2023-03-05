from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
def testone():
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
    total = driver.find_element(By.CSS_SELECTOR, 'label.roboto-regular.ng-binding').text

    if int(total[1]) == 5:
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
    print(fprice[1:])
    driver.back()

    speakers = driver.find_elements(By.CLASS_NAME, 'imgProduct')
    speakers[1].click()

    add = driver.find_element(By.CLASS_NAME,'plus')
    add.click()

    cart = driver.find_element(By.NAME, 'save_to_cart')
    cart.click()
    sprice = driver.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > h2:nth-child(2)').text
    print(sprice[1:])
    driver.back()

    speakers = driver.find_elements(By.CLASS_NAME, 'imgProduct')
    speakers[2].click()

    add = driver.find_element(By.CLASS_NAME,'plus')
    add.click()
    add.click()

    cart = driver.find_element(By.NAME, 'save_to_cart')
    cart.click()
    tprice = driver.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > h2:nth-child(2)').text
    print(tprice[1:])

    action = ActionChains(driver)
    menu = driver.find_element(By.ID, 'menuCart')
    action.move_to_element(menu).perform()

    sleep(3)

testfive()
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

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

sleep(5)
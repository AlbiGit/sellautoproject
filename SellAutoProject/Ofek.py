from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(r"C:\cell\chromedriver.exe")

# open site
driver.get("https://www.advantageonlineshopping.com/#/")
driver.implicitly_wait(10)
driver.maximize_window()

# click on category speakers
category = driver.find_element(By.CSS_SELECTOR,"#speakersImg")
category.click()

# click on the speaker 1
speakers = driver.find_elements(By.CLASS_NAME,'imgProduct')
speakers[0].click()

# add 1 to Quantity(total=2)
add = driver.find_element(By.CLASS_NAME,'plus')
driver.implicitly_wait(10)
add.click()

# click add to cart
cart = driver.find_element(By.NAME, 'save_to_cart')
cart.click()

# go back
driver.back()

# click on the speaker 2
speakers = driver.find_elements(By.CLASS_NAME,'imgProduct')
speakers[1].click()

# add 2 to Quantity(total=3)
add = driver.find_element(By.CLASS_NAME,'plus')
driver.implicitly_wait(10)
add.click()
add.click()

# click add to cart
cart = driver.find_element(By.NAME, 'save_to_cart')
cart.click()

# go back
driver.back()

# click on the speaker 3
speakers = driver.find_elements(By.CLASS_NAME,'imgProduct')
speakers[2].click()

# add 3 to Quantity(total=4)
add = driver.find_element(By.CLASS_NAME,'plus')
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
if driver.find_element(By.XPATH,"//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[3]/td[2]/a[1]/h3[1]").text=="BOSE SOUNDLINK BLUETOOTH SP...":
    print('speaker 1 name:',driver.find_element(By.XPATH,"//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[3]/td[2]/a[1]/h3[1]").text)

else:
    print("speaker 1 name error")

# verify speaker 1 Quantity
if driver.find_element(By.XPATH,"//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[3]/td[2]/a[1]/label[1]").text=="QTY: 2":
    print('speaker 1 Quantity:',driver.find_element(By.XPATH,"//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[3]/td[2]/a[1]/label[1]").text)
else:
    print("speaker 1 Quantity error:")

# verify speaker 1 color
if driver.find_element(By.XPATH,"//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[3]/td[2]/a[1]/label[2]/span[1]").text=="BLACK":
    print('speaker 1 color:',driver.find_element(By.XPATH,"//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[3]/td[2]/a[1]/label[2]/span[1]").text)
else:
    print("speaker 1 color error:")

# verify speaker 1 price
if driver.find_element(By.XPATH,"//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[3]/td[3]/p[1]").text=="$539.98":
    print('speaker 1 price:',driver.find_element(By.XPATH,"//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[3]/td[3]/p[1]").text)
else:
    print("speaker 1 price error:")


# verify speaker 2 name
if driver.find_element(By.XPATH,"//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/a[1]/h3[1]").text=="BOSE SOUNDLINK WIRELESS SPE...":
    print('speaker 2 name:',driver.find_element(By.XPATH,"//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/a[1]/h3[1]").text)
else:
    print("speaker 2 name error:")

# verify speaker 2 Quantity
if driver.find_element(By.XPATH,"//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/a[1]/label[1]").text=="QTY: 3":
    print('speaker 2 Quantity:',driver.find_element(By.XPATH,"//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/a[1]/label[1]").text)
else:
    print("speaker 2 Quantity error:")

# verify speaker 2 color
if driver.find_element(By.XPATH,"//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/a[1]/label[2]/span[1]").text=="TURQUOISE":
    print('speaker 2 color:',driver.find_element(By.XPATH,"//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/a[1]/label[2]/span[1]").text)
else:
    print("speaker 2 color error:")

# verify speaker 2 price
if driver.find_element(By.XPATH,"//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/p[1]").text=="$387.00":
    print('speaker 2 price:',driver.find_element(By.XPATH,"//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[3]/td[3]/p[1]").text)
else:
    print("speaker 2 price error:")

# verify speaker 3 name
if driver.find_element(By.XPATH,"//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[1]/h3[1]").text=="HP ROAR MINI WIRELESS SPEAKER":
    print('speaker 3 name:',driver.find_element(By.XPATH,"//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[1]/h3[1]").text)
else:
    print("speaker 3 name error:")

# verify speaker 3 Quantity
if driver.find_element(By.XPATH,"//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[1]/label[1]").text=="QTY: 4":
    print('speaker 3 Quantity:',driver.find_element(By.XPATH,"//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[1]/label[1]").text)
else:
    print("speaker 3 Quantity error:")

# verify speaker 3 color
if driver.find_element(By.XPATH,"//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[1]/label[2]/span[1]").text=="RED":
    print('speaker 3 color:',driver.find_element(By.XPATH,"//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[1]/label[2]/span[1]").text)
else:
    print("speaker 3 color error:")

# verify speaker 3 price
if driver.find_element(By.XPATH,"//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/p[1]").text=="$179.96":
    print('speaker 3 price:',driver.find_element(By.XPATH,"//body[1]/header[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/tool-tip-cart[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/p[1]").text)
else:
    print("speaker 3 price error:")


sleep(5)

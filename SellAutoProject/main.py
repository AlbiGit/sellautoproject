from selenium import webdriver
from Tests import Tests
from Products import Products

driver = webdriver.Chrome(r"C:\cell\chromedriver.exe")

driver.get("https://www.advantageonlineshopping.com/#/")
driver.implicitly_wait(10)
driver.maximize_window()




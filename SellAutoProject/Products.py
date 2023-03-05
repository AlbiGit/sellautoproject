from selenium import webdriver
from selenium.webdriver.common.by import By
class Products():
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

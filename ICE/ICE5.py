# Date: Nov 13, 2025
# Name: ICE5.py - ICE5
# Programmer:  Lucas
# Description: Using Selenium framework and WebDriver to register
# and login to a travel website.

# Selectors ["id", "xpath", "link text", "partial link text", "name",
# Resources "tag name", "class name", "css selector"]

from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Ice5TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.maximize_window()
        sleep(2) # wait for opening

    def test01_reg(self):
        self.browser.get("http://demo.guru99.com/test/newtours")
        self.browser.find_element(By.LINK_TEXT, "REGISTER").click()
        self.browser.find_element(By.NAME, "firstName").send_keys("Lucas")
        self.browser.find_element(By.NAME, "lastName").send_keys("Doe")
        self.browser.find_element(By.NAME, "phone").send_keys("123456789")
        self.browser.find_element(By.NAME, "userName").send_keys("lucas@dcmail.ca")
        self.browser.find_element(By.NAME, "address1").send_keys("2000 Simcoe Street North") # max length 60 char
        self.browser.find_element(By.NAME, "city").send_keys("Tokyo")
        self.browser.find_element(By.NAME, "state").send_keys("ON")
        self.browser.find_element(By.NAME, "postalCode").send_keys("L1G0C5")
        # --- dropdown select canada ---
        dropdown = self.browser.find_element(By.XPATH, "//select[@name='country']")
        select = Select(dropdown)
        select.select_by_visible_text("CANADA")
        # ----
        self.browser.find_element(By.ID, "email").send_keys("lucasusername")
        self.browser.find_element(By.NAME, "password").send_keys("Password1234")
        self.browser.find_element(By.NAME, "confirmPassword").send_keys("Password1234")
        sleep(2) # wait for submitting for verification
        self.browser.find_element(By.NAME, "submit").submit()
        
    def test02_login(self):
        self.browser.get("http://demo.guru99.com/test/newtours")
        self.browser.find_element(By.NAME, "userName").send_keys("lucasusername")
        self.browser.find_element(By.NAME, "password").send_keys("Password1234")
        sleep(2) # wait for submitting for verification
        self.browser.find_element(By.NAME, "submit").submit()
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
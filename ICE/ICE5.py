from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Ice5TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.browser.maximize_window()
        sleep(2)

    def test_reg(self):
        self.browser.get("http://demo.guru99.com/test/newtours")
        self.browser.find_element(By.LINK_TEXT, "REGISTER").click()
        self.browser.find_element(By.NAME, "firstName").send_keys("Lucas")
        self.browser.find_element(By.NAME, "lastName").send_keys("Doe")
        self.browser.find_element(By.NAME, "phone").send_keys("123456789")
        self.browser.find_element(By.NAME, "userName").send_keys("lucas@gmail.com")
        self.browser.find_element(By.NAME, "address1").send_keys("123 Sesame St")
        self.browser.find_element(By.NAME, "city").send_keys("Tokyo")
        self.browser.find_element(By.NAME, "state").send_keys("ON")
        self.browser.find_element(By.NAME, "postalCode").send_keys("m1E3d5")
        self.browser.find_element(By.XPATH, "//option[contains(text(),'CANADA')]").click()
        self.browser.find_element(By.ID, "email").send_keys("lucas@gmail")
        self.browser.find_element(By.NAME, "password").send_keys("Password1234")
        self.browser.find_element(By.NAME, "confirmPassword").send_keys("Password1234")
        self.browser.find_element(By.NAME, "submit").click()

    def test_login(self):
        self.browser.get("http://demo.guru99.com/test/newtours")
        self.browser.find_element(By.LINK_TEXT, "SIGN-ON").click()
        self.browser.find_element(By.NAME, "userName").send_keys("lucas@gmail.com")
        self.browser.find_element(By.NAME, "password").send_keys("Password1234")
        self.browser.find_element(By.NAME, "submit").click()

"""
        target = self.browser.find_element(By.CSS_SELECTOR, "h3")
        self.assertEqual("Login Successfully", target.text)
"""

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
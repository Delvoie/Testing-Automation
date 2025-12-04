# Date: Nov 29, 2025
# Name: Module7.py - Group Project
# Programmers:  Lucas Delvoie
# Description: Lucas' section for Group Project module 7 test cases 1-7

import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Module7TestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        time.sleep(2) # wait for opening

    def setUp(self):
        self.driver.get("http://demo.guru99.com/V4/")
        self.driver.find_element(By.NAME, "uid").send_keys("mngr647644") # Lucas' id and password
        self.driver.find_element(By.NAME, "password").send_keys("tyvAseg")
        self.driver.find_element(By.NAME, "btnLogin").click()
        time.sleep(2) # wait for login

    # Test Cases for Delete Customer
    def test_DC1(self):


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()



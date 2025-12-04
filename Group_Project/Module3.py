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
        self.driver.find_element(By.NAME, "uid").send_keys("mngr647644") # Alyssa's id and password
        self.driver.find_element(By.NAME, "password").send_keys("tyvAseg")
        self.driver.find_element(By.NAME, "btnLogin").click()
        time.sleep(2) # wait for login

    # Test Cases for Delete Customer
    def test_03_delete_customer(self):
        # DC 1
        self.browser.find_element(By.LINK_TEXT, "Delete Customer").click()
        self.browser.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        self.assertEqual(self.browser.find_element(By.ID, "message14").text, "Customer ID is required")
        print("DC 1 Successful")

        # DC 2
        self.browser.find_element(By.NAME, "cusid").send_keys("1234Acc123")
        self.assertEqual(self.browser.find_element(By.ID, "message14").text, "Characters are not allowed")
        print("DC 2 Successful")

        # DC 3
        self.browser.find_element(By.NAME, "cusid").clear()
        self.browser.find_element(By.NAME, "cusid").send_keys("123!@#!@#")
        self.assertEqual(self.browser.find_element(By.ID, "message14").text, "Special characters are not allowed")
        print("DC 3 Successful")

        # DC 4
        self.browser.find_element(By.NAME, "cusid").clear()
        self.browser.find_element(By.NAME, "cusid").send_keys("123 12")
        self.assertEqual(self.browser.find_element(By.ID, "message14").text, "Characters are not allowed")
        print("DC 4 Successful")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()



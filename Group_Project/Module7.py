# Date: Nov 29, 2025
# Name: Module7.py - Group Project
# Programmers:  Lucas Delvoie
# Description: Lucas' section for Group Project module 7 test cases 1-7


import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Lab4TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        time.sleep(2) # wait for opening

    def setUp(self):
        self.driver.get("http://demo.guru99.com/V4/")
        self.driver.find_element(By.NAME, "uid").send_keys("mngr647644")
        self.driver.find_element(By.NAME, "password").send_keys("tyvAseg")
        self.driver.find_element(By.NAME, "btnLogin").click()
        time.sleep(2) # wait for login

    def test_BE1(self):
        element = self.driver.find_element(By.LINK_TEXT, "Balance Enquiry")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2) # wait for page load
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        self.assertEqual(self.driver.find_element(By.ID, "message2").text, "Account Number must not be blank")
        print("Test BE1 passed")
    def test_BE2(self):
        element = self.driver.find_element(By.LINK_TEXT, "Balance Enquiry")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2) # wait for page load
        self.driver.find_element(By.NAME, "accountno").send_keys("1234Acc123")
        self.assertEqual(self.driver.find_element(By.ID, "message2").text, "Characters are not allowed")
        print("Test BE2 passed")
    def test_BE3(self):
        element = self.driver.find_element(By.LINK_TEXT, "Balance Enquiry")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2) # wait for page load
        self.driver.find_element(By.NAME, "accountno").send_keys("23!@#!@#")
        self.assertEqual(self.driver.find_element(By.ID, "message2").text, "Special characters are not allowed")
        print("Test BE3 passed")
    def test_BE4(self):
        element = self.driver.find_element(By.LINK_TEXT, "Balance Enquiry")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2) # wait for page load
        self.driver.find_element(By.NAME, "accountno").send_keys(" " + Keys.TAB)
        errorhandling = self.driver.find_element(By.ID, "message2").text
        print(errorhandling)
        print("Test BE4 Failed: Bug Found (Leading space not detected)")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

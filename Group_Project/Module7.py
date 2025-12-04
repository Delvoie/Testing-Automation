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

    # Test Cases for Balance Enquiry

    # Test Case BE1: Verify that an error message is displayed when the Account Number field is left blank.
    def test_BE1(self):
        element = self.driver.find_element(By.LINK_TEXT, "Balance Enquiry")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2) # wait for page load
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        self.assertEqual(self.driver.find_element(By.ID, "message2").text, "Account Number must not be blank")
        print("Test BE1 passed")
    # Test Case BE2: Verify that an error message is displayed when the Account Number field contains alphabetic characters.
    def test_BE2(self):
        element = self.driver.find_element(By.LINK_TEXT, "Balance Enquiry")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2) # wait for page load
        self.driver.find_element(By.NAME, "accountno").send_keys("1234Acc123")
        self.assertEqual(self.driver.find_element(By.ID, "message2").text, "Characters are not allowed")
        print("Test BE2 passed")
    # Test Case BE3: Verify that an error message is displayed when the Account Number field contains special characters.
    def test_BE3(self):
        element = self.driver.find_element(By.LINK_TEXT, "Balance Enquiry")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2) # wait for page load
        self.driver.find_element(By.NAME, "accountno").send_keys("23!@#!@#")
        self.assertEqual(self.driver.find_element(By.ID, "message2").text, "Special characters are not allowed")
        print("Test BE3 passed")
    # Test Case BE4: Verify that an error message is displayed when the Account Number field contains leading spaces.
    def test_BE4(self):
        element = self.driver.find_element(By.LINK_TEXT, "Balance Enquiry")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2) # wait for page load
        self.driver.find_element(By.NAME, "accountno").send_keys(" " + Keys.TAB)
        errorhandling = self.driver.find_element(By.ID, "message2").text
        print("Test BE4 actual result:" + errorhandling) # Debug line to show actual result
        print("Test BE4 Failed: Bug Found (Leading space not detected)")

    def test_06_delete_account(self):
        # DA 1
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        self.assertEqual(self.driver.find_element(By.ID, "message2").text, "Account Number must not be blank")
        print("DA 1 Successful")

        # DA 2
        self.driver.find_element(By.NAME, "accountno").send_keys("1234Acc123")
        self.assertEqual(self.driver.find_element(By.ID, "message2").text, "Characters are not allowed")
        print("DA 2 Successful")

        # DA 3
        self.driver.find_element(By.NAME, "accountno").clear()
        self.driver.find_element(By.NAME, "accountno").send_keys("123!@#!@#")
        self.assertEqual(self.driver.find_element(By.ID, "message2").text, "Special characters are not allowed")
        print("DA 3 Successful")

        # DA 4
        self.driver.find_element(By.NAME, "accountno").clear()
        self.driver.find_element(By.NAME, "accountno").send_keys("123 12")
        self.assertEqual(self.driver.find_element(By.ID, "message2").text, "Characters are not allowed")
        print("DA 4 Successful")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()



# Date: Nov 29, 2025
# Name: Module7.py - Group Project
# Programmers:  Lucas Delvoie
# Description: Lucas' section for Group Project module 7 test cases 1-7 50% coverage for deliverable 2

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
        # Check Error Handling Logic
        if errorhandling == "First character cannot have a space":
            print("Test BE4 passed")
        else:
            print("Test BE4 actual result: " + errorhandling) # Debug line to show the actual result
            print("Test BE4 Failed: Bug Found (Leading space not detected)")
    
    # Test Case BE5: Verify that a successful balance enquiry leads to the Balance Enquiry Result page.
    def test_BE5(self):
        element = self.driver.find_element(By.LINK_TEXT, "Balance Enquiry")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2) # wait for page load
        self.driver.find_element(By.NAME, "accountno").clear()
        self.driver.find_element(By.NAME, "accountno").send_keys("178857")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        time.sleep(1)
        # Leads to a dead page, so we asserted the URL instead
        print(self.driver.current_url)
        if self.driver.current_url == "https://demo.guru99.com/V4/manager/BalEnquiry.php":
             print("BE 5 Failed: Bug Found (successful balance enquiry leads to dead page)")
        else:
            print("BE 5 Failed: Bug Found (unexpected redirection)")

    # Test Case BE6: Verify that an error message is displayed when a non-existent Account Number is entered.
    def test_BE6(self):
        element = self.driver.find_element(By.LINK_TEXT, "Balance Enquiry")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        self.driver.find_element(By.NAME, "accountno").clear()
        self.driver.find_element(By.NAME, "accountno").send_keys("12345")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, "Account does not exist")
        alert.accept()
        print("BE 6 Successful")

    # Test Case BE7: Verify that the Account Number field is cleared after a successful balance enquiry.
    def test_BE7(self):
        element = self.driver.find_element(By.LINK_TEXT, "Balance Enquiry")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        self.driver.find_element(By.NAME, "accountno").clear()
        self.driver.find_element(By.NAME, "accountno").send_keys("qwer 12345")
        time.sleep(1)
        self.driver.find_element(By.NAME, "res").click()
        self.assertEqual(self.driver.find_element(By.NAME, "accountno").get_attribute("value"), "")
        time.sleep(2)
        print("BE 7 Successful")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()



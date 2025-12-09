# Date: Nov 30, 2025
# Name: Module3.py - Group Project
# Programmers:  Alyssa
# Description: Alyssa's section for Group Project module 3 test cases 1-7 50% coverage for deliverable 2

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
        self.driver.find_element(By.NAME, "uid").send_keys("mngr647648") # Alyssa's id and password
        self.driver.find_element(By.NAME, "password").send_keys("vUnuguz")
        self.driver.find_element(By.NAME, "btnLogin").click()
        time.sleep(2) # wait for login

# Test Cases for Delete Customer

    def test_03_delete_customer(self):
        # test Case DC 1: Verify that an error message is displayed when the Customer ID field is left blank.
        self.driver.find_element(By.LINK_TEXT, "Delete Customer").click()
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        self.assertEqual(self.driver.find_element(By.ID, "message14").text, "Customer ID is required")
        print("DC 1 Successful")

        # test Case DC 2: Verify that an error message is displayed when the Customer ID field contains alphabetic characters.
        self.driver.find_element(By.NAME, "cusid").send_keys("1234Acc123")
        self.assertEqual(self.driver.find_element(By.ID, "message14").text, "Characters are not allowed")
        print("DC 2 Successful")

        # test case DC 3: Verify that an error message is displayed when the Customer ID field contains special characters.
        self.driver.find_element(By.NAME, "cusid").clear()
        self.driver.find_element(By.NAME, "cusid").send_keys("123!@#!@#")
        self.assertEqual(self.driver.find_element(By.ID, "message14").text, "Special characters are not allowed")
        print("DC 3 Successful")

        # test case DC 4: Verify that an error message is displayed when the Customer ID field contains spaces.
        self.driver.find_element(By.NAME, "cusid").clear()
        self.driver.find_element(By.NAME, "cusid").send_keys("123 12")
        self.assertEqual(self.driver.find_element(By.ID, "message14").text, "Characters are not allowed")
        print("DC 4 Successful")

        # test


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()



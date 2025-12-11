# ------------------------------------
# Author: Alyssa Cipriani
# Date: December 9, 2025
# Description: Using Selenium WebDriver 
# to script for Delete Customer.
# ------------------------------------

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 

class TestDeleteCustomer(unittest.TestCase):
    '''Module: Delete Customer'''

    def setUp(self):
        # Setup
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
        # Login
        self.driver.get("http://demo.guru99.com/V4/")
        self.driver.find_element(By.NAME, "uid").send_keys("mngr647648")
        self.driver.find_element(By.NAME, "password").send_keys("vUnuguz")
        self.driver.find_element(By.NAME, "btnLogin").click()
        
        # Delete customer
        self.driver.find_element(By.LINK_TEXT, "Delete Customer").click()
        time.sleep(1)

    def tearDown(self):
        # Restart
        self.driver.quit()


    # Test Cases

    def verify_customer_id_empty(self):
        ''' Customer ID cannot be empty'''
        print("Customer ID Empty")
        
        input_box = self.driver.find_element(By.NAME, "cusid")
        input_box.click()
        input_box.send_keys(Keys.TAB) 
        page_content = self.driver.page_source
        if "Customer ID can not be blank" in page_content:
            print("PASS: Found Customer ID can not be blank")
        else:
            print("FAIL: Validation message not found.")

    def must_be_numeric(self):
        '''Customer ID must be numeric'''
        print("Numeric Validation")
        
        input_box = self.driver.find_element(By.NAME, "cusid")
        input_box.send_keys("1234Acc123") 
        
        page_content = self.driver.page_source
        if "Characters are not allowed" in page_content:
            print("PASS: Found Characters are not allowed")
        else:
            print("FAIL: Validation message not found.")

    def no_special_characters(self):
        '''Customer ID cannot have special characters'''
        print("Special Character Validation")
        
        input_box = self.driver.find_element(By.NAME, "cusid")
        input_box.send_keys("123!@#") 
        
        page_content = self.driver.page_source
        if "Special characters are not allowed" in page_content:
            print("PASS: Found Special characters are not allowed")
        else:
            print("FAIL: Validation message not found.")

    def no_blank_space(self):
        '''Customer ID cannot have blank space'''
        print("Blank Space Validation")
        
        input_box = self.driver.find_element(By.NAME, "cusid")
        input_box.send_keys("123 12") 
        
        page_content = self.driver.page_source
        if "Characters are not allowed" in page_content:
            print("PASS: Found Characters are not allowed")
        else:
            print("FAIL: Validation message not found.")

    def first_char_space(self):
        '''Character cannot be space'''
        print("First Character Space Validation")
        
        input_box = self.driver.find_element(By.NAME, "cusid")
        input_box.send_keys(" ") 
        
        page_content = self.driver.page_source
        if "First character can not have space" in page_content:
            print("PASS: Found First character can not have space")
        else:
            print("FAIL: Validation message not found.")

    def submit_incorrect_id(self):
        '''Submit Incorrect Customer ID'''
        print("Submit Incorrect ID")
        
        self.driver.find_element(By.NAME, "cusid").send_keys("123456") 
        self.driver.find_element(By.NAME, "AccSubmit").click()
        
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        
        time.sleep(1)
        alert2 = self.driver.switch_to.alert
        print(f"PASS: Alert said '{alert2.text}'")
        alert2.accept()

    def test_DC7_correct_customer_id_fail(self):
        '''Correct Customer ID'''
        print("Correct ID Logic")
        
        self.driver.find_element(By.NAME, "cusid").send_keys("67664") 
        self.driver.find_element(By.NAME, "AccSubmit").click()
        
        time.sleep(1)
        self.driver.switch_to.alert.accept() 
        
        time.sleep(1)
        alert2 = self.driver.switch_to.alert
        print(f"PASS: Alert said '{alert2.text}'")
        alert2.accept()

    def test_DC8_reset_button(self):
        '''Verify Reset Button'''
        print("Reset Button")
        
        input_box = self.driver.find_element(By.NAME, "cusid")
        input_box.send_keys("qwer 123456") 
        self.driver.find_element(By.NAME, "res").click()
        
        value = input_box.get_attribute("value")
        if value == "":
            print("PASS: Field is empty")
        else:
            print("FAIL: Field is not empty")

if __name__ == "__main__":
    unittest.main()
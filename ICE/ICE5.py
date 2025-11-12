from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Ice5TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()
        cls.browser.maximize_window()
        sleep(2)

    def test_reg(self):
        self.browser.get("http://demo.guru99.com/test/newtours")
        sleep(5)



    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
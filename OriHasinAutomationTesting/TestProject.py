import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep

class AOSTests(TestCase):
    def setUp(self) :
        self.driver = webdriver.Chrome(executable_path="C:/Users/User/Desktop/Ori Selenium/chromedriver.exe")
        self.driver.get("http://advantageonlineshopping.com/#/")

    def tearDown(self) :
        self.driver.find_element_by_xpath('//div[@class="logo"]')

    def Excrisice1(self):
        pass


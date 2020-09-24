import unittest
from unittest import TestCase
from selenium import webdriver
from OriHasinAutomationTesting.Pages import CartIcon,CartPage,CategoryPage,ProductPage,HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep
from random import *


class AOSTests(TestCase):
    def setUp(self) :
        self.driver = webdriver.Chrome(executable_path="C:\Downloads\chromedriver.exe")
        self.driver.get("http://advantageonlineshopping.com/#/")
        self.driver.maximize_window()
        self.ListOfCategories= ['headphones','mice','tablets','laptops','speakers']

    def tearDown(self) :
        self.driver.find_element_by_xpath('//div[@class="logo"]')
        self.driver.close()

    def test1(self):
        hpage1=HomePage(self.driver)
        cpage1=CategoryPage(self.driver)
        ppage1=ProductPage(self.driver)
        cartIcon1=CartIcon(self.driver)
        sumquantity=0
        for i in range(2):
            randomcategory=randint(0,4)
            randomproduct=randint(0,2)
            randomquantity=randint(1,5)
            sumquantity += randomquantity
            hpage1.WaitToHomepage()
            hpage1.CategoryIcon(self.ListOfCategories[randomcategory])
            cpage1.WaitToCategorypage()
            cpage1.GetProduct(randomproduct)
            ppage1.WaitToProductpage()
            ppage1.PlusQuantity(randomquantity)
            ppage1.AddToCartButton()
            ppage1.BackToCategory()
            cpage1.BackToHomepage()

        hpage1.WaitToHomepage()
        sleep(1)
        self.assertEqual(int(cartIcon1.NumberOfProducts()),sumquantity+2 or int(cartIcon1.NumberOfProducts()),sumquantity+1 )












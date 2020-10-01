import unittest
from unittest import TestCase
from selenium import webdriver
from OriHasinAutomationTesting.Pages import HomePage, CategoryPage, CartPage, CartIcon, ProductPage
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep


class AOSTests(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/admin/Desktop/Drivers/chromedriver.exe")
        self.driver.get("http://advantageonlineshopping.com/#/")
        self.ListOfCategories = ['headphones', 'mice', 'tablets', 'laptops', 'speakers']
        self.hpage = HomePage(self.driver)
        self.cpage = CategoryPage(self.driver)
        self.ppage = ProductPage(self.driver)
        self.cicon = CartIcon(self.driver)
        self.cartpage = CartPage(self.driver)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.find_element_by_xpath('//div[@class="logo"]')
        #self.driver.close()

    def test_Exercise1(self):
        sumquantity = 0
        for i in range(2):
            randomcategory = randint(0, 4)
            randomproduct = randint(0, 2)
            randomquantity = randint(1, 5)
            sumquantity += randomquantity
            self.hpage.WaitToHomepage()
            self.hpage.CategoryIcon(self.ListOfCategories[randomcategory])
            self.cpage.WaitToCategorypage()
            self.cpage.GetProduct(randomproduct)
            self.ppage.WaitToProductpage()
            self.ppage.PlusQuantity(randomquantity)
            self.ppage.AddToCartButton()
            self.ppage.BackToCategory()
            self.cpage.BackToHomepage()

        self.hpage.WaitToHomepage()
        sleep(1)
        self.assertEqual(int(self.cicon.NumberOfProducts()), sumquantity + 2 or int(self.cicon.NumberOfProducts()),
                         sumquantity + 1)

    def test_Exercise2(self):
        ListC = ['headphones', 'speakers', 'tablets', 'mice', 'laptops']
        ListP = []  # List of products
        ListPicon = []  # List of products in cart icon
        ListNum = []  # List of index of products
        num=2
        num2=2
        for i in range(3):
            #num = randint(0, 4)
            self.hpage.WaitToHomepage()
            self.hpage.CategoryIcon(ListC[num])
            self.cpage.WaitToCategorypage()
            #num2 = randint(0, self.cpage.ProductsInCategory()-1)
            while num == 0 and num2 == 1 or (num,num2) in ListNum:  # Out of stock product OR multiply product
                num2 = randint(0, self.cpage.ProductsInCategory()-1)
            ListNum.append((num,num2))
            print("ListNum = ",ListNum)  # debug
            self.cpage.GetProduct(num2)
            self.ppage.WaitToProductpage()
            self.ppage.PlusQuantity(i)
            ListP.append(self.ppage.ProductAttributes())
            ListP[i][2] = 1 + i  # Update of QTY
            ListP[i][3] = int(ListP[i][2]) * float(ListP[i][3])  # Update of Price
            self.ppage.AddToCartButton()
            self.cicon.CartIcon()
            self.cicon.WaitToCartIcon()
            ListPicon.append(self.cicon.ProductAttributesIcon(i))
            self.ppage.BackToCategory()
            self.cpage.WaitToCategorypage()
            self.cpage.BackToHomepage()
            num+=1
            num2+=1
        self.assertTrue(self.ppage.EqualProduct(ListP, ListPicon) == 'True')

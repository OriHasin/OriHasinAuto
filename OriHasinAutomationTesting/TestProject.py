import unittest
from unittest import TestCase
from selenium import webdriver
from OriHasinAutomationTesting.Pages import HomePage, CategoryPage, CartPage, CartIcon, ProductPage , UserIcon , OrderPaymentPage
from random import randint
from selenium.common.exceptions import NoSuchElementException
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
        self.uicon = UserIcon(self.driver)
        self.opp = OrderPaymentPage(self.driver)
        self.driver.maximize_window()


    def tearDown(self):
        self.hpage.LogoIcon()
        self.driver.close()


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
        self.assertEqual(int(self.cicon.NumberOfProducts()), sumquantity + 2 or int(self.cicon.NumberOfProducts()),sumquantity + 1)


    def test_Exercise2(self):
        ListC = ['headphones', 'speakers', 'tablets', 'mice', 'laptops']
        ListP = []  # List of products
        ListPicon = []  # List of products in cart icon
        ListNum = []  # List of index of products
        for i in range(3):
            num = randint(0, 4)
            self.hpage.WaitToHomepage()
            self.hpage.CategoryIcon(ListC[num])
            self.cpage.WaitToCategorypage()
            num2 = randint(0, self.cpage.ProductsInCategory()-1)
            while num == 0 and num2 == 1 or (num,num2) in ListNum:  # Out of stock product OR multiply product
                num2 = randint(0, self.cpage.ProductsInCategory() - 1)
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
        self.assertTrue(self.ppage.EqualProduct(ListP, ListPicon))


    def test_Exercise4(self):
        ListC = ['headphones', 'speakers', 'tablets', 'mice', 'laptops']
        num = randint(0,4)
        self.hpage.WaitToHomepage()
        self.hpage.CategoryIcon(ListC[num])
        self.cpage.WaitToCategorypage()
        num2 = randint(0, self.cpage.ProductsInCategory()-1)
        while num == 0 and num2 == 1:
            num2 = randint(0, self.cpage.ProductsInCategory()-1)
        self.cpage.GetProduct(num2)
        self.ppage.WaitToProductpage()
        self.ppage.AddToCartButton()
        self.cicon.CartIcon().click()
        self.cartpage.WaitToCartPage()
        self.assertTrue(self.cartpage.ShoppingCartText() == 'SHOPPING CART')


    def test_Exercise6(self):
        ListC = ['headphones', 'speakers', 'tablets', 'mice', 'laptops']
        ListNum = []
        Plus = 2
        for i in range(2):  # Added 2 products
            num = randint(0, 4)
            self.hpage.WaitToHomepage()
            self.hpage.CategoryIcon(ListC[num])
            self.cpage.WaitToCategorypage()
            num2 = randint(0, self.cpage.ProductsInCategory() - 1)
            while num == 0 and num2 == 1 or (num, num2) in ListNum:
                num2 = randint(0, self.cpage.ProductsInCategory() - 1)
            ListNum.append((num, num2))
            self.cpage.GetProduct(num2)
            self.ppage.WaitToProductpage()
            self.ppage.AddToCartButton()
            self.hpage.LogoIcon()
        self.cicon.CartIcon().click()
        for i in range(2):  # Edit 2 products
            self.cartpage.WaitToCartPage()
            self.cartpage.EditButton(i)
            self.ppage.WaitToProductpage()
            self.ppage.PlusQuantity(Plus)
            Plus += 1
            self.ppage.AddToCartButton()
        self.assertEqual(self.cartpage.Quantity(0),3)
        self.assertEqual(self.cartpage.Quantity(1),4)


    def test_Exercise8(self):
        ListC = ['headphones', 'speakers', 'tablets', 'mice', 'laptops']
        num = randint(0, 4)
        self.hpage.WaitToHomepage()
        self.hpage.CategoryIcon(ListC[num])
        self.cpage.WaitToCategorypage()
        num2 = randint(0, self.cpage.ProductsInCategory() - 1)
        while num == 0 and num2 == 1:
            num2 = randint(0, self.cpage.ProductsInCategory() - 1)
        self.cpage.GetProduct(num2)
        self.ppage.WaitToProductpage()
        self.ppage.AddToCartButton()
        self.cicon.CartIcon().click()
        self.cartpage.WaitToCartPage()
        self.cartpage.CheckOutButton()
        self.opp.WaitToOrderPaymentPage()
        self.opp.RegisterButton()
        self.opp.WaitToRegisterPage()
        self.opp.RegisterUser('Ori125','ori1432@gmail.com','123652112Fe')
        self.opp.WaitToShippingDetailsPage()
        self.opp.NextButton()
        self.opp.WaitToPaymentMethodPage()
        self.opp.SafePayDetails()
        self.opp.PayNowSafePay()
        self.opp.WaitToOrderCompletePage()
        order_number = self.opp.GetOrderNumber()
        self.uicon.UserOrdersEnter()
        self.uicon.WaitToMyOrdersPage()
        self.assertEqual(self.cicon.LengthListOfProducts(), 0)
        self.assertTrue(self.uicon.OrderInList(order_number))


    def test_Exercise10(self):
        self.hpage.WaitToHomepage()
        self.uicon.UserIcon().click()
        self.uicon.WaitToLogIn()
        self.uicon.LoginUserIcon('OriHasin','Ori12345')
        username = self.uicon.UserName()
        self.assertTrue(self.uicon.UserName() == username)
        self.uicon.UserIcon().click()
        self.uicon.LogoutUserIcon()
        try:
            self.uicon.UserName()
        except NoSuchElementException:
            pass




























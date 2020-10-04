import unittest
from unittest import TestCase
from selenium import webdriver
from OriHasinAutomationTesting.Pages import HomePage,CategoryPage,CartPage,CartIcon,ProductPage,OrderPaymentPage,UserIcon
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep

class AOSTests(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\selenium_driver\chromedriver.exe")
        self.driver.get("http://advantageonlineshopping.com/#/")
        self.ListOfCategories=['headphones','mice','tablets','laptops','speakers']
        self.hpage = HomePage(self.driver)
        self.cpage = CategoryPage(self.driver)
        self.ppage = ProductPage(self.driver)
        self.cicon=CartIcon(self.driver)
        self.cartpage=CartPage(self.driver)
        self.orderpayment=OrderPaymentPage(self.driver)
        self.usericon=UserIcon(self.driver)
        self.driver.maximize_window()

    def tearDown(self) :
        self.driver.find_element_by_xpath('//div[@class="logo"]')
        self.driver.close()

    def test1(self):
        self.hpage1=HomePage(self.driver)
        self.cpage1=CategoryPage(self.driver)
        self.ppage1=ProductPage(self.driver)
        cartIcon1=CartIcon(self.driver)
        sumquantity=0
        for i in range(2):
            randomcategory=randint(0,4)
            randomproduct=randint(0,2)
            randomquantity=randint(1,5)
            sumquantity += randomquantity
            self.hpage1.WaitToHomepage()
            self.hpage1.CategoryIcon(self.ListOfCategories[randomcategory])
            self.cpage1.WaitToCategorypage()
            self.cpage1.GetProduct(randomproduct)
            self.ppage1.WaitToProductpage()
            self.ppage1.PlusQuantity(randomquantity)
            self.ppage1.AddToCartButton()
            self.ppage1.BackToCategory()
            self.cpage1.BackToHomepage()

        self.hpage1.WaitToHomepage()
        self.assertEqual(int(cartIcon1.NumberOfProducts()),sumquantity+2 or int(cartIcon1.NumberOfProducts()),sumquantity+1 )

    def test_Exercise2(self):
      #  pointer=3
        plus=0
        index=0
        ListOfProducts = []

        for i in range(3):
            index2=randint(0,4) # Index of category
            self.Hpage.WaitToHomepage()
            self.Hpage.CategoryIcon(self.ListOfCategories[index2])
            self.Cpage.WaitToCategorypage()
            index3=randint(0,self.Cpage.NumberOfProducts()-1) # Index of product
            while index==1 and index3==1: # Specific product that Out Of Stock
                index3=randint(0,self.Cpage.NumberOfProducts()-1)
            self.Cpage.GetProduct(index3)
            self.Ppage.WaitToProductpage()
            self.Ppage.PlusQuantity(plus)
            plus+=plus
            ListOfProducts.append(self.Ppage.ProductAttributes())
            ListOfProducts[i][2] = (plus+1) # Update quantity of product
            ListOfProducts[i][3] = (plus+1) * ListOfProducts[i][3] # Update the price by quantity
            self.Ppage.AddToCartButton()
            self.Ppage.BackToCategory()
            self.Cpage.BackToHomepage()
        for i in range(3):
            print(ListOfProducts[i][0],"hey")
            print(self.Cicon.NameInCartIcon(2-i),"bye")
            self.Cicon.CartIcon()
            self.assertEqual(ListOfProducts[i][0], self.Cicon.NameInCartIcon(2-i))
            self.assertEqual(ListOfProducts[i][1], self.Cicon.ColorInCartIcon(2-i))
            self.assertEqual(ListOfProducts[i][2], self.Cicon.QtyInCartIcon(2-i))
            self.assertEqual(ListOfProducts[i][3], self.Cicon.PriceInCartIcon(2-i))
            #pointer-=1


    def test_Exercise3(self):
        counter1=0
        for i in range(2):
            counter1+=1
            randomcategory=randint(0,4)
            randomproduct=randint(0,2)
            randomquantity=randint(1,5)
            self.hpage.WaitToHomepage()
            self.hpage.CategoryIcon(self.ListOfCategories[randomcategory])
            self.cpage.WaitToCategorypage()
            self.cpage.GetProduct(randomproduct)
            self.ppage.WaitToProductpage()
            self.ppage.PlusQuantity(randomquantity)
            self.ppage.AddToCartButton()
            self.ppage.BackToCategory()
            self.cpage.BackToHomepage()
        if self.cicon.LengthListOfProducts()==counter1:
            self.cicon.RemoveInCartIcon(1)
        print(self.cicon.LengthListOfProducts(),counter1)
        self.assertTrue(counter1==self.cicon.LengthListOfProducts()+1)

    def test_Exercise5(self):
        listqty=[]
        listcat=[]
        randomquantity = randint(1,5)
        randomcategory = randint(0,4)
        for i in range(3):
            bool1=True
            while bool1:
                if randomquantity in listqty:
                    randomquantity = randint(1,5)
                else:
                    listqty.append(randomquantity)
                    bool1=False
            bool2=True
            while bool2:
                if randomcategory in listcat:
                    randomcategory = randint(0,4)
                else:
                    listcat.append(randomcategory)
                    bool2=False
            randomproduct = randint(0, 2)
            self.hpage.WaitToHomepage()
            self.hpage.CategoryIcon(self.ListOfCategories[randomcategory])
            self.cpage.WaitToCategorypage()
            self.cpage.GetProduct(randomproduct)
            self.ppage.WaitToProductpage()
            self.ppage.PlusQuantity(randomquantity)
            self.ppage.AddToCartButton()
            self.ppage.BackToCategory()
            self.cpage.BackToHomepage()
            randomquantity = randint(1,5)
            randomcategory = randint(0,4)
        self.cicon.CartIcon().click()
        self.cartpage.WaitToCartpage()
        sumprices=0
        for i in range(0,3,1):
            tmpprice=self.cartpage.ProductPriceInCart(i)
            tmpprice=tmpprice.replace(",","")
            tmpprice=tmpprice[1:]
            sumprices+=float(tmpprice)
            print(sumprices)
            print("The Product Name Is:" + self.cartpage.ProductNameInCart(i) + "The QTY Is:" + self.cartpage.ProductQtyInCart(i) + "The Price Is:" + self.cartpage.ProductPriceInCart(i))
        totalprice=self.cartpage.TotalPrice()
        totalprice=totalprice.replace(",","")
        totalprice=totalprice[1:]
        self.assertEqual(float(totalprice),round(sumprices,2))

    def test_Exercise7(self):
        self.hpage.WaitToHomepage() #wait to homepage
        self.hpage.CategoryIcon("tablets") #enter category tablets
        self.cpage.WaitToCategorypage() #wait to category page
        self.cpage.GetProduct(randint(0,2)) #choose random product
        self.ppage.WaitToProductpage() #wait to product page
        self.ppage.PlusQuantity(randint(1,9)) #add random quantity
        self.ppage.AddToCartButton() #add to cart
        self.ppage.BackToCategory() #back to tablets page
        self.cpage.WaitToCategorypage() #wait
        self.assertEqual(len(self.cpage.TabletsCategoryValidation()),4) #make sure it is the tablets page
        self.cpage.BackToHomepage() #back to homepage
        self.hpage.WaitToHomepage() #wait
        self.assertEqual(len(self.hpage.HomePageValidation()),5) #make sure it is the home page

    def test_Exercise9(self):
        self.hpage.WaitToHomepage()  # wait to homepage
        self.hpage.CategoryIcon("tablets")  # enter category tablets
        self.cpage.WaitToCategorypage()  # wait to category page
        self.cpage.GetProduct(randint(0, 2))  # choose random product
        self.ppage.WaitToProductpage()  # wait to product page
        self.ppage.PlusQuantity(randint(1, 9))  # add random quantity
        self.ppage.AddToCartButton()  # add to cart
        self.cicon.CartIcon().click()
        self.cartpage.WaitToCartpage()
        self.cartpage.CheckoutButtonCartpage()
        self.orderpayment.WaitToOrderPaymentPage()
        self.orderpayment.InsertUserExist("zivush","Zzziiivvv4")
        self.orderpayment.LogInButton()
        self.orderpayment.WaitToShippingDetailsPage()
        sleep(3)
        self.orderpayment.NextButton()
        self.orderpayment.WaitToPaymentMethodPage()
        self.orderpayment.PayNowButton()
        self.orderpayment.WaitToOrderCompletePage()
        ordernumber = self.orderpayment.OrderNumberGet()
        print("hey",ordernumber)
        sleep(3)
        self.assertEqual(self.cicon.LengthListOfProducts(),0)
        self.usericon.UserOrdersEnter()
        self.usericon.WaitToMyOrdersPage()
        self.assertTrue(self.usericon.OrderInList(ordernumber))




























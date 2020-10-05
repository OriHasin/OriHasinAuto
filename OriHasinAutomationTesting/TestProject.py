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
        self.hpage.LogoIcon()
        self.driver.close()

    def test1(self):
        sumquantity=2 #sum the quantity of each product is ordered|begins on 2 because the default quantity is 1
        listqty = [] #list of quantities
        listcat = [] #list of categories
        randomquantity = randint(1,5) #rand quantity
        randomcategory = randint(0,4) #rand category
        for i in range(2): #order of 2 products
            randomquantity = self.ppage.RandomQuantityCheck(listqty, randomquantity) #check that quantity not used before
            listqty.append(randomquantity) #add the current quantity to the QTY list
            randomcategory = self.cpage.RandomCategoryCheck(listcat, randomcategory) #check that category not used before
            listcat.append(randomcategory) #add the current category to the CAT list
            sumquantity += randomquantity #sum
            self.hpage.WaitToHomepage() #wait
            self.hpage.CategoryIcon(self.ListOfCategories[randomcategory]) #press on current category
            self.cpage.WaitToCategorypage() #wait
            randomproduct = randint(0, self.cpage.ProductsInCategory() - 1) #choose random product from list of products in the current category
            randomproduct=self.ppage.RandomProductCheck(randomcategory,randomproduct,self.cpage.ProductsInCategory()) #check that product not out of stock
            self.cpage.GetProduct(randomproduct) #press on current product
            self.ppage.WaitToProductpage() #wait
            self.ppage.PlusQuantity(randomquantity) #choose current quantity
            self.ppage.AddToCartButton() #press on add to cart button
            self.ppage.BackToCategory() #back to current category
            self.cpage.BackToHomepage() #back to homepage

        self.hpage.WaitToHomepage() #wait
        self.assertEqual(int(self.cicon.NumberOfProducts()),sumquantity) #check that quantity of products that ordered is equal to actually number of products in cart icon.



    def test_Exercise3(self):
        listqty = [] #list of quantities
        listcat = [] #list of categories
        randomquantity = randint(1, 5) #rand quantity
        randomcategory = randint(0, 4) #rand category
        counter1=0 #count the items are ordered
        for i in range(2): #order of 2 products
            counter1+=1 #count
            randomquantity = self.ppage.RandomQuantityCheck(listqty, randomquantity) #check that quantity not used before
            listqty.append(randomquantity) #add the current quantity to the QTY list
            randomcategory = self.cpage.RandomCategoryCheck(listcat, randomcategory) #check that category not used before
            listcat.append(randomcategory) #add the current category to the CAT list
            self.hpage.WaitToHomepage() #wait
            self.hpage.CategoryIcon(self.ListOfCategories[randomcategory]) #press on current category
            self.cpage.WaitToCategorypage() #wait
            randomproduct = randint(0, self.cpage.ProductsInCategory() - 1) #choose random product from list of products in the current category
            randomproduct = self.ppage.RandomProductCheck(randomcategory, randomproduct,self.cpage.ProductsInCategory())  # check that product not out of stock
            self.cpage.GetProduct(randomproduct) #press on current product
            self.ppage.WaitToProductpage() #wait
            self.ppage.PlusQuantity(randomquantity) #choose current quantity
            self.ppage.AddToCartButton() #press on add to cart button
            self.ppage.BackToCategory() #back to current category
            self.cpage.BackToHomepage() #back to homepage
        if self.cicon.LengthListOfProducts()==counter1: #check that count equal to length list of products in cart icon
            self.cicon.RemoveInCartIcon(1) #remove one product from order
        print("The quantity of products after remove one is:", self.cicon.LengthListOfProducts(), "The quantity of products that ordered: ", counter1) #debug
        self.assertTrue(counter1==self.cicon.LengthListOfProducts()+1) #check that the product actually removed from order

    def test_Exercise5(self):
        listqty=[] #list of quantities
        listcat=[] #list of categories
        randomquantity = randint(1,5) #rand quantity
        randomcategory = randint(0,4) #rand category
        for i in range(3): #add to cart three different products in different quantities
            randomquantity=self.ppage.RandomQuantityCheck(listqty,randomquantity) #check that quantity not used before
            listqty.append(randomquantity) #add the current quantity to the QTY list
            randomcategory=self.cpage.RandomCategoryCheck(listcat,randomcategory) #check that category not used before
            listcat.append(randomcategory) #add the current category to the CAT list
            self.hpage.WaitToHomepage() #wait
            self.hpage.CategoryIcon(self.ListOfCategories[randomcategory]) #press on current category
            self.cpage.WaitToCategorypage() #wait
            randomproduct = randint(0, self.cpage.ProductsInCategory() - 1) #choose random product from list of products in the current category
            randomproduct = self.ppage.RandomProductCheck(randomcategory, randomproduct,self.cpage.ProductsInCategory())  # check that product not out of stock
            self.cpage.GetProduct(randomproduct) #press on current product
            self.ppage.WaitToProductpage() #wait
            self.ppage.PlusQuantity(randomquantity) #choose current quantity
            self.ppage.AddToCartButton() #press on add to cart button
            self.ppage.BackToCategory() #back to current category
            self.cpage.BackToHomepage() #back to homepage
            randomquantity = randint(1,5) #rand quantity
            randomcategory = randint(0,4) #rand category
        self.cicon.CartIcon().click() #enter to cart page
        self.cartpage.WaitToCartpage() #wait
        sumprices=0 #sum of prices of products that were ordered
        for i in range(0,3,1): #
            tmpprice=self.cartpage.ProductPriceInCart(i) #catch the product price from cart page into a varriable
            tmpprice=tmpprice.replace(",","") #remove the ',' from the varriable
            tmpprice=tmpprice[1:] #slice the number without the '$'
            sumprices+=float(tmpprice) #add the number to sumprices
            print("The Product Name Is: " + self.cartpage.ProductNameInCart(i) + " ,The QTY Is: " + self.cartpage.ProductQtyInCart(i) + " And The Price Is: " + self.cartpage.ProductPriceInCart(i)) #present the product
        totalprice=self.cartpage.TotalPrice() #catch the total price of the order into a varriable
        totalprice=totalprice.replace(",","") #remove the ',' from the varriable
        totalprice=totalprice[1:] #slice the number without the '$'
        self.assertEqual(float(totalprice),round(sumprices,2)) #check that total price of the order is equal to the sum of the prices of products in order

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
        self.hpage.CategoryIcon('tablets')
        self.cpage.WaitToCategorypage()  # wait to category page
        randomproduct = randint(0, self.cpage.ProductsInCategory() - 1)
        self.cpage.GetProduct(randomproduct)  # choose random product
        self.ppage.WaitToProductpage()  # wait to product page
        self.ppage.PlusQuantity(randint(1, 9))  # add random quantity
        self.ppage.AddToCartButton()  # add to cart
        self.cicon.CartIcon().click() #enter to cart page
        self.cartpage.WaitToCartpage() #wait
        self.cartpage.CheckoutButtonCartpage() #press on check out button
        self.orderpayment.WaitToOrderPaymentPage() #wait
        self.orderpayment.InsertUserExist("zivush","Zzziiivvv4") #log in with user exist
        self.orderpayment.LogInButton() #press on log in button
        self.orderpayment.WaitToShippingDetailsPage() #wait
        self.orderpayment.NextButton() #press on next button
        self.orderpayment.WaitToPaymentMethodPage() #wait
        self.orderpayment.PayNowButtonMasterCard() #press on pay now with master card
        self.orderpayment.WaitToOrderCompletePage() #wait
        ordernumber = self.orderpayment.OrderNumberGet() #catch order number into varriable
        print("hey",ordernumber) #debug(check that catched)
        self.orderpayment.WaitToOrderCompletePage() #wait to icon cart will be empty
        self.assertEqual(self.cicon.LengthListOfProducts(),0) #check that there is no products in cart icon
        self.usericon.UserOrdersEnter() #enter to 'My Orders' page
        self.usericon.WaitToMyOrdersPage() #wait
        self.assertTrue(self.usericon.OrderInList(ordernumber)) #check that the current order number in the list of my orders


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















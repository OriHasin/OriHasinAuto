from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep
from random import *


class HomePage:
    def __init__(self,driver):
        self.driver=driver
    def CategoryIcon(self,category):
        self.driver.find_element_by_id(f"{category.lower()}Img").click()

    def HomePageValidation(self):
        return self.driver.find_elements_by_xpath("//div[@href='javascript:void(0)']")

    def WaitToHomepage(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "headphonesImg")))


###############################################################################################

class CartPage:
    def __init__(self,driver):
        self.driver=driver

    def ProductPriceInCart(self,index):
        #index+=3
        return self.driver.find_elements_by_xpath('//p [@class="price roboto-regular ng-binding"]')[index].text

    def ProductNameInCart(self,index):
        return self.driver.find_elements_by_xpath('//label [@class="roboto-regular productName ng-binding"]')[index].text

    def ProductQtyInCart(self,index):
        return self.driver.find_elements_by_xpath('//tbody/tr/td/label [@class="ng-binding"]')[index].text

    def EditButton(self,index): # לחיצה כל כפתור עריכה של מוצר ספציפי בעגלת הקניות
         self.driver.find_elements_by_css_selector("a[class='edit ng-scope']")[index].click()

    def ShoppingCartText(self): # מחזיר את הטקסט "Shopping Cart" בעגלת הקניות
        return self.driver.find_element_by_class_name("select  ng-binding").text


    def TotalPrice(self):
        return self.driver.find_element_by_xpath('// *[ @ id = "shoppingCart"] / table / tfoot / tr[1] / td[2] / span[2]').text

    def CheckoutButtonCartpage(self):
        self.driver.find_element_by_xpath("//button[@class='roboto-medium tami uft-class ng-binding']").click()


    def WaitToCartpage(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h3[@class="roboto-regular center sticky fixedImportant ng-binding"]')))


###############################################################################################

class CartIcon:
    def __init__(self,driver):
        self.driver=driver

    def CartIcon(self):
        return self.driver.find_element_by_id("shoppingCartLink")

    def NumberOfProducts(self):
        return self.driver.find_element_by_xpath('//header//a/span[@ng-show="(cart | productsCartCount) > 0"]').text

    def QtyInCartIcon(self,index):
        return self.driver.find_elements_by_xpath("//lable[contains(text(),'QTY')]")[index].text

    def PriceInCartIcon(self,index):
        return self.driver.find_elements_by_class_name("price roboto-regular ng-binding")[index].text
    def ColorInCartIcon(self,index):
        return self.driver.find_elements_by_css_selector("span[class='ng-binding']")[index].text
    def NameInCartIcon(self,index):
        return self.driver.find_elements_by_css_selector("h3[class='ng-binding']")[index].text
    def RemoveInCartIcon(self,index):
        return self.driver.find_elements_by_css_selector("[class='removeProduct iconCss iconX']")[index].click()
    def LengthListOfProducts(self):
        return len(self.driver.find_elements_by_xpath('//img [@class="imageUrl"]'))



###############################################################################################


class CategoryPage:

    def __init__(self,driver):
        self.driver=driver

    def GetProduct(self,index):
         self.driver.find_elements_by_css_selector("img[class='imgProduct']")[index].click()

    def BackToHomepage(self):
         self.driver.find_element_by_xpath('// a[ @ translate = "HOME"]').click()

    def ProductsInCategory(self):
        return len(self.driver.find_elements_by_css_selector("img[class='imgProduct']"))

    def TabletsCategoryValidation(self):
        return self.driver.find_elements_by_xpath("//h4[@href='javascript:void(0)']")

    def WaitToCategorypage(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "imgProduct")))


###############################################################################################

class ProductPage:

    def __init__(self,driver):
        self.driver=driver

    def SwitchColor(self,color): # Choosing a color for product
        return self.driver.find_element_by_xpath(f"//span[@title='{color.upper()}']")

    def PlusQuantity(self,quantity): # Clicking on '+' button
        for i in range(quantity):
            self.driver.find_element_by_xpath("//div[@class='plus']").click()

    def AddToCartButton(self):
        self.driver.find_element_by_xpath('//button[@name="save_to_cart"]').click()

    def BackToCategory(self):
         self.driver.find_element_by_xpath('//a[@class="ng-binding"]').click()

    def ProductAttributes(self): # Create a list with attributes of specific product
        list1=[]
        list1.append(self.driver.find_element_by_css_selector("h1[class='roboto-regular screen768 ng-binding']").text) # Name
        list1.append(self.driver.find_element_by_xpath("//span[@title]").get_attribute("title")) # Color
        list1.append("") # Quantity
        list1.append(self.driver.find_element_by_css_selector("article>div>div>h2[class='roboto-thin screen768 ng-binding']").text) # Price
        return list1

    def WaitToProductpage(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "save_to_cart")))

class OrderPaymentPage:

    def __init__(self,driver):
        self.driver=driver

    def InsertUserExist(self,username,password):
        self.driver.find_element_by_xpath('//input[@name="usernameInOrderPayment"]').send_keys(username)
        self.driver.find_element_by_xpath('//input[@name="passwordInOrderPayment"]').send_keys(password)

    def LogInButton(self):
        self.driver.find_element_by_xpath('//button[@id="login_btnundefined"]').click()

    def NextButton(self):
        self.driver.find_element_by_xpath('//button[@class="a-button nextBtn marginTop75 ng-scope"]').click()

    def EditButton(self):
        self.driver.find_element_by_xpath('//label[@class="edit  ng-scope"]').click()

    def PayNowButtonMasterCard(self):
        self.driver.find_element_by_xpath('//button[@style="    margin-bottom: 5px;"]').click()

    def OrderNumberGet(self):
       return self.driver.find_element_by_xpath('//label[@id="orderNumberLabel"]').text

    def WaitToOrderPaymentPage(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h5[@translate='ORDER_SUMMARY']")))

    def WaitToShippingDetailsPage(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//label[@class="roboto-regular ng-binding selected"]')))

    def WaitToPaymentMethodPage(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="paymentMethods"]')))

    def WaitToOrderCompletePage(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="seccion borderRight"]')))

class UserIcon:
    def __init__(self,driver):
        self.driver=driver

    def UserOrdersEnter(self):
        self.driver.find_element_by_xpath('//a[@id="menuUserLink"]').click()
        self.driver.find_element_by_xpath('//a/div/label[@translate="My_Orders"]').click()

    def OrderInList(self,ordernumber):
        list1=self.driver.find_elements_by_css_selector("label[class='ng-binding']")
        reversed(list1)
        for i in range(len(list1)):
            if list1[i].text == ordernumber:
                return True
        return False

    def WaitToMyOrdersPage(self):
        WebDriverWait(self.driver, 16).until(EC.presence_of_element_located((By.XPATH, '//label[@class="center ng-binding"]')))















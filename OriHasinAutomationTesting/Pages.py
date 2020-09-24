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
    def WaitToHomepage(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "headphonesImg")))


###############################################################################################

class CartPage:
    def __init__(self,driver):
        self.driver=driver

    def EditButton(self,index): # לחיצה כל כפתור עריכה של מוצר ספציפי בעגלת הקניות
         self.driver.find_elements_by_css_selector("a[class='edit ng-scope']")[index].click()

    def ShoppingCartText(self): # מחזיר את הטקסט "Shopping Cart" בעגלת הקניות
        return self.driver.find_element_by_class_name("select  ng-binding").text

    def TotalPrice(self):
        return self.driver.find_element_by_xpath("//span[@class='roboto-medium ng-binding'][3]").text


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















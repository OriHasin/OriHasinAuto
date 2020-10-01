from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep
from random import *


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def CategoryIcon(self, category):
        self.driver.find_element_by_id(f"{category.lower()}Img").click()

    def WaitToHomepage(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "headphonesImg")))


# --------------------------------------------------------------------------------------------------------------

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def EditButton(self, index):  # לחיצה כל כפתור עריכה של מוצר ספציפי בעגלת הקניות
        self.driver.find_elements_by_css_selector("a[class='edit ng-scope']")[index].click()

    def ShoppingCartText(self):  # מחזיר את הטקסט "Shopping Cart" בעגלת הקניות
        return self.driver.find_element_by_class_name("select  ng-binding").text

    def TotalPrice(self):
        return self.driver.find_element_by_xpath("//span[@class='roboto-medium ng-binding'][3]").text


# --------------------------------------------------------------------------------------------------------------

class CartIcon:
    def __init__(self, driver):
        self.driver = driver

    def CartIcon(self):
        return self.driver.find_element_by_id("shoppingCartLink")

    def NumberOfProducts(self):
        return self.driver.find_element_by_xpath('//header//a/span[@ng-show="(cart | productsCartCount) > 0"]').text

    def WaitToCartIcon(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"img[class='imageUrl']")))

    def QtyInCartIcon(self, index):
         list1 = self.driver.find_elements_by_xpath("//label[contains(text(),'QTY')]")
         list1 = self.ReplaceList(list1)
         Qty = list1[index].text[5:]
         print(Qty)
         return Qty

    def PriceInCartIcon(self, index):
        list1 = self.driver.find_elements_by_class_name("price")
        list1 = self.ReplaceList(list1)
        Price = list1[index].text[1:]
        Price = Price.replace(',','')
        print(Price)
        return Price

    def ColorInCartIcon(self, index):
        list1 = self.driver.find_elements_by_css_selector("span[class='ng-binding']")
        list1 = self.ReplaceList(list1)
        Color = list1[index].text
        print(Color)
        return Color

    def NameInCartIcon(self, index):
        list1 = self.driver.find_elements_by_css_selector("h3[class='ng-binding']")
        list1 = self.ReplaceList(list1)
        Name = list1[index].text[:-3]
        print(Name)
        return Name

    def RemoveInCartIcon(self, index):
        return self.driver.find_elements_by_css_selector("[class='removeProduct iconCss iconX']")[index].click()

    def ProductAttributesIcon(self,index):  # Create a list with attributes of product ( product that appeared in cart icon )
        list1 = []
        list1.append(self.NameInCartIcon(index))
        list1.append(self.ColorInCartIcon(index))
        list1.append(self.QtyInCartIcon(index))
        list1.append(self.PriceInCartIcon(index))
        return list1

    def ReplaceList(self,list1):
        list2=[]
        for i in range(len(list1)-1,-1,-1):
            list2.append(list1[i])
        return list2


# --------------------------------------------------------------------------------------------------------------


class CategoryPage:

    def __init__(self, driver):
        self.driver = driver

    def GetProduct(self, index):
        self.driver.find_elements_by_css_selector("img[class='imgProduct']")[index].click()

    def BackToHomepage(self):
        self.driver.find_element_by_xpath('// a[ @ translate = "HOME"]').click()

    def ProductsInCategory(self): # Return the number of products each category
        return len(self.driver.find_elements_by_css_selector("img[class='imgProduct']"))

    def WaitToCategorypage(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "imgProduct")))


# --------------------------------------------------------------------------------------------------------------


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def SwitchColor(self, color):  # Choosing a color for product
        return self.driver.find_element_by_xpath(f"//span[@title='{color.upper()}']")

    def PlusQuantity(self, quantity):  # Clicking on '+' button
        for i in range(quantity):
            self.driver.find_element_by_xpath("//div[@class='plus']").click()

    def AddToCartButton(self):
        self.driver.find_element_by_xpath('//button[@name="save_to_cart"]').click()

    def BackToCategory(self):
        self.driver.find_element_by_xpath('//a[@class="ng-binding"]').click()

    def ProductAttributes(self):  # Create a list with attributes of specific product
        list1 = []
        list1.append(self.driver.find_element_by_css_selector("h1[class='roboto-regular screen768 ng-binding']").text)  # Name
        list1.append(self.driver.find_element_by_xpath("//span[@id='bunny']").get_attribute("title"))  # Color
        list1.append("")  # Quantity
        price = self.driver.find_element_by_css_selector("article>div>div>h2[class='roboto-thin screen768 ng-binding']").text[1:]
        price = price.replace(',','')
        list1.append(price)  # Price
        return list1


    def WaitToProductpage(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "save_to_cart")))


    def EqualProduct(self, list1, list2):  # Check if product that added to cart , appearing good in cart icon
        for i in range(3):# debug
            for x in range(4):
                print("list2")    # debug
                print(list2[i][x])     # debug
                print("list1")    # debug
                print(list1[i][x])     # debug


        for i in range(len(list1)):
            if str(list2[i][0]) not in str(list1[i][0]):   # First , check the name (Substring)
                return False
            for x in range(1,4):
                #print("First " + list1[i][x])
                #print("Second " + list2[i][x])
                if list2[i][x] == list1[i][x]:
                    continue
                else:
                    return False
        return True

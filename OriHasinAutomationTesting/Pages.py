from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep


class HomePage:
    def __init__(self,driver):
        self.driver=driver
    def CategoryIcon(self,category):
       return self.driver.find_element_by_id(f"{category.lower()}Img")


###############################################################################################

class CartPage:
    def __init__(self,driver):
        self.driver=driver
    def EditButton(self,index): # לחיצה כל כפתור עריכה של מוצר ספציפי בעגלת הקניות
         self.driver.find_elements_by_css_selector("a[class='edit ng-scope']")[index].click()
    def ShoppingCartText(self): # מחזיר את הטקסט "Shopping Cart" בעגלת הקניות
        return self.driver.find_element_by_class_name("select  ng-binding").text
    def TotalPrice(self): # מחזיר את המחיר הכולל בעגלת הקניות

    def TotalPrice(self):
        return self.driver.find_element_by_xpath("//span[@class='roboto-medium ng-binding'][3]").text


###############################################################################################

class CartIcon:
    def __init__(self,driver):
        self.driver=driver
    def CartIcon(self): # מצביע על אייקון העגלה
        return self.driver.find_element_by_id("shoppingCartLink")
    def NumberOfProducts(self): # מחזיר טקסט של כמות המוצרים באייקון עגלה
        return self.driver.find_element_by_xpath["//span[@class='cart ng-binding'][2]"].text
    def QtyInCartIcon(self,index): # מחזיר טקסט של כמות מוצר ספיציפי באייקון עגלה
        return self.driver.find_elements_by_xpath("//lable[contains(text(),'QTY')]")[index].text
    def PriceInCartIcon(self,index): # מחזיר טקסט של מחיר מוצר ספציפי באייקון עגלה
        return self.driver.find_elements_by_class_name("price roboto-regular ng-binding")[index].text
    def ColorInCartIcon(self,index): # מחזיר טקסט של צבע מוצר ספציפי באייקון עגלה
        return self.driver.find_elements_by_css_selector("span[class='ng-binding']")[index].text
    def NameInCartIcon(self,index): # מחזיר טקסט של שם מוצר ספציפי באייקון עגלה
        return self.driver.find_elements_by_css_selector("h3[class='ng-binding']")[index].text
    def RemoveInCartIcon(self,index): #מוחק מוצר ספציפי מאייקון עגלה
        return self.driver.find_elements_by_css_selector("[class='removeProduct iconCss iconX']")[index].click()


###############################################################################################


class CategoryPage:
    def __init__(self,driver):
        self.driver=driver
    def GetProduct(self,index): # כניסה לדף מוצר ספציפי
         self.driver.find_elements_by_css_selector("img[class='imgProduct']")[index].click()
    def BackToHomepage(self): # לחיצה על דף HomePage בדף קטגוריה
         self.driver.find_element_by_xpath('// a[ @ translate = "HOME"]').click()


###############################################################################################

class ProductPage:
    def __init__(self,driver):
        self.driver=driver
    def SwitchColor(self,color): # בחירת צבע בדף מוצר
        return self.driver.find_element_by_xpath(f"//span[@title='{color.upper()}']")

    def PlusQuantity(self,quantity): # הוספת כמות בדף מוצר
        for i in range(quantity):
            self.driver.find_element_by_xpath("//div[@class='plus']").click()

    def AddToCartButton(self):
        self.driver.find_element_by_xpath('//button[@name="save_to_cart"]').click()

    def BackToCategory(self):
        return self.driver.find_element_by_xpath('//a[@class="ng-binding"]')
    def BackToCategory(self): # לחיצה על דף Category בדף מוצר
         self.driver.find_element_by_xpath('//a[@class="ng-binding"]').click()


###############################################################################################


def main():
    driver = webdriver.Chrome(executable_path="C:/Users/User/Desktop/Ori Selenium/chromedriver.exe")
    driver.get("http://advantageonlineshopping.com/#/")


# CP=CategoryPage(driver)
# sleep(10)
# list1=CP.GetProducts()
# list1[1].click()
# sleep(3)
# pp1=ProductPage(driver)
# pp1.SwitchColor("gray")

#hp1=HomePage(driver)
#sleep(8)
#hp1.CategoryIcon("Headphones").click()
#cp=CategoryPage(driver)
#sleep(3)
#list1=cp.GetProducts()
#print(len(list1))
#list1[1].click()
#sleep(3)
#pp1=ProductPage(driver)
#pp1.BackToCategory().click()
#sleep(3)
#try:
#    list1[0].click()
#except StaleElementReferenceException as Exception:
#    print("Product not sync with the page document anymore")
#    list1=cp.GetProducts()
#    list1[0].click()
#pp1.PlusQuantity(3)
# pp1=ProductPage(driver)
# pp1.SwitchColor("gray").click()
# pp1.BackToCategory().click()
# cp.BackToHomepage().click()












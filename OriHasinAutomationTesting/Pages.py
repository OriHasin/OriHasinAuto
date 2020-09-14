from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep
class HomePage:
    def __init__(self,driver):
        self.driver=driver
    def CategoryIcon(self,category):
       return self.driver.find_element_by_id(f"{category.lower()}Img")

class CartPage:
    def __init__(self,driver):
        self.driver=driver
    def CartIcon(self):
        return self.driver.find_element_by_id("shoppingCartLink")
    def NumberOfProducts(self):
        return self.driver.find_element_by_xpath["//span[@class='cart ng-binding'][2]"].text
    def EditButton(self):
        return self.driver.find_element_by_css_selector("a[class='edit ng-scope']")
class CategoryPage:
    def __init__(self,driver):
        self.driver=driver
    def GetProducts(self):
        return self.driver.find_elements_by_css_selector("img[class='imgProduct']")

class ProductPage:
    def __init__(self,driver):
        self.driver=driver
    def SwitchColor(self,color):
        self.driver.find_element_by_xpath(f"//span[@title='{color.upper()}']").click()


driver=webdriver.Chrome(executable_path="C:/selenium_driver/chromedriver.exe")
driver.get("http://advantageonlineshopping.com/#/")
# CP=CategoryPage(driver)
# sleep(10)
# list1=CP.GetProducts()
# list1[1].click()
# sleep(3)
# pp1=ProductPage(driver)
# pp1.SwitchColor("gray")
hp1=HomePage(driver)
sleep(5)
hp1.CategoryIcon("Headphones").click()












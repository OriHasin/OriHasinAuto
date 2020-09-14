from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep
class HomePage:
    def __init__(self,driver):
        self.driver=driver
    def HeadPhonesIcon (self):
        return self.driver.find_element_by_id("headphonesImg")
    def TabletsIcon(self):
        return self.driver.find_element_by_id("tabletsImg")
    def LaptopsIcon(self):
        return self.driver.find_element_by_id("laptopsImg")
    def SpeakersIcon(self):
        return self.driver.find_element_by_id("speakersImg")
    def MiceIcon(self):
        return self.driver.find_element_by_id("miceImg")
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

# driver=webdriver.Chrome(executable_path="C:/Users/User/Desktop/Ori Selenium/chromedriver.exe")
# driver.get("https://www.advantageonlineshopping.com/#/category/Tablets/3")
# CP=CategoryPage(driver)
# sleep(10)
# list1=CP.GetProducts()
# list1[1].click()











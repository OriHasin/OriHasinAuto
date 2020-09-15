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
    def BackToHomepage(self):
        return self.driver.find_element_by_xpath('// a[ @ translate = "HOME"]')

class ProductPage:
    def __init__(self,driver):
        self.driver=driver
    def SwitchColor(self,color):
        return self.driver.find_element_by_xpath(f"//span[@title='{color.upper()}']")
    def PlusQuantity(self,quantity):
        for i in range(quantity):
            self.driver.find_element_by_xpath("//div[@class='plus']").click()

    def BackToCategory(self):
        return self.driver.find_element_by_xpath('//a[@class="ng-binding"]')


driver=webdriver.Chrome(executable_path="C:/selenium_driver/chromedriver.exe")
driver.get("http://advantageonlineshopping.com/#/")
hp1=HomePage(driver)
sleep(8)
hp1.CategoryIcon("Headphones").click()
cp=CategoryPage(driver)
sleep(3)
list1=cp.GetProducts()
print(len(list1))
list1[1].click()
sleep(3)
pp1=ProductPage(driver)
pp1.BackToCategory().click()
sleep(3)
try:
    list1[0].click()
except StaleElementReferenceException as Exception:
    print("Product not sync with the page document anymore")
    list1=cp.GetProducts()
    list1[0].click()
pp1.PlusQuantity(3)
# pp1=ProductPage(driver)
# pp1.SwitchColor("gray").click()
# pp1.BackToCategory().click()
# cp.BackToHomepage().click()












from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def CategoryIcon(self, category):
        return self.driver.find_element_by_id(f"{category.lower()}Img")


###############################################################################################

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def EditButton(self):  # מחזיר רשימת מיקומי האלמנטים של כפתור עריכה בכל מוצר
        return self.driver.find_elements_by_css_selector("a[class='edit ng-scope']")

    def shopping_cart_text(self):
        return self.driver.find_element_by_class_name("select  ng-binding").text

    def TotalPrice(self):
        return self.driver.find_element_by_xpath("//span[@class='roboto-medium ng-binding'][3]").text


###############################################################################################

class CartIcon:
    def __init__(self, driver):
        self.driver = driver

    def CartIcon(self):
        return self.driver.find_element_by_id("shoppingCartLink")

    def NumberOfProducts(self):
        return self.driver.find_element_by_xpath["//span[@class='cart ng-binding'][2]"].text

    def QtyInCartIcon(self):  # מחזיר רשימת מיקומי האלמנטים של כמות מוצרים באייקון העגלה
        return self.driver.find_elements_by_xpath("//lable[contains(text(),'QTY')]")

    def PriceInCartIcon(self):  # מחזיר רשימת מיקומי האלמנטים של מחיר מוצרים באייקון העגלה
        return self.driver.find_elements_by_class_name("price roboto-regular ng-binding")

    def ColorInCartIcon(self):  # מחזיר רשימת מיקומי האלמנטים של צבע מוצרים באייקון עגלה
        return self.driver.find_elements_by_css_selector("span[class='ng-binding']")

    def NameInCartIcon(self):  # מחזיר רשימה של מיקומי האלמנטים של שמות המוצרים באייקון עגלה
        return self.driver.find_elements_by_css_selector("h3[class='ng-binding']")

    def RemoveInCartIcon(self):  # מחזיר רשימה של מיקומי האלמנטים של מחיקת מוצר באייקון עגלה
        return self.driver.find_elements_by_css_selector("[class='removeProduct iconCss iconX']")


###############################################################################################


class CategoryPage:
    def __init__(self, driver):
        self.driver = driver

    def GetProducts(self):
        return self.driver.find_elements_by_css_selector("img[class='imgProduct']")

    def BackToHomepage(self):
        return self.driver.find_element_by_xpath('// a[ @ translate = "HOME"]')


###############################################################################################

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def SwitchColor(self, color):
        return self.driver.find_element_by_xpath(f"//span[@title='{color.upper()}']")

    def PlusQuantity(self, quantity):
        for i in range(quantity):
            self.driver.find_element_by_xpath("//div[@class='plus']").click()

    def AddToCartButton(self):
        self.driver.find_element_by_xpath('//button[@name="save_to_cart"]').click()

    def BackToCategory(self):
        return self.driver.find_element_by_xpath('//a[@class="ng-binding"]')


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

# hp1=HomePage(driver)
# sleep(8)
# hp1.CategoryIcon("Headphones").click()
# cp=CategoryPage(driver)
# sleep(3)
# list1=cp.GetProducts()
# print(len(list1))
# list1[1].click()
# sleep(3)
# pp1=ProductPage(driver)
# pp1.BackToCategory().click()
# sleep(3)
# try:
#    list1[0].click()
# except StaleElementReferenceException as Exception:
#    print("Product not sync with the page document anymore")
#    list1=cp.GetProducts()
#    list1[0].click()
# pp1.PlusQuantity(3)
# pp1=ProductPage(driver)
# pp1.SwitchColor("gray").click()
# pp1.BackToCategory().click()
# cp.BackToHomepage().click()

if __name__ == '__main__':
    main()

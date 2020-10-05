from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def CategoryIcon(self, category):
        self.driver.find_element_by_id(f"{category.lower()}Img").click()

    def HomePageValidation(self):
        return self.driver.find_elements_by_xpath("//div[@href='javascript:void(0)']")


    def LogoIcon(self):
        self.driver.find_element_by_id("Layer_1").click()

    def WaitToHomepage(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "headphonesImg")))



# --------------------------------------------------------------------------------------------------------------



class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def ProductPriceInCart(self,index):
        #index+=3
        return self.driver.find_elements_by_xpath('//p [@class="price roboto-regular ng-binding"]')[index].text

    def ProductNameInCart(self,index):
        return self.driver.find_elements_by_xpath('//label [@class="roboto-regular productName ng-binding"]')[index].text

    def ProductQtyInCart(self,index):
        return self.driver.find_elements_by_xpath('//tbody/tr/td/label [@class="ng-binding"]')[index].text

    def EditButton(self,index): # לחיצה כל כפתור עריכה של מוצר ספציפי בעגלת הקניות
         self.driver.find_elements_by_css_selector("a[class='edit ng-scope']")[index].click()

    def CheckOutButton(self):
        self.driver.find_element_by_xpath("//button[@class='roboto-medium tami uft-class ng-binding']").click()

    def Quantity(self,index):
        return self.driver.find_elements_by_css_selector("tbody>tr>td>label[class='ng-binding']")[index].text

    def ShoppingCartText(self):
        return self.driver.find_element_by_class_name("select").text

    def TotalPrice(self):
        return self.driver.find_element_by_xpath('// *[ @ id = "shoppingCart"] / table / tfoot / tr[1] / td[2] / span[2]').text

    def CheckoutButtonCartpage(self):
        self.driver.find_element_by_xpath("//button[@class='roboto-medium tami uft-class ng-binding']").click()



    def WaitToCartPage(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CLASS_NAME, "sticky")))



# --------------------------------------------------------------------------------------------------------------



class CartIcon:
    def __init__(self, driver):
        self.driver = driver

    def CartIcon(self):
        return self.driver.find_element_by_id("shoppingCartLink")

    def NumberOfProducts(self):
        return self.driver.find_element_by_css_selector("nav>ul>li>a>span[class='cart ng-binding']").text

    def LengthListOfProducts(self):
        return len(self.driver.find_elements_by_xpath('//img [@class="imageUrl"]'))

    def WaitToCartIcon(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//li//table[@ng-show='cart.productsInCart.length > 0']")))

    def QtyInCartIcon(self, index):
         list1 = self.driver.find_elements_by_xpath("//label[contains(text(),'QTY')]")
         list1 = self.ReplaceList(list1)
         Qty = list1[index].text[5:]
         return int(Qty)

    def PriceInCartIcon(self, index):
        list1 = self.driver.find_elements_by_class_name("price")
        list1 = self.ReplaceList(list1)
        Price = list1[index].text[1:]
        Price = Price.replace(',','')
        return float(Price)

    def ColorInCartIcon(self, index):
        list1 = self.driver.find_elements_by_css_selector("span[class='ng-binding']")
        list1 = self.ReplaceList(list1)
        Color = list1[index].text
        return Color

    def NameInCartIcon(self, index):
        list1 = self.driver.find_elements_by_css_selector("h3[class='ng-binding']")
        list1 = self.ReplaceList(list1)
        Name = list1[index].text[:-3]
        return Name

    def RemoveInCartIcon(self, index):
        return self.driver.find_elements_by_css_selector("[class='removeProduct iconCss iconX']")[index].click()
    def LengthListOfProducts(self): #quantity of list of products in cart icon
        return len(self.driver.find_elements_by_xpath('//img [@class="imageUrl"]'))


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

    def TabletsCategoryValidation(self):
        return self.driver.find_elements_by_xpath("//h4[@href='javascript:void(0)']")

    def RandomCategoryCheck(self,list1,category):
        bool=True
        while bool:
            if category in list1:
                category = randint(0, 4)
            else:
                list1.append(category)
                bool=False
        return category

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
        list1.append(self.driver.find_element_by_xpath("//span[contains(@class,'colorSelected')]").get_attribute('title'))  # Color
        list1.append("")  # Quantity
        price = self.driver.find_element_by_css_selector("article>div>div>h2[class='roboto-thin screen768 ng-binding']").text[1:]
        price = price.replace(',','')
        list1.append(price)  # Price
        return list1

    def RandomQuantityCheck(self,list1,quantity): #check that quantity not used
        bool=True
        while bool:
            if quantity in list1:
                quantity = randint(0, 4)
            else:
                list1.append(quantity)
                bool=False
        return quantity

    def RandomProductCheck(self,category,product,length): #check that product isn't sold out
        bool1=True
        while bool1:
            if category==0 and product==1:
                product=randint(0,length-1)
            else:
                bool1=False
        return product


    def WaitToProductpage(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "save_to_cart")))

class OrderPaymentPage:

    def __init__(self,driver):
        self.driver=driver

    def InsertUserExist(self,username,password): #insert details of user exist
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
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="userDetails"]')))

    def WaitToPaymentMethodPage(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="paymentMethods"]')))

    def WaitToOrderCompletePage(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="seccion borderRight"]')))

    def WaitToEmptyCart(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//label[@translate="Your_shopping_cart_is_empty"]')))

class UserIcon:
    def __init__(self,driver):
        self.driver=driver

    def UserOrdersEnter(self): #enter to my orders page
        self.driver.find_element_by_xpath('//a[@id="menuUserLink"]').click()
        self.driver.find_element_by_xpath('//a/div/label[@translate="My_Orders"]').click()

    def OrderInList(self,ordernumber): #check if order number in my orders
        list1=self.driver.find_elements_by_css_selector("label[class='ng-binding']")
        reversed(list1)
        for i in range(len(list1)):
            if list1[i].text == ordernumber:
                return True
        return False

    def WaitToMyOrdersPage(self):
        WebDriverWait(self.driver, 16).until(EC.presence_of_element_located((By.XPATH, '//label[@class="center ng-binding"]')))


    def EqualProduct(self, list1, list2):  # Check if product that added to cart , appearing good in cart icon
        for i in range(3): #  debug
            for x in range(4):
                print("list2")    # debug
                print(list2[i][x])     # debug
                print("list1")    # debug
                print(list1[i][x])     # debug


        for i in range(len(list1)):
            if str(list2[i][0]) not in str(list1[i][0]):   # First , check the name (Substring)
                return False
            for x in range(1,4):
                if list2[i][x] == list1[i][x]:
                    continue
                else:
                    return False
        return True



# --------------------------------------------------------------------------------------------------------------



class OrderPaymentPage:

    def __init__(self,driver):
        self.driver=driver

    def LoginUser(self,username,password):  #  Insert Username & password to SignIn
        self.driver.find_element_by_xpath('//input[@name="usernameInOrderPayment"]').send_keys(username)
        self.driver.find_element_by_xpath('//input[@name="passwordInOrderPayment"]').send_keys(password)

    def RegisterUser(self,username,email,password):  # SignUp with a new account
        self.driver.find_element_by_css_selector("input[name='usernameRegisterPage']").send_keys(username)
        self.driver.find_element_by_css_selector("input[name='passwordRegisterPage']").send_keys(password)
        self.driver.find_element_by_css_selector("input[name='confirm_passwordRegisterPage']").send_keys(password)
        self.driver.find_element_by_css_selector("input[name='emailRegisterPage']").send_keys(email)
        self.driver.find_element_by_css_selector("input[name='i_agree']").click()
        self.driver.find_element_by_id("register_btnundefined").click()

    def RegisterButton(self):
        self.driver.find_element_by_id("registration_btnundefined").click()

    def LoginButton(self):
        self.driver.find_element_by_xpath('//button[@id="login_btnundefined"]').click()

    def NextButton(self):
        self.driver.find_element_by_xpath('//button[@class="a-button nextBtn marginTop75 ng-scope"]').click()

    def EditButton(self):
        self.driver.find_element_by_xpath('//label[@class="edit  ng-scope"]').click()

    def PayNowSafePay(self):
        self.driver.find_element_by_id("pay_now_btn_SAFEPAY").click()

    def SafePayDetails(self):
        self.driver.find_element_by_xpath("//input[@name='safepay_username']").send_keys("11223344")
        self.driver.find_element_by_xpath("//input[@name='safepay_password']").send_keys("11223344Pp")

    def GetOrderNumber(self):
       return self.driver.find_element_by_xpath('//label[@id="orderNumberLabel"]').text

    def WaitToOrderPaymentPage(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h5[@translate='ORDER_SUMMARY']")))

    def WaitToShippingDetailsPage(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//label[@class="roboto-regular ng-binding selected"]')))

    def WaitToPaymentMethodPage(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="paymentMethods"]')))

    def WaitToOrderCompletePage(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="seccion borderRight"]')))

    def WaitToRegisterPage(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h3[translate="ACCOUNT_DETAILS"]')))



# --------------------------------------------------------------------------------------------------------------



class UserIcon:

    def __init__(self,driver):
        self.driver=driver

    def UserIcon(self):
        return self.driver.find_element_by_id("menuUserLink")

    def LoginUserIcon(self,username,password):
        self.driver.find_element_by_css_selector("input[name='username']").send_keys(username)
        self.driver.find_element_by_css_selector("input[name='password']").send_keys(password)
        self.driver.find_element_by_id("sign_in_btnundefined").click()

    def LogoutUserIcon(self):
        self.driver.find_element_by_css_selector("a>div>label[translate='Sign_out']").click()

    def UserName(self):
        return self.driver.find_element_by_css_selector("nav>ul>li>a>span[data-ng-show='userCookie.response']").text

    def UserOrdersEnter(self):
        self.driver.find_element_by_xpath('//a[@id="menuUserLink"]').click()
        self.driver.find_element_by_xpath('//a/div/label[@translate="My_Orders"]').click()

    def OrderInList(self, order_number):
        list1 = self.driver.find_elements_by_css_selector("label[class='ng-binding']")
        for i in range(len(list1)):
            if list1[i].text == order_number:
                return True
        return False

    def WaitToLogIn(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    def WaitToMyOrdersPage(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//label[@class="ng-binding"]')))